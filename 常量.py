from collections import OrderedDict

源数据路径 = "UnicodeCJK-Wubi/"
源数据文件 = ["CJK-A.txt", "CJK-B.txt", "CJK-C.txt",
         "CJK-D.txt", "CJK-E.txt", "CJK-F.txt", "CJK.txt"]
# 暂时只指出导出到一个文件
修改后文件 = "CJK-所有.txt"

# TODO: 支持windows路径
图片主目录 = "UnicodeCJK-FontGlyphs/"
字体名_中易宋体 = "中易宋体"
字体名_中华书局宋体 = "中华书局宋体"
字体名_汉仪字典宋 = "汉仪字典宋"
字体名_汉仪仿宋 = "汉仪仿宋"
字体名_方正楷体S = "方正楷体S"

字体名_细明体 = "细明体"
字体名_细明体_HKSCS = "细明体_HKSCS"
字体名_方正楷体T = "方正楷体T"

字体名_花园明朝 = "花园明朝"

图片路径 = {
    字体名_中易宋体: "SimSun/",
    字体名_中华书局宋体: "ZhongHuaSong/",
    字体名_汉仪字典宋: "HYZiDianSong/",
    字体名_汉仪仿宋: "HYFangSong/",
    字体名_方正楷体S: "FZKaiS/",
    字体名_细明体: "MingLiU/",
    字体名_细明体_HKSCS: "MingLiU_HKSCS/",
    字体名_方正楷体T: "FZKaiT/",
    字体名_花园明朝: "HanaMin/",
}

无字体图片 = "images/NoneFontGlyph.gif"

按地区名取字体列表 = OrderedDict([
    ("中国大陆", [字体名_中易宋体, 字体名_中华书局宋体, 字体名_汉仪字典宋, 字体名_汉仪仿宋, 字体名_方正楷体S]),
    ("中国台港澳", [字体名_细明体, 字体名_细明体_HKSCS, 字体名_方正楷体T]),
    ("日本", [字体名_花园明朝])])

# TODO: 判断tkinter版本, 如<8.6则用.gif
图片扩展名 = ".png"

无 = "无"
