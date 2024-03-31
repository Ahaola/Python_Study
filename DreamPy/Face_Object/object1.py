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

'''
在python里面  __new__方法里面  x = object.__new__(cls) 就是申请内存空间的 
'''

'''继承'''
class Animals(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,name):
        print(f'{self.name}在吃东西')

    def __siyou(self):
        print("私有方法不能被继承")
class Dog(Animals):
    def eat(self,name):
        print(f"{self.name}吃骨头")

d1 = Dog("dahuang",2)
d1.eat("xiaohei")
# d1.__siyou()


'''继承特点：想果一个类A继承自类B，由类A创建出来的实例对全部能直接使用类B里定义的方法

1.子类的实现和父类的实现完全不一样，子类可以选择重写父类的方法。

2.子类科父类的基础上又有更多的实现 可以选择重写'''


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '入睡')


class Student1(Person):

    # 重写方法
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 子类在父类实现的基础上，又添加了自己的新的功能
        # 调用父类方法的两种方式

        # 1.父类名.方法名（self,参数列表）
        # Person.__init__(self,name,age)

        # 2.使用super直接调用父类方法(建议使用这个)
        super(Student1, self).__init__(name, age)
        self.school = school

    # 重写方法
    def sleep(self):
        print(self.name + '正在床上呼呼大睡')

    def study(self):
        print(self.name + '正在学习')


s = Student('jerry', 20, '幼稚园')
# s.sleep()

# 然后介绍一个方法 __mro__ 就是可以看 使用函数对象的时候 他会找谁
# print(Student.__mro__)
# (<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
#  意思就是先找自己 然后找Person 然后找 object