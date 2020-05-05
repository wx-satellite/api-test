import requests
import json


class BaseRequest:
    headers = {}
    cookies = {}

    def set_header(self, key, value):
        self.headers[key] = value

    def set_cookie(self, key, value):
        self.cookies[key] = value

    def __send_post(self, url, data):
        res = requests.post(url=url, data=data, headers=self.headers, cookies=self.cookies).text
        return res

    def __send_get(self, url, data):
        res = requests.get(url=url, params=data, headers=self.headers, cookies=self.cookies).text
        return res

    def run(self, method, url, data=None):
        if "get" == method:
            res = self.__send_get(url, data)
        else:
            res = self.__send_post(url, data)
        try:
            res = json.loads(res)
        except json.JSONDecodeError as e:
            print("请求返回的结果不是json字符串")
            res = {}
        return res


request = BaseRequest()
