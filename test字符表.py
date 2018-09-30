import unittest
import 字符表

字符1 = ['1111', '一', 'a', 'b', 'c', 1, 1]
字符2 = ['2222', '二', 'b', 'c', 'd', 2, 2]


class test_字符表(unittest.TestCase):

    字符表 = 字符表.字符表()

    def test_0_添加字符(self):
        self.字符表.添加所有字符([字符1])
        self.assertEqual(self.字符表.取所有字符(), [字符1])
        self.字符表.添加所有字符([字符2])
        self.assertEqual(self.字符表.取所有字符(), [字符1, 字符2])

    def test_1_取当前字符(self):
        self.assertEqual(self.字符表.取当前字符(), 字符1)


if __name__ == '__main__':
    unittest.main()
