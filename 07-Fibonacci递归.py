"""
斐波那契数列
"""
a, b = 0, 1  # a=0,b=1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b  # a=b,b=a+b
