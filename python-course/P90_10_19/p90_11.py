def fun(s):
    char = ""
    a = []
    for ch in s:
        if ('A'<= ch <='Z') or ('a'<= ch <='z'):
            char += str(ch)
        else:
            a.append(char)
            char = ""
    print("单词的个数为：",len(a))
    for j in range(len(a)):
        print(a[j])

#主函数
s = str(input("输入字符串："))
fun(s)
