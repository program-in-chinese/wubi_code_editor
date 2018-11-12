import csv
import 常量
import 字符表
from tkinter import *
from functools import partial

from 功用.csv文件处理 import csv文件处理
from 功用.功能 import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.字符表 = 字符表.字符表()
        self.创建控件()

    def 修改当前条目(self):
        self.字符表.修改当前字符(self.编码86版值.get(),
                        self.编码98版值.get(), self.编码06版值.get())
        源数据文件路径 = 常量.源数据路径 + 常量.源数据文件[self.字符表.取当前字符区间号()]
        字符区间 = self.字符表.取当前字符区间()
        csv文件处理.写数组到文件(self.字符表.取所有字符()[字符区间[0]:字符区间[1]], 源数据文件路径)

    # TODO: 提示已到开头/末尾
    def 上一个字符(self):
        self.字符表.取上一个字符()
        self.刷新控件()

    def 下一个字符(self):
        self.字符表.取下一个字符()
        self.刷新控件()

    def 创建字体区(self, 区域, 地区名):
        字体区 = Frame(区域)
        字体区.pack()
        字体区提示 = Label(字体区, text=地区名 + "字形")
        字体区提示.pack()
        字体显示 = Frame(字体区)
        字体显示.pack()
        for 字体 in 常量.按地区名取字体列表[地区名]:
            self.按字体取图片显示[字体] = self.创建图片显示(字体显示, 字体, "left")

    # 显示图片, 参考: https://stackoverflow.com/questions/35024118/how-to-load-an-image-into-a-python-3-4-tkinter-window
    def 创建图片显示(self, 区域, 字体名, 位置):
        字体区 = Frame(区域)
        字体区.pack(side=位置)
        字体提示 = Label(字体区, text=字体名)
        字体提示.pack()
        图片 = self.按字体取图片(字体名)
        图片显示 = Label(字体区, image=图片)
        图片显示.image = 图片
        图片显示.pack()
        return 图片显示

    def 创建五笔编码编辑区(self, 区域, 年份, 值):
        编码区 = Frame(区域)
        编码区.pack()
        编码提示 = Label(编码区, text="编码" + 年份 + "版")
        编码提示.pack(side="left")
        # 参考 https://stackoverflow.com/questions/20125967/how-to-set-default-text-for-a-tkinter-entry-widget
        编码值 = StringVar(value=值)
        编码 = Entry(编码区, textvariable=编码值)
        编码.pack(side="right")
        return 编码值

    def 创建只读区(self, 区域, 提示文本, 值):
        # 显示文本, 参考https://www.python-course.eu/tkinter_labels.php
        区 = Frame(区域)
        区.pack()
        显示提示 = Label(区, text=提示文本)
        显示提示.pack(side="left")
        可变值 = StringVar(value=值)
        显示 = Label(区, textvariable=可变值)
        显示.pack(side="right")
        return 可变值

    def 组成图片子路径(self, Unicode码):
        return 功能.组成图片子路径(Unicode码) + 常量.图片扩展名

    def 创建控件(self):
        self.按字体取图片显示 = {}

        for 文件名 in 常量.源数据文件:
            self.字符表.添加所有字符(csv文件处理.读文件到数组(常量.源数据路径 + 文件名))

        self.IRG表 = 功能.数组前两列转换为表(csv文件处理.读IRG文件到数组(常量.IRG数据路径))

        当前字符 = self.字符表.取当前字符()

        图片区 = Frame(self)
        图片区.pack(side="left")

        for 地区名 in 常量.按地区名取字体列表.keys():
            self.创建字体区(图片区, 地区名)

        细节区 = Frame(self)
        细节区.pack(side="right")
        self.Unicode编码值 = self.创建只读区(细节区, "Unicode编码", 当前字符[0])
        self.Unicode编码区 = self.创建只读区(细节区, "Unicode编码区", 常量.源数据文件[self.字符表.取当前字符区间号()][:-4])
        self.中国大陆笔顺值 = self.创建只读区(细节区, "中国大陆笔顺", "共" + str(len(当前字符[5])) + "画:" + 当前字符[5])
        self.中国台湾笔顺值 = self.创建只读区(细节区, "中国台湾笔顺", "共" + str(len(当前字符[6])) + "画:" + 当前字符[6])

        self.IRGSource值 = self.创建只读区(细节区, "IRGSource", self.构建IRG显示(当前字符[0]))
        修改区 = Frame(细节区)
        修改区.pack()
        可改编码区 = Frame(修改区)
        可改编码区.pack(side="left")
        self.编码86版值 = self.创建五笔编码编辑区(可改编码区, "86", 当前字符[2])
        self.编码98版值 = self.创建五笔编码编辑区(可改编码区, "98", 当前字符[3])
        self.编码06版值 = self.创建五笔编码编辑区(可改编码区, "06", 当前字符[4])

        修改按钮 = Button(修改区, text="修改", command=self.修改当前条目)
        修改按钮.pack(side="right")

        遍历区 = Frame(细节区)
        遍历区.pack()
        上一个 = Button(遍历区, text="上一个", command=self.上一个字符)
        上一个.pack(side="left")

        下一个 = Button(遍历区, text="下一个", command=self.下一个字符)
        下一个.pack(side="right")

        搜索区 = Frame(细节区)
        搜索区.pack()
        搜索值 = StringVar(value="")
        搜索输入 = Entry(搜索区, textvariable=搜索值)
        搜索输入.pack(side="left")

        搜索 = Button(搜索区, text="按Unicode或字搜索",
                           command=lambda: self.按Unicode或字搜索(搜索值.get()))
        搜索.pack(side="right")

    def 构建IRG显示(self, Unicode码):
        IRG显示 = ""
        for 某键值 in 常量.IRG键值:
            状态 = ""
            if (常量.IRG值前缀 + 某键值 + 常量.IRG值后缀) in self.IRG表[Unicode码]:
                状态 = "√"
            else:
                状态 = "×"
            IRG显示 += 某键值 + 状态 + "  "
        return IRG显示

    def 按Unicode或字搜索(self, 搜索框输入):
        已找到 = False
        输入为字 = len(搜索框输入) == 1
        if (输入为字):
            已找到 = self.字符表.按字置当前字符(搜索框输入)
        else:
            已找到 = self.字符表.按Unicode码置当前字符(搜索框输入)
        if 已找到:
            self.刷新控件()
        else:
            if (输入为字):
                print("未找到字: " + 搜索框输入)
            else:
                print("未找到Unicode码: " + 搜索框输入)

    def 刷新图片显示(self, 图片显示, 字体名):
        图片 = self.按字体取图片(字体名)
        图片显示.configure(image=图片)
        图片显示.image = 图片

    def 按字体取图片(self, 字体名):
        try:
            return PhotoImage(file=常量.图片主目录 + 常量.图片路径[字体名] + self.组成图片子路径(self.字符表.取当前字符()[0][2:]))
        except:
            return PhotoImage(file=常量.无字体图片)

    # 只读部分如果为空, 显示'无', 而不是空白
    def 显示只读项(self, 值):
        return 常量.无 if not 值 else 值

    def 刷新控件(self):
        当前字符 = self.字符表.取当前字符()
        print("当前字符: " + str(当前字符))

        for 字体 in 常量.图片路径.keys():
            self.刷新图片显示(self.按字体取图片显示[字体], 字体)

        self.Unicode编码值.set(self.显示只读项(当前字符[0]))
        self.Unicode编码区.set(常量.源数据文件[self.字符表.取当前字符区间号()][:-4])
        self.编码86版值.set(当前字符[2])
        self.编码98版值.set(当前字符[3])
        self.编码06版值.set(当前字符[4])
        self.中国大陆笔顺值.set(self.显示只读项("共" + str(len(当前字符[5])) + "画:" + 当前字符[5]))
        self.中国台湾笔顺值.set(self.显示只读项("共" + str(len(当前字符[6])) + "画:" + 当前字符[6]))
        self.IRGSource值.set(self.构建IRG显示(当前字符[0]))

root = Tk()
app = Application(master=root)
app.mainloop()
