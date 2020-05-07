import math
#<0
def fun_1():
    print("函数无解")
#=0
def fun_2(a,b):
    x1 = -b/2*a
    print("有一个解：",x1)
#>0
def fun_3(a,b,c):
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a    
    print("有两个解：%d，%d"%(x1,x2))

def fun(a,b,c):
    p = b**2-4*a*c
    if p < 0:
        fun_1()
    elif p == 0:
        fun_2(a,b)
    elif p > 0:
        fun_3(a,b,c)

#主程序
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

fun(a,b,c)
