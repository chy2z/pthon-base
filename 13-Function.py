"""
函数 使用
"""


# 无参数函数
def hello():
    print("hello world!")
    return


hello()

# 函数返回值
def count(a, b):
    c = a + b
    return c

toal = count(10, 10)
print("total=", toal)


# 参数函数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
printinfo(name="runoob")
printinfo("runoob", 40)

# lambda表达式
sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
