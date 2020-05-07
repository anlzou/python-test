def shu(n):
    list1=[]
    for i in range(1,n):
        if n%i==0:
            list1.append(i)
    if n==sum(list1):
        print("%d是完数"%n)
    else:
        print("%d不是完数"%n)

shu(6)
        
