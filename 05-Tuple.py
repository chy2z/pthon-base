"""
元祖类型的使用
元祖元素不允许修改
"""
tuple1 = (1, 2, 3, 4)

print(tuple1)
print(tuple1[1])
print(tuple1[0:])
print(tuple1[1:3])

for x in tuple1:
    print(x)

tuple3 = tuple1 + (5, 6);
print(tuple3)

del tuple3
tuple3 = ()
print(tuple3)




