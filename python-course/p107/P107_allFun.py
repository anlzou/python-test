def readFile(file):
    File = open(file)
    lines = File.readlines()
    count = len(lines)
    print("(1)该文本有",count,"行：")

    count = 0
    for line in lines:
        if line[0] == "P":
            count += 1
    print("(2)文件中以大写字母P开头的有",count,"行")
    a = []
    for line in lines:
        a.append(len(line))
    maxchar = a.index(max(a))
    minchar = a.index(min(a))

    print("(3)一行中包含字符最多的和包含字符最少的分别在%d，%d\n"%(maxchar+1,minchar+1))

    for line in lines:
        print(line,end = '')
    File.close()

def writeTest(file):
    File = open(file,"w")
    string = input("输入要保存的文字：")
    File.write(string+'\n')
    File.close()

def writeTestAdd(file):
    File = open(file,"a")
    string = input("输入要追加保存的文字：")
    File.write(string+'\n')
    File.close()

def writeFile(oldfile, newfile):
    old_file = open(oldfile)
    new_file = open(newfile,"a")

    line = old_file.readlines()
    new_file.writelines(line)

    old_file.close()
    new_file.close()


#主程序
#writeTestAdd("C://Users//anlzou//手工//python//test.txt")

#writeFile("C://Users//anlzou//手工//python//test.txt","C://Users//anlzou//手工//python//test1.txt")

readFile("C://Users//anlzou//手工//python//test.txt")
