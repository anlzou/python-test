def fun(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            print("不是回文数")
            return
    print("是回文数")
    
#主函数
s = str(input("输入字符串："))
while len(s) <= 2:
    print("字符数至少为3个，重新输入")
    s = str(input("输入字符串："))
fun(s)
