import pytest
from framework.config_reader import ConfigReader
from framework.validators import ConfigValidator

@pytest.fixture()
def config():
    reader = ConfigReader()
    return reader.read_config()

def test_database_section_exists(config):
    assert 'Database' in config.sections()

@pytest.mark.parametrize("param,validator,args",[
                        ("Host", "string_validator", None),
                        ("Port", "integer_validator", (1, 65535)),
                        ("Username", "string_validator", None),
                        ("Password", "string_validator", None),
                        ("Name", "database_validator", None),
                        ("PoolSize", "integer_validator", (1, 20))
])
def test_database_section_parameters(config, param, validator, args):
    assert param in config['Database'], f'Параметр {param} отсутствует в секции [Database]'
    value = config['Database'][param]
    validator_func = getattr(ConfigValidator, validator)
    if args:
        assert validator_func(value, *args), f'Тест упал на {param}={value}'
    else:
        assert validator_func(value), f'Тест упал на {param}={value}'

def test_database_section_null(config):
    allowed_params = {"Host", "Port", "Username", "Password", "Database", "Name", "PoolSize"}
    actual_params = set(config['Database'].keys())
    unexpected_params = actual_params - allowed_params
    assert not unexpected_params, f'Параметры {unexpected_params} не допустимы'
