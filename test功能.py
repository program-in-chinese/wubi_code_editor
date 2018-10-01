import unittest
from 功用.功能 import *


class test功能(unittest.TestCase):

    def test_合法unicode(self):
        self.assertEqual(功能.组成图片子路径("3400"), "Plane00/U_003400")
        self.assertEqual(功能.组成图片子路径("13400"), "Plane01/U_013400")
        self.assertEqual(功能.组成图片子路径("23400"), "Plane02/U_023400")
        self.assertEqual(功能.组成图片子路径("33400"), "Plane03/U_033400")
        self.assertEqual(功能.组成图片子路径("E3400"), "Plane14/U_0E3400")
        self.assertEqual(功能.组成图片子路径("F3400"), "Plane15/U_0F3400")
        self.assertEqual(功能.组成图片子路径("103400"), "Plane16/U_103400")

if __name__ == '__main__':
    unittest.main()
