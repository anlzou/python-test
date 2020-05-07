def fun(x):
    a = 0
    if x<1:
        print("数应该大于1")
        return
    for j in range(1,x):
        if x%j == 0:
            a += j
    if a == x:
        print(x,"是完数")
    else:
        print(x,"不是完数")
#主函数
i = int(input("输入一个整数："))
fun(i)
