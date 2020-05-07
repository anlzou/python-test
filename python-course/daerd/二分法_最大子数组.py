def max_child(arr, low, height):
    if low == height:               #如果只有一个元素
        return arr[low]             #返回该元素
    mid = (height+low)//2           #求数组的中点取下限
    m1 = max_child(arr, low, mid)       #求数组左边
    m2 = max_child(arr, mid+1, height)  #求数组右边

    now_left = arr[mid]
    left = arr[mid]
    for i in range(mid-1, low -1, -1):
        now_left = now_left + arr[i]
        if now_left > left:
            left = now_left

    now_right = arr[mid+1]
    right = arr[mid+1]
    for j in range(mid+2, height+1):
        now_right = now_right + arr[j]
        if now_right > right:
            right = now_right

    m3 = left + right
    result = max(m1, m2, m3)
    return result

arr = [-1,20,-3,4,5]
print(max_child(arr, 0, len(arr)-1))
