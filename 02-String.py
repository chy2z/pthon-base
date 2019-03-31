"""
字符串类型的使用
"""
# 字符串组合
first_name = 'chy'
last_name = '2z'
full_name = first_name + "-" + last_name
print(full_name)

# 去空格
name = " chy2z "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# 长度
print(len(name))

charts = "abcdef"
# 输出所有字符
print(charts[0:])
# 输出第1个到倒数第2个的所有字符，不包含倒数第一个
print(charts[0:-1])
# 输出第3个到第4个所有字符，不包含第5个
print(charts[2:4])
# 输出第1个字符
print(charts[0])
# 输出倒数第1个字符
print(charts[-1])
# 输出2遍所有字符
print(charts * 2)

# 类型转字符串
age = 21
print(age)
print(name.title() + " is " + str(age))

# 制表符
print("-------\r-------")
print("-------\t-------")
print("-------\n-------")
