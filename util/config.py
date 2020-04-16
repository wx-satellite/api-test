import configparser
import os


class Config:
    def __init__(self, path=None):
        if path is None:
            self.path = os.path.dirname(__file__) + "/../config.ini"
        self.config_handle = configparser.ConfigParser()
        # 参考：https://blog.csdn.net/qq_34332010/article/details/74261725
        self.config_handle.read(self.path,encoding="utf-8")

    def get_value(self, key, section="server", default=""):
        return self.config_handle.get(section, key, fallback=default)
