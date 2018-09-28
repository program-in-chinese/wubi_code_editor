class 字符表:
    当前字符序号 = 0
    字符列表 = []

    def 添加所有字符(self, 子字符列表):
        self.字符列表.extend(子字符列表)

    def 取当前字符(self):
        # TODO: 判断序号范围
        return self.字符列表[self.当前字符序号]

    def 取上一个字符(self):
        if (self.当前字符序号 > 0):
            self.当前字符序号 -= 1
        print("字符序号: " + str(self.当前字符序号))

    def 取下一个字符(self):
        if (self.当前字符序号 < len(self.字符列表)):
            self.当前字符序号 += 1
        print("字符序号: " + str(self.当前字符序号))

    def 置当前字符序号(self, 新序号):
        self.当前字符序号 = 新序号

    def 修改当前字符(self, 编码86版值, 编码98版值, 编码06版值):
        当前字符 = self.取当前字符()
        当前字符[2] = 编码86版值
        当前字符[3] = 编码98版值
        当前字符[4] = 编码06版值
        print("已修改: " + str(当前字符))

    def 取所有字符(self):
        return self.字符列表
