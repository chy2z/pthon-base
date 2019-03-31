"""
演示异常使用
"""
index=1

while index:
    index=index-1

try:
    index=1/index
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("except")