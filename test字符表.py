import unittest
import 字符表

字符1 = ['1111', '一', 'a', 'b', 'c', 1, 1]
字符2 = ['2222', '二', 'b', 'c', 'd', 2, 2]


class test字符表(unittest.TestCase):

    字符表 = 字符表.字符表()

    def test_0_添加字符(self):
        self.字符表.添加所有字符([字符1])
        self.assertEqual(self.字符表.取所有字符(), [字符1])
        self.字符表.添加所有字符([字符2])
        self.assertEqual(self.字符表.取所有字符(), [字符1, 字符2])

    def test_1_取当前字符(self):
        self.assertEqual(self.字符表.取当前字符(), 字符1)

    def test_2_取当前字符区间号(self):
        self.assertEqual(self.字符表.取当前字符区间号(), 0)
        self.assertEqual(self.字符表.取当前字符区间(), (0, 1))

    def test_3_取下一个字符(self):
        self.字符表.取下一个字符()
        self.assertEqual(self.字符表.取当前字符(), 字符2)

    def test_4_取当前字符区间号(self):
        self.assertEqual(self.字符表.取当前字符区间号(), 1)
        self.assertEqual(self.字符表.取当前字符区间(), (1, 2))

    def test_5_取下一个字符失败(self):
        self.字符表.取下一个字符()
        self.assertEqual(self.字符表.取当前字符(), 字符2)

    def test_6_取上一个字符(self):
        self.字符表.取上一个字符()
        self.assertEqual(self.字符表.取当前字符(), 字符1)

    def test_7_取上一个字符失败(self):
        self.字符表.取上一个字符()
        self.assertEqual(self.字符表.取当前字符(), 字符1)

if __name__ == '__main__':
    unittest.main()
