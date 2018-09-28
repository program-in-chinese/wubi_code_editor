
源数据路径 = "UnicodeCJK-Wubi/"
源数据文件 = ["CJK-A.txt", "CJK-B.txt", "CJK-C.txt", "CJK-D.txt", "CJK-E.txt", "CJK-F.txt", "CJK.txt"]
# 暂时只指出导出到一个文件
修改后文件 = "CJK-所有.txt"

# TODO: 支持windows路径
图片主目录 = "UnicodeCJK-FontGlyphs/"
图片路径 = {
  "中易宋体": "SimSun/",
  "中华书局宋体": "ZhongHuaSong/",
  "汉仪字典宋": "HYZiDianSong/",
  "汉仪仿宋": "HYFangSong/",
  "方正楷体S": "FZKaiS/",
  "细明体": "MingLiU/",
  "细明体_HKSCS": "MingLiU_HKSCS/",
  "方正楷体T": "FZKaiT/",
  "花园明朝": "HanaMin/",
}

大陆字体列表 = ["中易宋体", "中华书局宋体", "汉仪字典宋", "汉仪仿宋", "方正楷体S"]
台港澳字体列表 = ["细明体", "细明体_HKSCS", "方正楷体T"]
日本字体列表 = ["花园明朝"]
按地区名取字体列表 = {"中国大陆": 大陆字体列表, "中国台港澳": 台港澳字体列表, "日本": 日本字体列表}

图片扩展名 = ".png"

无 = "无"