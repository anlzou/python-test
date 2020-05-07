import jieba

def jieBaFile():
    textline = readLineFromFile()
    for readlines in textline:
        seg_list = jieba.cut(readlines, cut_all=True)
        print("Full Mode: " + "/ ".join(seg_list))  # 全模式

        seg_list = jieba.cut(readlines, cut_all=False)
        print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

        seg_list = jieba.cut(readlines)  # 默认是精确模式
        print(", ".join(seg_list))

        seg_list = jieba.cut_for_search(readlines)  # 搜索引擎模式
        print(", ".join(seg_list))

def getFilePath():
    path = str(input("(txt)的文件路径："))
    path.replace('\\','*')
    if path.find('*') > -1:
        path.replace('*',"\\\\")
    return path

def readLineFromFile():
    path = getFilePath()
    file = open(path,encoding='gb18030')
    readfiles = file.readlines()
    file.close()
    return readfiles

jieBaFile()
