import unittest
import ddt

data = [
    [
        1, 2, 3, 4
    ],
    [
        2, 3, 4, 5
    ],
    [
        3, 4, 5, 6
    ]
]


# 数据驱动
@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束\n")

    # * 会打散列表
    @ddt.data(*data)
    def test_01(self, row_value):
        num1, num2, num3, num4 = row_value
        print(num1, num2, num3, num4)


if __name__ == "__main__":
    unittest.main()
