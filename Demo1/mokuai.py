# import os
# import sys
# from datetime import datetime, timedelta
# import random
# import json
# import requests
# import numpy as np
# import matplotlib.pyplot as plt
# import threading
# import math
# import sqlite3
# import unittest
# import itertools
#
#
#
#
# # 查看当前工作目录
# print(os.getcwd())
#
# # 创建新目录
# # os.mkdir('new_folder')
#
# # 列出指定目录下的文件和子目录
# for item in os.listdir('../../'):
#     print(item)
#
# # 输出Python版本信息
# print(sys.version)
#
# # 打印命令行参数
# for arg in sys.argv:
#     print(arg)
#
# # 获取当前日期时间
# now = datetime.now()
# print(now)
#
# # 计算未来日期
# future_date = now + timedelta(days=30)
# print(future_date)
#
# # 生成一个[0, 1)之间的随机浮点数
# rand_float = random.random()
# print(rand_float)
#
# # 随机从列表中选取一个元素
# choices = ['apple', 'banana', 'orange']
# for i in range(len(choices)):
#     random_choice = random.choice(choices)
#     print(random_choice)
#
#
# # 将Python对象转换为JSON字符串
# data = {'name': 'XiaoLang', 'age': 22}
# json_str = json.dumps(data)
# print(json_str)
#
# # 从JSON字符串解析回Python对象
# object_data = json.loads(json_str)
# print(object_data)
#
#
# # 发送GET请求并打印响应内容
# # response = requests.get('https://api.github.com')
# # print(response.text)
#
# # 创建一个2x2的数组
# arr = np.array([[1, 2], [3, 4]])
# print(arr)
#
# # 计算数组元素之和
# sum_arr = np.sum(arr)
# print(sum_arr)
#
# # 绘制简单的折线图
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()
#
# # 定义线程任务
# def thread_task(name):
#     print(f"Thread {name} started.")
#     # ... 执行任务 ...
#     print(f"Thread {name} finished.")
#
# # 创建并启动两个线程
# t1 = threading.Thread(target=thread_task, args=("Thread 1",))
# t2 = threading.Thread(target=thread_task, args=("Thread 2",))
#
# t1.start()
# t2.start()
#
# # 等待所有线程完成
# t1.join()
# t2.join()
#
# print("All threads finished.")
#
# # class TestMathFunctions(unittest.TestCase):
# #
# #     def test_factorial(self):
# #         self.assertEqual(math.factorial(5), 120)
# #
# #     def test_gcd(self):
# #         self.assertEqual(math.gcd(18, 24), 6)
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
#
# # conn = sqlite3.connect('example.db')
# # cursor = conn.cursor()
# #
# # cursor.execute('''CREATE TABLE stocks
# #                  (date text, trans text, symbol text, qty real, price real)''')
# #
# # cursor.execute("INSERT INTO stocks VALUES ('202.jpg', 'BUY', 'RHAT', 100, 35.14)")
# #
# # conn.commit()
# # conn.close()
#
# combinations = itertools.combinations(range(4), 2)
# for combo in combinations:
#     print(combo)
#
#


import json

# 从文件中读取JSON数据并将其转换为Python对象
# with open("data.json", "r") as file:
#     data = json.load(file)
#     print(data)

# Python对象
data = {"name": "Alice", "age": 30}

# 将Python对象写入文件中以JSON格式
with open("data.json", "w") as file:
    json.dump(data, file)






















