from util.excel import Excel
import json
from jsonpath_rw import parse

'''
获取依赖数据，解析 excel文件 前置条件 的值
1>data.banner.id  其中 1 表示case编号， data.banner.id 表示获取编号为1的接口返回结果的id值
case编号 列的值 与 实际excel对应的行编号 相差 1
'''


# 返回依赖数据，配合 依赖key 一起使用，最后追加到 请求data 中
def get_rely_data(value):
    values = value.split(">")
    num = int(values[0]) + 1  # 获取对应的行编号
    path = values[1]
    excel = Excel()
    result_data = excel.get_row_value_from_target_sheet(row_index=num).pop()
    result_data = json.loads(result_data)
    # jsonpath_rw 解析规则：data.banner.id 中间必须是 "."
    # 当banner为数组时需要制定解析第几个： data.banner.[0].id
    p = parse(path)
    return p.find(result_data)[0].value


if __name__ == "__main__":
    get_rely_data("1>data.banner.[1].id")
