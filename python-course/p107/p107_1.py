def getFilePath():
    path = str(input("filepath："))
    path.replace('\\','*')
    if path.find('*') > -1:
        path.replace('*',"\\\\")
    return path
                     
def countString(string):
    path = getFilePath()
    file = open(path,"r")
    readfile = file.read()
    count = readfile.count(string)
    print("\"%s\"出现了%d次"%(string,int(count)))

#主程序
string = str(input("输入关键字："))
countString(string)
