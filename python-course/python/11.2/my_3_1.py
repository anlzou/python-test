n=int(input("请输入一个整数："))

if(n%5==0 and n%7==0):
    print("%d能同时被5和7整除"%n)
else:
    print("%d不能同时被5和7整除"%n)
