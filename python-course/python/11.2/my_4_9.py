def change(n):
    la=[]
    while True:
        n,rem=divmod(n,2)
        la.append(str(rem))
        if n==0:
            return ''.join(la[::-1])

num=int(input("请输入一个十进制的整数："))
print(change(num))
