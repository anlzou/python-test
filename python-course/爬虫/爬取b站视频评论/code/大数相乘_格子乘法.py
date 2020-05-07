'''
    内容：大数相乘
    还没有完成

    参考文件：multiply.py、add.py、jian.py
'''


def fun(n,m):
    ans = 0
    len_n = len(str(n))
    len_m = len(str(m))
    list_n = []
    list_m = []

    for i in str(n):
        list_n.append(int(i))
    for i in str(m):
        list_m.append(int(i))

    data = [len_n+1][len_m+1][2]

    for i in range(list_n):
        for j in range(list_m):
            a = list_n[i] *[j]
            data[i][j][0] = a%10
            data[i][j][1] = a//10

    list_n.clear()
    list_m.clear()
    for j in range(list_m,-1):
        for i in range(list_n,-1):
            list_n.append(str(data[j][i])[0])



    return ans

n = int(input("输入n"))
m = int(input("输入m"))

ans = fun(n,m)
#print(ans)