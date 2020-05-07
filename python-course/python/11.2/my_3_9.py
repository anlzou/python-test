for i in range(1,1000):
    k=str(i*i)
    m=int(k[(-len(str(i))):])
    if(m==i):
        print(m,end=" ")
   
