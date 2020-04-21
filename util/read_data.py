import os
import json


class ReadErrorCodeMessage:
    base_path = os.path.dirname(__file__)

    def __init__(self, file_name=None):
        if file_name is None:
            file_name = "error_code_message.json"
        file_path = self.base_path + "/../data/" + file_name
        with open(file_path, encoding="utf-8") as f:
            self.data = json.loads(f.read())

    def get_value(self, url):
        return self.data.get(url)

    def get_message(self, url, code):
        info = self.data.get(url)
        if info is None:
            return ""
        return info.get(code)


class ReadStandardApiReturn:
    base_path = os.path.dirname(__file__)

    def __init__(self, file_name=None):
        if file_name is None:
            file_name = "standard_api_return.json"
        file_path = self.base_path + "/../data/" + file_name
        with open(file_path, encoding="utf-8") as f:
            self.data = json.loads(f.read())

    def get_standard(self, url):
        return self.data.get(url)
