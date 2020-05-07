sum = 0
k = 1
for i in range(1,10,2):
    for j in range(1,i+1):
       k*=j
    sum+=k       
print(sum)
