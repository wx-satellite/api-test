import unittest
import ddt
from util.excel import Excel
from util.help import get_rely_data
import json
from util.file import ReadOrWriteLoginStatus, ReadStandardApiReturn
from util.request import Request
from util.check import CheckJson
import os
import HtmlTestRunner

excel = Excel()
excel_data = [row for row in range(2, excel.get_row_nums() + 1)]

case_num = 2


# 数据驱动测试
@ddt.ddt
class TestRunCaseDDT(unittest.TestCase):

    def tearDown(self):
        global case_num
        case_num = case_num + 1

    @ddt.data(*excel_data)
    def test_main(self, case):  # case为excel每一行的值
        # 是否执行
        is_run = case[2]
        if "yes" == is_run:
            # 依赖数据
            is_depend = case[3]
            # 请求数据
            request_data = json.loads(case[7])
            if is_depend:
                # 依赖key
                depend_key = case[4]
                depend_data = get_rely_data(is_depend)
                # 将依赖数据设置到请求参数中
                request_data[depend_key] = depend_data
            # 请求方式
            request_method = case[6]
            # 请求地址
            request_url = case[5]

            # 读取请求信息
            header_info = json.loads(case[9])

            # 登录状态
            login_status_method = case[8]

            need_write_login_status = False

            # 将登陆状态写入到文件中
            if "write" == login_status_method:
                need_write_login_status = True
            # 将登录状态携带到头信息中
            if "read" == login_status_method:
                login_status = ReadOrWriteLoginStatus()
                token_info = login_status.read("api")
                header_info["Authorization"] = token_info["token"]

            # 请求
            request = Request()
            request.do_request(request_method, request_url, request_data)

            # 是否需要写入cookie
            if need_write_login_status:
                print(request.get_cookie_result())

            # 获取接口的返回值
            result = request.get_json_result()

            # 预期结果校验方式
            except_method = case[10]

            if "errorCodeMessage" == except_method:
                pass

            if "errorCode" == except_method:
                pass

            # 这里认为 json 模式就是表明api正确返回
            if "json" == except_method:
                check = CheckJson()
                # 检测api正确返回的结构是否和配置文件中一致
                ok = check.check_api_key_return(request_url, request)
                try:
                    # 断言失败会抛出异常
                    self.assertTrue(ok)
                    # 回写测试结果
                    excel.set_cell_value_from_target_sheet(case_num, 12, "通过")
                except Exception as e:
                    excel.set_cell_value_from_target_sheet(case_num, 12, "失败")
                    raise e
                finally:
                    # 回写api请求结果
                    excel.set_cell_value_from_target_sheet(case_num, 13, json.dumps(result))
                    excel.save()


if __name__ == "__main__":
    base_path = os.getcwd()
    report_path = base_path + "/reports/report.html"
    suit = unittest.defaultTestLoader.discover(start_dir=base_path, pattern="run.py")
    with open(report_path, "wr") as f:
        runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_title="接口测试报告", descriptions="测试阿测试")
        # Runs the given testCase or testSuite
        runner.run(suit)
