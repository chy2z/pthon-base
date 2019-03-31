"""
iter 和 yield 使用
"""
list1 = ("1", "2", "3", "4")

# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
it = iter(list1)
print(next(it))
print(next(it))
for x in it:
    print(x, end=" ")
print("访问完结束")

# 生成器函数
def f(n):
    while n > 0:
        # yield函数会暂停并保存当前所有的运行信息
        yield n
        n = n - 2

y = f(10) # f 是一个迭代器，由生成器返回生成

for x in y:
    print(x, end=" ")