f1=1
f2=2
f3=3

for i in range(4,1000):
    f4=(f1+f2+f3)/2
    if(f4>1200):
        print(i,":",f4)
        break
    f1=f2
    f2=f3
    f3=f4
   


