def multi(x):
    z = 1
    for i in x:
        z *= i
    return z

#主程序
y = []                  #列表
x = int(input())
y.append(x)

while 1:
    x = int(input())
    if x == 0:
        break
    y.append(x)
    
a = multi(y)
print(a)
