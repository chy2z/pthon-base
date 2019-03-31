'''
演示数据库访问

安装：
1 进入Python安装目录：D:\Program Files\Python\Scripts

2 pip install PyMySQL

'''

import pymysql

# 创建连接
db = pymysql.connect("localhost", "root", "wmzycn", "eakay")
# 创建游标对象
cursor = db.cursor()
# 执行SQL语句
cursor.execute("SELECT VERSION()")
# 获取返回数据
data = cursor.fetchone()
# 打印数据
print("Database version : %s " % data)
# 关闭连接
db.close();
