'''
    大数相加
'''

import sys

def Sumab(num1,num2):
    array1 = [int(i) for i in str(num1)]
    array2 = [int(i) for i in str(num2)]

    len1 = len(array1)
    len2 = len(array2)
    if len1 <= len2:#两种情况，第一种：数组1的长度小于数组2的长度，第二种情况反过来。
        minlen = len1#较大和较小的数组长度
        maxlen = len2
        ans = [0 for x in range(maxlen)]#新建立一个与较长数组长度一致的全为0的数组
        ans[-minlen:] = array1#数组的后一部分保存较短数组的值
        #print ans
        for i in range(1,maxlen+1):
            i = -i#从数组尾部开始算
            temp = ans[i] + array2[i]
            if temp >= 10:#如果和大于10，则保留个位数值，并进位
                temp = temp - 10
                ans[i] = temp
                print (ans)
                if i == -maxlen: #数组的第一位，进位后超出数组范围，用python的insert函数，在数组前插入数值
                    ans.insert(0,1)
                else:#如果没有超出数组范围，则直接在新建的数组的前一位加1
                    ans[i-1] = ans[i-1] + 1
            else:
                ans[i] = temp
                #print ans
    else:#第二种情况
        minlen = len2
        maxlen = len1
        ans = [0 for x in range(maxlen)]
        ans[-minlen:] = array2
        for i in range(1,maxlen+1):
            i = -i
            temp = ans[i] + array1[i]
            if temp >= 10:
                temp = temp - 10
                ans[i] = temp
                if i == -maxlen:
                    ans.insert(0,1)
                else:
                    ans[i-1] = ans[i-1] + 1
            else:
                ans[i] = temp
    return ans


print("请输入两个整数：")
num1, num2 = map(int, sys.stdin.readline().split())
print (Sumab(num1,num2))