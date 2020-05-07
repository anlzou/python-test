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

    print("(3)一行中包含字符最多的和包含字符最少的分别在第%d行，第%d行\n"%(maxchar+1,minchar+1))

    for line in lines:
        print(line,end = '')
    File.close()


#主程序
readFile("C://Users//anlzou//手工//python//test.txt")
