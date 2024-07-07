import random

random_float = random.random()
print("随机浮点数:", random_float)

random_int = random.randint(1, 10)
print("随机整数:", random_int)

my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("随机选择的元素:", random_element)

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("随机打乱后的序列:", my_list)

# 设置随机数种子为固定值（例如42）
random.seed(42)
# 生成随机数
random_number = random.random()
print("随机浮点数:", random_number)

random_number = random.random()
print("随机浮点数:", random_number)