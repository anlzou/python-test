def fun(x,n):
    for i in range(n+1):
        print((x*i).center(n*4))

#主程序
x = input("输入打印字符：")
x = x+"   "
n = int(input("输入打印行数："))

fun(x,n)
