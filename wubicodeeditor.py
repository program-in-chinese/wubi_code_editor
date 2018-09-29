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

    def 导出文件(self):
        csv文件处理.写数组到文件(self.字符表.取所有字符(), 常量.修改后文件)

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

        当前字符 = self.字符表.取当前字符()

        图片区 = Frame(self)
        图片区.pack(side="left")

        for 地区名 in 常量.按地区名取字体列表.keys():
            self.创建字体区(图片区, 地区名)

        细节区 = Frame(self)
        细节区.pack(side="right")
        self.Unicode编码值 = self.创建只读区(细节区, "Unicode编码", 当前字符[0])

        self.笔顺值 = self.创建只读区(细节区, "笔顺", 当前字符[5])

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
        搜索Unicode值 = StringVar(value="")
        Unicode值输入 = Entry(搜索区, textvariable=搜索Unicode值)
        Unicode值输入.pack(side="left")

        搜索Unicode = Button(搜索区, text="搜索Unicode",
                           command=lambda: self.搜索Unicode(搜索Unicode值.get()))
        搜索Unicode.pack(side="right")

        导出按钮 = Button(细节区, text="导出文件", command=self.导出文件)
        导出按钮.pack()

    def 搜索Unicode(self, Unicode值输入):
        if self.字符表.按Unicode码置当前字符(Unicode值输入):
            self.刷新控件()
        else:
            print("未找到Unicode码: " + Unicode值输入)

    def 刷新图片显示(self, 图片显示, 字体名):
        图片 = self.按字体取图片(字体名)
        图片显示.configure(image=图片)
        图片显示.image = 图片

    def 按字体取图片(self, 字体名):
        try:
            return PhotoImage(file=常量.图片主目录 + 常量.图片路径[字体名] + self.组成图片子路径(self.字符表.取当前字符()[0]))
        except:
            return PhotoImage(file=常量.无字体图片)

    def 刷新控件(self):
        当前字符 = self.字符表.取当前字符()
        print("当前字符: " + str(当前字符))

        for 字体 in 常量.图片路径.keys():
            self.刷新图片显示(self.按字体取图片显示[字体], 字体)

        # TODO: 界面改进: 只读部分如果为空, 显示'无', 而不是空白
        self.Unicode编码值.set(当前字符[0])
        self.编码86版值.set(当前字符[2])
        self.编码98版值.set(当前字符[3])
        self.编码06版值.set(当前字符[4])
        self.笔顺值.set(当前字符[5])


root = Tk()
app = Application(master=root)
app.mainloop()
