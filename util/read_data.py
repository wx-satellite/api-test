import os
import json


class HandleErrorCodeMessageType:
    base_path = os.path.dirname(__file__)

    def __init__(self, file_name):
        file_path = self.base_path + "/../data/" + file_name
        with open(file_path, encoding="utf-8") as f:
            self.data = json.loads(f)

    def get_value(self, url):
        return self.data.get(url)

    def get_message(self, url, code):
        info = self.data.get(url)
        if info is None:
            return ""
        return info.get(code)
