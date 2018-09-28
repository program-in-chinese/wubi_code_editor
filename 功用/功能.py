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
    # TODO: 简化代码
    @staticmethod
    def 组成图片子路径(Unicode码):
        Plane值 = "00"
        if (len(Unicode码) == 5):
            Plane值 = "0" + Unicode码[0]
        elif (len(Unicode码) == 6):
            前两位 = Unicode码[0:1]
            if 前两位 == '0E':
                Plane值 = "14"
            elif 前两位 == '0F':
                Plane值 = "15"
            elif 前两位 == '10':
                Plane值 = "16"
        补0数 = 6 - len(Unicode码)
        大写Unicode码 = "0" * 补0数 + Unicode码.upper()
        return "Plane" + Plane值 + "/U_" + 大写Unicode码
