class 功能:
    # Unicode编码->Plane号
    # 00xxxx 	Plane00
    # 01xxxx 	Plane01
    # 02xxxx 	Plane02
    # 03xxxx 	Plane03
    # 0Exxxx 	Plane14
    # 0Fxxxx 	Plane15
    # 10xxxx 	Plane16
    # 文件名格式统一为 U_xxxxxx.png （ xxxxxx 为 6 位 Unicode 编码，不足 6 位则前面补 0 ）
    # 输入值为全大写, 无前置0, 输出也为全大写
    @staticmethod
    def 组成图片子路径(Unicode码):
        Plane值 = "00"
        if (len(Unicode码) == 5):
            前一位 = Unicode码[0]
            if 前一位 == '1' or 前一位 == '2' or 前一位 == '3':
                Plane值 = "0" + 前一位
            elif 前一位 == 'E':
                Plane值 = "14"
            elif 前一位 == 'F':
                Plane值 = "15"
        elif (len(Unicode码) == 6):
            if Unicode码[0:2] == '10':
                Plane值 = "16"
        补0数 = 6 - len(Unicode码)
        大写Unicode码 = "0" * 补0数 + Unicode码.upper()
        return "Plane" + Plane值 + "/U_" + 大写Unicode码

    # U+3400	kIRG_GSource	GKX-0078.01
    # U+3400	kIRG_JSource	JA-2121
    # U+3400	kIRG_TSource	T6-222C
    # U+3400	kRSUnicode	1.4
    # 转换为
    # "U+3400"->["kIRG_GSource", "kIRG_JSource", "kIRG_TSource", "kRSUnicode"]
    @staticmethod
    def 数组前两列转换为表(数组):
        表 = {}
        for 行 in 数组:
            if len(行) == 0:
                break
            if 行[0] not in 表:
                表[行[0]] = [行[1]]
            else:
                表[行[0]].append(行[1])
        return 表
