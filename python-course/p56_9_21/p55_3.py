def fun(x):
    if(x>1000 and x<=2000):
        print('打九五折后价格为：',x*0.95)
    elif(x>2000 and x<=3000):
        print('打九折后价格为：',x*0.9)
    elif(x>3000 and x<=5000):
        print('打八五折后价格为：',x*0.85)
    elif(x>5000):
        print('打八折后价格为：',x*0.8)
    else:
        print('没有打折优惠，价格为：',x)

x = float(input())
fun(x)
