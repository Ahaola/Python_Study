'''
面向对象练习1
'''
class Student(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def me(self):
        print("我是{}".format(self.name))

    def eat(self):
        print(f"我的年龄是{self.age}")

s1 = Student("zhangsan",18,"男")
s1.me()
s1.eat()

#静态方法的使用特点
class Demo(object):
    @staticmethod
    def eat(name):
        print(f"{name}在吃饭")

print(Demo.eat("lisi"))


# 定义一个类属性，记录通过这个类创建了多少个对象

class Person(object):
    count = 0

    def __init__(self, name, age):
        Person.count += 1
        self.name = name
        self.age = age


# 因为每创建一个实例对象 就会自动调用 __new__ 和 __init__方法 所以可以用这个来统计

# 调用__new__方法，用来申请内存
# 如果不重写 __new__ 方法 它会自动找object的 __new__
# object的 __new__方法 默认是创建一个对象申请一段内存

p1 = Person('z', 20)
p2 = Person('b', 20)
p3 = Person('r', 20)

print(Person.count)

"""
在python里面  __new__方法里面  x = object.__new__(cls) 就是申请内存空间的 
"""