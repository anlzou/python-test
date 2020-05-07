#列表
list1 = ['中国','美国',1997,2000]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]

print("1：",list1)
print("2：",list2[0])
print("3：",list3[0:3])

#更新
list1[1] = '日本'
print("1：",list1)

list2.append('加拿大')
print("2：",list2)

#删除
del(list1[1])
print("1：",list1)
list2.remove('加拿大')
print("2：",list2)

