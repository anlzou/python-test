'''
    大数相乘
'''


import sys

def multiplication(num1, num2):
    num_list1 = [int(i) for i in str(num1)]
    num_list2 = [int(i) for i in str(num2)]

    int_martix = [[i * j for i in num_list1] for j in num_list2]
    # pprint.pprint(int_martix)
    result_martix = convert(int_martix)
    # pprint.pprint(result_martix)
    x_len = len(result_martix) - 1
    y_len = len(result_martix[0]) - 1
    x = x_len
    y = y_len
    # print x,y
    result = str(result_martix[x][y])
    # print result
    while (x != 0 and y != 0):
        jinwei_past = 0
        for i in range(y):
            m = x
            n = y
            n = n - i - 1
            # print result_martix[m][n]
            temp = 0
            while (m >= 0 and n <= y_len):
                temp = temp + result_martix[m][n]
                m = m - 1
                n = n + 1
            # print temp
            jinwei_now = temp / 10
            num = int(temp % 10 + jinwei_past)
            if num >= 10:
                jinwei_now = jinwei_now + 1
            result = str(num % 10) + result
            jinwei_past = jinwei_now
            # print result
        y = 0
        for i in range(x + 1):
            m = x
            n = 0
            m = m - 1 - i
            temp = 0
            while (m >= 0 and n <= y_len):
                temp = temp + result_martix[m][n]
                m = m - 1
                n = n + 1
            jinwei_now = temp / 10
            num = int(temp % 10 + jinwei_past)
            if num >= 10:
                jinwei_now = jinwei_now + 1
            result = str(num % 10) + result
            jinwei_past = jinwei_now
        x = 0

    for i in range(len(result)):
        if result[i] != '0':
            result = result[i:]
            print(result)
            print(len(str(result)))
            break


def convert(martix):
    return_martix = [[(j[i] % 10 + j[i + 1] / 10) for i in range(0, len(j) - 1)] for j in martix]
    i = 0
    for j in martix:
        # print i,j
        return_martix[i].insert(0, j[0] / 10)
        return_martix[i].append(j[len(j) - 1] % 10)
        i = i + 1
        if i == len(martix):
            break
    return return_martix


def main():
    print("请输入两个整数：")
    num1, num2 = map(int, sys.stdin.readline().split())
    multiplication(num1, num2)


main()

