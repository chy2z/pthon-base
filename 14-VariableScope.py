"""
变量作用域
"""

'''
Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
'''
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


g = 5  # 全局作用域
if g > 2:
    g = 10
    print("g=", g)
print("g=", g)


def f(n):
    g = n  # 局部作用域
    return


def gf(n):
    global g  # 使用全局
    g = n
    return


f(5)
print("f(n)=", g)
gf(5)
print("gf(n)=", g)


# 全局变量在函数内部可以使用
# 在函数内部声明相同名字的变量是局部变量
def ss(a):
    print(str(g))
    c = a + g
    print(c)


ss(10)


# 闭包
def outer():
    g = 50
    f = 50

    def inner():
        nonlocal g  # nonlocal关键字声明 闭包函数外的函数中
        g = 100
        f = 100
        print("inner-g=", g)
        print("inner-f=", f)

    inner()
    print("outer-g=", g)
    print("outer-f=", f)


outer()
