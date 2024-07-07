import json

'''
学习教程： https://blog.csdn.net/weixin_67276852/article/details/134834500
'''
data = {
    'name': '水滴',
    'age': 20,
    'city': '青岛'
}

# 将数据序列化到文件
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False)

# 将数据序列化为字符串
json_str = json.dumps(data, ensure_ascii=False)
# 打印序列化后的字符串
print(json_str)

# 从文件中反序列化数据
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 打印反序列化后的数据
print(data)

json_str = '{"name": "水滴", "age": 20, "city": "青岛"}'
# 从字符串中反序列化数据
data = json.loads(json_str)
# 打印反序列化后的数据
print(data)
