import re
from pathlib import Path


class ConfigValidator:
    @staticmethod
    def string_validator(value):
        return str(value)

    @staticmethod
    def version_validator(value):
        return re.match(r'^\d+\.\d+\.\d+$', value) is not None

    @staticmethod
    def bool_validator(value):
        return str(value).lower() in ("true", "false")

    @staticmethod
    def integer_validator(value, min_value, max_value):
        try:
            num = int(value)
            return min_value <= num <= max_value
        except(ValueError, TypeError):
            return False

    @staticmethod
    def log_level_validator(value):
        return str(value) in ("debug", "info", "warning", "error")
    
    @staticmethod
    def database_validator(value):
        return re.match(r'^[a-zA-Z0-9]+$', value) is not None

