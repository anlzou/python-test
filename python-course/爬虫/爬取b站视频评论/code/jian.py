'''
    大数相减
'''

def solution(line):
    a,b = line.strip().split()
    a = [int(item) for item in a]
    b = [int(item) for item in b]
    res = ''
    for i in range(len(b)):
        flag_a = len(a)-1-i
        flag_b = len(b)-1-i
        if a[flag_a]>= b[flag_b]:
            res = str(a[flag_a]-b[flag_b])+res
        else:
            res = str(10+a[flag_a]-b[flag_b])+res
            while a[flag_a-1]==0:
                a[flag_a-1]=9
                flag_a -= 1
            a[flag_a-1] -= 1
    for j in range(len(a)-1-i-1,-1,-1):
        res = str(a[j])+res
    zero_flag=0
    for i in range(len(res)):
        if res[i]!='0':
            zero_flag=1
            break
    if zero_flag==0:
        return 0
    return res[i:]


line = input("输入一行数据(两个数值之间用空格分隔)：")
print (solution(line))