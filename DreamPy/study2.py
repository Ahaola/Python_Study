'''
集合Set是一个无序且不可重复的序列，使用{}或set()函数进行创建，如果想创建一个空集合必须用 set() ，{ } 是用来创建一个空字典的。
注意：集合（Set）只存储不可变的数据类型，如Number（数字）、字符串、元组等，而无法存储列表、字典、集合这些可变的数据类型。
'''

# set1 = set({1, 2, 3, 4})
# print(set1)

#bool类型是可以相加的，相加之后会转换成int类型
# a = True
# b = False
# print(a+b)

#位置传递
# def user_info(*args):
#     print(args)
#
# user_info("张三",18)
#
# #关键字传递
# def student_info(**kwargs):
#     print(kwargs)
#
# student_info(name="lisi",age=18,sex="女")
#
# #lambda表达式
# def test_user(compute):
#     res = compute(1, 2)
#     print(res)
#
# def compute(x,y):
#     return  x+y
#
# test_user(lambda x,y: x+y)

#文件相关操作
# f = open('D:/test.txt', 'r', encoding='utf8')
# print(type(f))
# print(f"读取十个字节的结果是：{f.read(10)}")
# print(f"读取所有的文本内容是：{f.read()}")
# print(f"读取所有行的内容是{f.readlines()}")
# print(f"读取一行内容的方法是:{f.readline()}")

#for循环读取行
# for line in f:
#     print(f"每一行的内容是：{line}")
#
# #关闭文件
# f.close()

#with open 方法是自带close()方法 有效避免我们打开文件忘记关闭
# with open('D:/test.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line)

#文件的写 w 操作 write方法打开文件，文件若有，则打开，若没有，则创建新的文件
f = open('D:/test.txt', 'w', encoding='utf8')
#write方法只是把内容写到了内存，并没有写到硬盘里面
f.write("啊哈哈哈哈哈哈哈哈")
#调用 flush方法才是将文件内容写入硬盘
f.flush()
#close方法内置了flush方法，调用close方法相当于也调用了flush方法
f.close()