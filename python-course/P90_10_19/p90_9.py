def fun(x):
    a = []
    a.append(x%2)
    x = x//2
    while(x >= 1):
        a.append(x%2)
        x = x//2
    for i in range(len(a)-1,-1,-1):
        print(a[i],end = "")

#主函数
x = int(input("输入一个数："))
fun(x)
