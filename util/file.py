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


class ReadOrWriteLoginStatus:
    base_path = os.path.dirname(__file__)

    def __init__(self, file_name=None):
        if file_name is None:
            file_name = "login_status.json"
        self.file_path = self.base_path + "/../data/" + file_name

    def write(self, login_status, flag="web"):
        ori_data = self.read()
        ori_data[flag] = login_status
        with open(self.file_path, encoding="utf-8", mode="w") as f:
            f.write(json.dumps(ori_data))

    def read(self, flag=""):
        with open(self.file_path, encoding="utf-8", mode="r") as f:
            content = f.read()
            # 文件内容为空时
            data = {} if len(content) <= 0 else json.loads(content)

        return data if len(flag) <= 0 else ({} if flag not in data else data[flag])


if __name__ == "__main__":
    read = ReadOrWriteLoginStatus()
    read.write({"token": "1asdashduy7qw726736273asgdsakabsxkbkx"})

    print(read.read("web"))
