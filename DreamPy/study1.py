# print(1+2-3)
# str1 = "hello world"
# print(str1[-1:-4:-2])
# avg = (34+23+345+12.7) / 4
# print(avg)
# sum = avg + 45
# print(sum)
# total = (120-avg)**2 + (135-avg)**2
# print(total)
# a:int = 0.5
# print(type(a))
# s1 = '''my 'name' is "yuanhao"'''
# print(s1)
# print(len(s1))
# #类型声明
# s2:str = 'hello'
# s3:str = 'world'
# print(s2+s3)

'''
这是一个文档字符串，也是一个注释
'''
from datetime import datetime
import random1

# print(10/0)
# print(-7 // 2)
# a=10
# b=15
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)

#浮点数比较
# a = 0.1+0.2
# b = 0.3
# print(-0.00001 < (a-b) < 0.000001)
#
# #多元赋值
# c,d = 10,20
# print(c,d)

# c += 1
#python不支持自增++，自减--这样的运算符的
# ++c
# c--
# print(c)
#
# c -= 1
# print(c)
#
# e = True
# f = False

#选择语句，注意缩进和elif合体了
# if a:
#     a += 1
# elif b:
#     b += 1
# else:
#     c += 2

#input读取的是一个字符串
#可以进行强制类型转换：a = int(a)
# shuru = int(input("输入1表示正确，输入2表示错误，输入其他表示非法！"))
# if shuru == 1:
#     print("正确")
# elif shuru == 2:
#     print("错误")
# else:
#     print("输入非法，请重新输入！")

# year = int(input("请输入一个年份"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("闰年")
# else:
#     print("平年")

#空语句占位，啥也不做
# dudu = int(input("这是一个空语句占位操作"))
# if dudu == 1:
#     #空语句表示啥也不做
#     pass
# else:
#     print("输入的不是1")

# num,sum = 1,0
# while num <= 10:
#     print(num)
#     num += 1
#     sum += num
# print(sum)

#左闭右开 范围
# for i in range(1,11):
#     print(i)
# #range最后一个参数表示“步长”，这里表示隔两个数字打印一次
# for i in range(2,12,2):
#     print(i)
#
# #求1到100的和
# result = 0
# for i in range(1,101):
#     result  += i
# print(f"sum = {result}")

#求1！+……+ 5！
# temp = 1
# i = 1
# sum = 0
# while temp <= 5:
#     i *= temp
#     temp += 1
#     sum += i
# print(f"sum = {sum}")

#左右都是闭区间
# point = random.randint(1,10)
# print(point)

#定义一个求和函数,求beg到end之间的和
# def sum(beg,end):
#     res = 0
#     while beg <= end:
#         res += beg
#         beg += 1
#     print(res)
# sum(1,11)

# def jiou(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False
# print(jiou(3))

#一次性返回多个值
# def getpoint():
#     x = 1
#     y = 2
#     return x,y
# a,b = getpoint()
# #还可以只要其中的额一部分值
# _,b = getpoint()

#局部变量，全局变量
# x = 10
# def test():
# #使用global关键是声明x是一个全局变量
#     global x
#     x = 21

#形参的默认值
# def demo1(x,y,debug = False):
#     if debug:
#         return x,y
#     return x+y
# print(demo1(1,2))

#位置参数
# def demo1(x,y):
#     if debug:
#         return x,y
#     return x+y
# print(demo1(y=1,x=2))

#创建列表
# a = [1,2,3,4]
# # print(type(a))
# print(a)
# a1 = [1,"hello",True,233]
# print(a1)
#
# #列表名[]进行下标访问,下标从0开始
# print(a1[2])
# a1[2] = False
# print(a1[2])
#
# #用len获取列表的长度
# print(len(a1))
# #下标可以为负数,从右往左遍历
# print(a1[-1])
#
# #切片操作,打印对应区间的内容，左闭右开
# print(a1[1:3])
# #还可以省略边界,表示从1开始一直到末尾的所有元素
# print(a1[1:])
# print(a1[:3])
# print(a1[:])
# #还可以进行带有步长的切片
# print(a1[::2])
# print(a1[::-2])
# #当切片给的步长超过列表的长度时，不会报错，而是会尽可能打印出所有的元素
# print(a1[0:100])

#第二种方式
# b = list()
# print(type(b))

#几种遍历列表的方式
#type1
# a2 = [1,2,3,4]
# for elem in a2:
#     elem = elem + 1
#     print(elem)
#type2
# a2 = [1,2,3,4]
# for i in range(0,len(a2)):
#     a2[i] = a2[i] + 2
#     print(a2[i])

#使用append往列表中新增一个元素
# a3 = [1,2,3,4]
# a3.append("hello")
# print(a3)
#使用insert在指定位置进行插入
# a3.insert(1,"xiaoalng")
# print(a3)
#使用in来判断某个元素是否在列表中存在
# print(1 in a3)
# print(10 in a3)
#使用index判断某个元素是否在列表中
# print(a3.index(1))
# print(a3.index(10))
#使用pop删除列表中末尾的元素
# a3 = [1,2,3,4]
# a3.pop()
# print(a3)
# a3.pop(1)
# print(a3)
# #使用remove按照值进行删除
# a3.remove(3)
# print(a3)

#字符串拼接
#1.使用+进行拼接
# a = [1, 2, 3, 4]
# b = [5,6,7,8]
# print(a+b)
# #2.使用extend进行拼接
# c = a.extend(b)
# print(a)
# print(b)
# print(c)
# #使用 += 的方式进行拼接
# a += b
# print(a)

#元组操作
# a = (1,2,3,4)
# print(type(a))
# print(a)
# print(a[1])
# print(a[-1])
# print(a[1:3])

#字典创建,两种方式：key-value的格式,每个键值对用逗号隔开，最后一个键值对不用写逗号
# dic1 = {"id": 1,
#         "name": "XiaoLang"
#         }
# dic2 = dict()
# #in 只是判定key是否存在，与value无关
# print("id" in dic1)
# print("id" not in dic1)
# #根据key获取value
# print(dic1["id"])
# #插入，修改
# dic1['score'] = 90
# print(dic1)
# dic1['score'] = 60
# print(dic1)
# #使用pop来删除键值对
# dic1.pop("score")
# print(dic1)
# #遍历操作
# for key in dic1:
#         print(key, dic1[key])
#
# for key, value in dic1.items():
#         print(key, value)
#
# #获取所有的key，所有的value，所有的键值对items
# print(dic1.keys())
# print(dic1.values())
# print(dic1.items())

#不可变的对象一般是可hash的，可变的对象一般是不可hash的
# print(hash(1))
# print(hash((1, 2, 3)))
#
# print(hash([1, 2, 3]))
# print(hash({1, 2, 3}))

#open打开文件操作,逗号后面的r表示读文件，w表示写
# open的返回值是一个文件对象
# f = open('D:/测试开发工程师！！/test.txt', 'r')
# print(f)
# print(type(f))
# f.close()

# flist = []
# count = 0
# while True:
#     f = open('D:/测试开发工程师！！/test.txt', 'r')
#     flist.append(f)
#     f.close()
#     count += 1
#     print(f'打开的文件个数为{count}个')

#使用write进行写文件，使用w方式打开会清空文件中的所有内容
# f = open('D:/测试开发工程师！！/test.txt', 'w')
# f.write("hello\n")
# f.close()

#使用追加的方式进行写文件,这个时候使用a方式打开
# f = open('D:/测试开发工程师！！/test.txt', 'a')
# f.write("world")
# f.close()
#如果文件已经关闭，那么意味着系统中和该文件相关的资源已经释放，这个时候强行去写就会报异常
# f = open('D:/测试开发工程师！！/test.txt', 'a')
# f.close()
# f.write("world")

#使用read指定读取几个字符
# f = open('D:/测试开发工程师！！/test.txt', 'r', encoding="utf8")
# res = f.read(2)
# print(res)
# f.close()

#文件按行读取,使用for循环的方法
# f = open('D:/测试开发工程师！！/test.txt', 'r', encoding="utf8")
# for line in f:
#     #end参数表示每次打印要在末尾加上啥，空字符串表示什么也不加
#     print(f'line={line}', end='')
# f.close()

#使用readlines方法直接将每一行读取出来，放到一个列表里面
# f = open('D:/测试开发工程师！！/test.txt', 'r', encoding="utf8")
# lines = f.readlines()
# print(lines)
# f.close()

#时间转换器
# date1 = datetime(year=2002, month=7, day=19)
# date2 = datetime(year=2023, month=7, day=18)
# print(date2-date1)

'''类和对象'''
# class Student:
#     name = None
#     age = None
#     sex = None
#     def __int__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print("Student类创建了一个对象！")
# stu = Student("zhansgan",19,"男")
#
#
# '''封装'''
# class fengzhuang:
#     name = None
#     tel = None
#     __haha_didi = None #私有成员变量 __ 开头
#     def __test1(self,name,tel,__haha_didi):
#         '''私有成员变量无法被对象访问，但是可以被其他私有成员访问'''
#         if self.__haha_didi > 10:
#             print("私有成员变量被访问到了！")
#
# '''继承'''
# class demo1:
#     id = None
#     def test1(self):
#         print("这是demo1类的方法")
#
# class demo2(demo1):
#     watch = None
#     id = "1"
#     def test2(self,watch,id):
#         print("重新命名id")
#     '''在子类中调用父类的/变量方法'''
#     demo1.test1()
#     super().test1()


# for i in range(5):
#     print(i, end='')

list1 = [1, 'hello', 'world']
list2 = [2, 'dodo', 'haha']

list2.extend(list1)
print(list2)


'''
系统内置的异常：
ZeroDivisionError : 除以0的异常 1/0
FileNotFoundError : 文件不存在异常
FileExistsError : 多次创建同名的文件夹 文件重复报错
ValueError : 数据值不对 转换不了值 比如 int('a')
KeyError : 就是字典里面 键值不存在 或者输入错误
SyntaxError : 报语法错误 比如 用了中文的括号或者逗号啥的
IndexError : 脚标的错误，就是列表只有2个然后写 list1[5]
'''

#自定义异常
class LengthException(Exception):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "长度限制在{}到{}之间是合法的密码".format(self.a,self.b)

password = input('请输入密码')
a = 8
b = 15
if a <= len(password) <= b:
    print("密码合法可以正常登录")
else:
    raise LengthException(a,b)
