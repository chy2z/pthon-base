"""
演示面向对象
"""

#类定义
class Person:
    # 定义基本属性
    name = 'lord'
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self,_age,_weight):
        self.age = _age
        self.__weight=_weight

    # 定义方法
    def getName(self):
        return self.name;

    # 定义方法
    def setName(self, _name):
        self.name = _name

    # 定义方法
    def toString(self):
        print("name=%s,age=%s,weight=%s" %(self.name,self.age,self.__weight))

# 实例化类
p = Person(21,120)
print(p.name)
print(p.age)
p.toString()

# 继承
class Student(Person):
    grade=''

    def __init__(self,_age,_weight,_grade):
        # 调用父类的构函
        Person.__init__(self,_age,_weight)
        self.grade=_grade

    # 覆写父类的方法
    def toString(self):
        print("name=%s,age=%s,grade=%s" %(self.name,self.age,self.grade))

    # 私有方法
    def __getGrade(self):
        print('这是私有方法')

s=Student(25,140,2)
print(s.name)
print(s.grade)
s.toString()