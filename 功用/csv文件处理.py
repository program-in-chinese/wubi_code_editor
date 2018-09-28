import csv


class csv文件处理:

    @staticmethod
    def 读文件到数组(文件名):
        # 官方文档参考: https://docs.python.org/3/library/csv.html#module-contents
        with open(文件名, newline='') as 源数据文件:
            源数据读取器 = csv.reader(源数据文件, delimiter=',')
            所有行 = []
            for 行 in 源数据读取器:
                所有行.append(行)
        return 所有行

    @staticmethod
    def 写数组到文件(数据, 文件名):
        with open(文件名, 'w', newline='') as 目标文件:
            写文件 = csv.writer(目标文件, delimiter=',')
            for 字符 in 数据:
                写文件.writerow(字符)
        print("修改保存到: " + 文件名)