def max_child(arr):
    max = 0
    x = 0
    y = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(i, n):
            arr_sum = 0
            for k in range(i, j+1):
                arr_sum = arr_sum + arr[k]
            if arr_sum >= max:
                max = arr_sum
                x = i
                y = j

    print("最大数组的起始坐标-结束坐标",x,y)
    return max

arr = [1,2,-3,4,5]
print("最大数组的和：",max_child(arr))
