"""
List类型的使用
"""
list1 = ["python", "java", "net"]

list2 = ['Google', 'Runoob', 1997, 2000, 2002]

# 输出索引
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 输出列表第1个元素
print(list1[0])

# 列表区间输出第3个到第5个，不包含第5个
print(list2[2:4])

# 列表区间输出第3个到倒数第一个，不包含倒数第一个
print(list2[2:-1])

# 列表长度
print(len(list2))

# 多个列表组合
list3 = list1 + list2

print(list3)

# 删除列表
del list3[0]
print(list3)

# 删除列表区间
del list3[0:3]
print(list3)

# 列表元素是否在集合中
print("Runoob" in list3)
print("Runoob" in list1)

# 输出列表
index=0
for x in list3:
    index=index+1
    print("元素"+str(index)+":" + str(x))

# 末尾追加元素
list3.append("追加")
print(list3)

# 末尾删除元素
temp=list3.pop()
print(temp)
print(list3)

# 删除指定位置元素
temp=list3.pop(1)
print(temp)
print(list3)

# 清空集合
list3.clear()
print(list3)

list1 = ["python", "java", "net"]

list2 = ['Google', 'Runoob', 1997, 2000, 2002]

# 嵌套列表
list5 = [list1,list2]

print(list5)
print(list5[0])
print(list5[0][1])