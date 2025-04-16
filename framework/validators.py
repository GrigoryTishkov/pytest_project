import re
from pathlib import Path


class ConfigValidator:
    @staticmethod
    def string_validator(value):
        return str(value)

    @staticmethod
    def version_validator(value):
        pattern_version = re.compile(r'^\d+\.\d+\.d+$', re.I)
        return bool(pattern_version.match(str(value).strip()))

    @staticmethod
    def bool_validator(value):
        return str(value).lower() in ("true", "false")

    @staticmethod
    def threads_validator(value):
        try:
            num = int(value)
            return 1 <= num <= 16
        except(ValueError, TypeError):
            return False

    @staticmethod
    def log_level_validator(value):
        return str(value) in ("debug", "info", "warning", "error")

