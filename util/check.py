from deepdiff import DeepDiff

from util.file import ReadStandardApiReturn


class CheckJson:
    read = None

    def __init__(self):
        if self.read is None:
            self.read = ReadStandardApiReturn()

    def check_api_key_return(self, url, result):
        standard = self.read.get_standard(url)
        return self.key_is_ok(standard, result)

    def check_api_value_return(self, url, result):
        standard = self.read.get_standard(url)
        return self.value_is_ok(standard, result)

    # 返回的结构是否一致
    @classmethod
    def key_is_ok(cls, dict1, dict2):
        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            return False
        res = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        return res.get("dictionary_item_added") is None and res.get("dictionary_item_removed") is None

    # 返回的值是否一致
    @classmethod
    def value_is_ok(cls, dict1, dict2):
        if not isinstance(dict1, dict) or not  isinstance(dict2,dict):
            return False
        res = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        return res.get("values_changed") is None


if __name__ == "__main__":
    check = CheckJson()
    print(check.check_api_key_return("login", {"code": -1, "message": "用户名或者密码错误", "data": None}))
