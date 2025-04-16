from pathlib import Path
import configparser
import os


class ConfigReader:
    def __init__(self, config_path=None):
        self.config_path = config_path or os.getenv('CONFIG_PATH', 'config.ini')
        self.config = configparser.ConfigParser()

    def read_config(self):
        if not Path(self.config_path).exists():
            raise FileNotFoundError(f"Файл не найден в {self.config_path}")
        self.config.read(self.config_path)
        return self.config
