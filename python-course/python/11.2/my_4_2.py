import math

def su(num):
    j=2
    while j<=math.sqrt(num):
        if num%j==0:break
        j=j+1
    if j>math.sqrt(num):
        return num
    
print("三位数的素数有：")
for i in range(100,1000):    
    if su(i):
        print(su(i),end=" ")
