"""
数据结构使用
"""
# 列表使用
a = [66.25, 333, 333, 1, 1234.5]
# 统计出现的次数
print(a.count(333), a.count(66.25), a.count('x'))

# 在索引2位置插入元素
a.insert(2, -1)
# 在末尾插入元素
a.append(333)
print(a)

# 元素第一次出现所在的位置
index = a.index(333)
print("333第一次出现所在的位置:", index)

# 删除列表中值为 333 的第一个元素
a.remove(333)
print(a)

# 倒排元素位置
a.reverse()
print(a)

# 排序
# 从小到大
a.sort()
print(a)
# 从大到小
a.sort(reverse=True)
print(a)

# 浅复制
c=a.copy()
c.append(999)
print(c)

# 数据结构 堆栈
# 尾巴进
c.append(0)
# 尾巴出
c.pop()

# 模拟队列
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()
print(queue)
