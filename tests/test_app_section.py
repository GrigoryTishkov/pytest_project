import pytest
from framework.config_reader import ConfigReader
from framework.validators import ConfigValidator


@pytest.fixture()
def config():
    reader = ConfigReader()
    return reader.read_config()


def test_config_app_section_exists(config):
    assert 'App' in config.sections()

@pytest.mark.parametrize("param,validator,args",[
                        ("Name", "string_validator", None),
                        ("Version", "version_validator", None),
                        ("DebugMode", "bool_validator", None),
                        ("MaxThreads", "integer_validator", (1, 16))
])
def test_app_validator(config, param, validator, args):
    assert param in config['App'], f'Параметр {param} отсутствует в [App]'
    value = config['App'][param]
    validate_func = getattr(ConfigValidator, validator)
    if args:
        assert validate_func(value, *args), f'Тест упал на {param}={value}'
    else:
        assert validate_func(value), f'Тест упал на {param}={value}'

def test_app_validator_null():
    pass

