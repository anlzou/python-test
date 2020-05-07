sum=0
s1=1

for i in range(1,10,2):
    for j in range(1,i+1):
        s1=s1*j
    sum=sum+s1
    s1=1

print("1!+3!+5!+7!+9!=%d"%sum)

