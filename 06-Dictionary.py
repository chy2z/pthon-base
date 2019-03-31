"""
字典类型的使用
"""
json = {"name": "chy", "age": 21}

# 赋值
json["age"] = 30

# 输出值
print(json["age"])

# 动态增加属性
json["sex"] = '男'
print(json["sex"])

# 删除属性
del json["sex"]
print("sex" in json)
print("name" in json)

# 循环打印
for x in json:
    print(json[x])

# 循环打印
for key, value in json.items():
    print("key:%s,value:%s" % (key, value))

# 动态删除属性
json["sex"] = '女'
temp = json.pop("sex")
print(temp)

citys = {
    '北京': {
        '朝阳': ['国贸', 'CBD', '天阶', '我爱我家', '链接地产'],
        '海淀': ['圆明园', '苏州街', '中关村', '北京大学']
    },
    '河北': {
        '张家口': ['张家口A', '张家口B', '张家口C'],
        '承德': ['承德A', '承德B', '承德C', '承德D']
    }
}

for i in citys['北京']:
    print(i)
print("----------------")

for i in citys['北京']['海淀']:
    print(i)
print("----------------")

for key in citys.keys():
    print(key)
print("----------------")
