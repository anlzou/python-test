def pingfahe(n):
    s=0
    for i in range(1,n+1):
        s=s+i**2
    return s

#print(pingfahe(14))
for x in range(1,100):
   if pingfahe(x)>=1000:
        print(x-1)
        break
    
