def fun(n):
    for i in range(2,n):      #2到n-1
        if(n%i == 0):
            return 0
    return 1

#主函数
for i in range(100,1000):
    x = fun(i)
    if(x == 1):
        print(i,end = ' ')
