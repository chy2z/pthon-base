"""
while 使用
"""
n, counter = 1, 100
while n < 5:
    counter = counter + n
    print("counter=%d" %(counter) )
    n = n + 1

var = 1
while var:
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)
    if num < 1:
        break

print("输入结束!")