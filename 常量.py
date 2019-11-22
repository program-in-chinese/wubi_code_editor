import tkinter
from collections import OrderedDict

源数据路径 = "UnicodeCJK-WuBi/"

# https://github.com/CNMan/UnicodeCJK-WuBi/pull/2#issuecomment-424330083
# 4E00..9FFF	CJK
# 3400..4DBF	CJK-A
# 20000..2A6DF	CJK-B
# 2A700..2B73F	CJK-C
# 2B740..2B81F	CJK-D
# 2B820..2CEAF	CJK-E
# 2CEB0..2EBEF	CJK-F
# 按码大小范围排序
源数据文件 = ["CJK-A.txt", "CJK.txt", "CJKCompatibilityIdeographs.txt", "CJK-B.txt", "CJK-C.txt",
         "CJK-D.txt", "CJK-E.txt", "CJK-F.txt", "CJKCompatibilityIdeographsSupplement.txt", "CJK-G.txt"]
# 暂时只指出导出到一个文件
修改后文件 = "CJK-所有.txt"

# TODO: 支持windows路径
图片主目录 = "UnicodeCJK-FontGlyphs/"
字体名_中易宋体 = "中易宋体"
字体名_中华书局宋体 = "中华书局宋体"
字体名_汉仪字典宋 = "汉仪字典宋"
字体名_汉仪仿宋 = "汉仪仿宋"
字体名_方正宋体S = "方正宋体S"
字体名_方正楷体S = "方正楷体S"
字体名_方正新楷体S = "方正新楷体S"
字体名_BabelStoneHan = "BabelStoneHan"

字体名_細明體 = "細明體"
字体名_細明體_HKSCS = "細明體_HKSCS"
字体名_方正楷体T = "方正楷体T"
字体名_全字庫正宋體 = "全字庫正宋體"
字体名_全字庫正楷體 = "全字庫正楷體"

字体名_花園明朝 = "花園明朝"

图片路径 = {
    字体名_中易宋体: "SimSun/",
    字体名_中华书局宋体: "ZhongHuaSong/",
    字体名_汉仪字典宋: "HYZiDianSong/",
    字体名_汉仪仿宋: "HYFangSong/",
    字体名_方正宋体S: "FZSongS/",
    字体名_方正楷体S: "FZKaiS/",
    字体名_方正新楷体S: "FZNewKaiS/",
    字体名_BabelStoneHan: "BabelStoneHan/",
    字体名_細明體: "MingLiU/",
    字体名_細明體_HKSCS: "MingLiU_HKSCS/",
    字体名_方正楷体T: "FZKaiT/",
    字体名_全字庫正宋體: "TW-Sung/",
    字体名_全字庫正楷體: "TW-Kai/",
    字体名_花園明朝: "HanaMin/"
}

无字体图片 = "images/NoneFontGlyph.gif"

按地区名取字体列表 = OrderedDict([
    ("中国大陆", [字体名_中易宋体, 字体名_中华书局宋体, 字体名_汉仪字典宋, 字体名_汉仪仿宋, 字体名_方正宋体S, 字体名_方正楷体S, 字体名_方正新楷体S, 字体名_BabelStoneHan]),
    ("中国台港澳", [字体名_細明體, 字体名_細明體_HKSCS, 字体名_方正楷体T, 字体名_全字庫正宋體, 字体名_全字庫正楷體]),
    ("日本", [字体名_花園明朝])])

# https://stackoverflow.com/questions/27599311/tkinter-photoimage-doesnt-not-support-png-image/34995365#34995365
图片扩展名 = ".gif" if tkinter.TkVersion < 8.6 else ".png"

无 = "无"

IRG数据路径 = "Unicode/Unihan/Unihan_IRGSources.txt"
IRG键值 = ["G", "H", "J", "KP", "K", "M", "S", "T", "UK", "U", "V"]
IRG值前缀 = "kIRG_"
IRG值后缀 = "Source"