"""
for 使用
"""
ranges = range(1, 10)
for x in ranges:
    if x % 2 == 0:
        continue
    else:
        print("数字 %d 是奇数" % (x))

for x in "abc":
    print("字符", x)
