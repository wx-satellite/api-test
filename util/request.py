import requests
import json


class Request:
    headers = None
    cookies = None
    res = None

    # 设置头信息
    def set_header(self, key, value):
        self.headers[key] = value
        return self

    def set_cookie(self, key, value):
        self.cookies[key] = value
        return self

    def __send_post(self, url, data):
        self.res = requests.post(url=url, data=data, headers=self.headers, cookies=self.cookies)

    def __send_get(self, url, data):
        self.res = requests.get(url=url, params=data, headers=self.headers, cookies=self.cookies)

    def do_request(self, method, url, data=None):
        if "get" == method:
            self.__send_get(url, data)
        else:
            self.__send_post(url, data)
        return self

    def get_json_result(self):
        try:
            res = json.loads(self.res)
        except json.JSONDecodeError as e:
            print("请求返回的结果不是json字符串")
            res = {}
        return res

    def get_cookie_result(self):
        # 直接 response.cookies 返回的是 CookieJar，需要转成字典
        return requests.utils.dict_from_cookiejar(self.res.cookies)


request = Request()
