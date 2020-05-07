x1,x2,x3 = 1,2,3
i = 3

x = (x1+x2+x3)/2

while(x<1200):
    x1,x2,x3 = x2,x3,x
    x = (x1+x2+x3)/2
    i+=1
    
print(i)
