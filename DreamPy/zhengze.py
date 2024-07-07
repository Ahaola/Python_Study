import re
'''
学习地址：https://blog.csdn.net/weixin_67276852/article/details/131997392
'''

string = "The quick brown fox jumps over the lazy dog."
match = re.search("fox", string)
if match:
    print("Found:", match.group())
else:
    print("Not found")

match1 = re.findall("quick", string)
if match1:
    print("Found", match1)
else:
    print("Not found")

match2 = re.sub("fox", "cat", string)
print(match2)

pattern = re.compile("fox")
mathc3 = pattern.search(string)
if mathc3:
    print("Found:", mathc3.group())
    print("Found:", mathc3.start())
    print("Found:", mathc3.end())
    print("Found:", mathc3.span())
else:
    print("Not found")

#匹配数字
string1 = "hello world 123 dodo"
mathc4 = re.findall("\d+", string1)
print(mathc4)

#匹配邮箱
email = "yuanhao_fight@163.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
matches = re.findall(pattern, email)
print(matches)

#匹配URL
url = "https://www.google.com/search?q=python"
pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
matches = re.findall(pattern, url)
print(matches)

#匹配日期
date = "Today is 2024-07-07."
pattern = r"\d{4}-\d{2}-\d{2}"
matches = re.findall(pattern, date)
print(matches)

#匹配IP地址
ip = "192.168.1.1"
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
matches = re.findall(pattern, ip)
print(matches)

#匹配HTML标签
html = "<p>This is a paragraph.</p>"
pattern = r"<.*?>"
matches = re.findall(pattern, html)
print(matches)

#匹配手机号码
phone = "13812345678"
pattern = r"1[3-9]\d{9}"
matches = re.findall(pattern, phone)
print(matches)

#匹配身份证号码
idcard = "310101198001010001"
pattern = r"\d{6}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1-2]\d|3[0-1])\d{3}[0-9Xx]"
matches = re.findall(pattern, idcard)
print(matches)

#匹配QQ号码
qq = "123456"
pattern = r"^[1-9]\d{4,10}$"
matches = re.findall(pattern, qq)
print(matches)

#匹配中文字符
text = "这是一段中文文本。"
pattern = r"[\u4e00-\u9fa5]+"
matches = re.findall(pattern, text)
print(matches)

#匹配空白字符
text = "This is a sentence with spaces."
matches = re.findall("\s+", text)
print(matches)

#匹配非空白字符
text = "This is a sentence with spaces."
matches = re.findall("\S+", text)
print(matches)

#匹配多行文本
text = "Line 1\nLine 2\nLine 3"
matches = re.findall(r"^.*$", text, re.MULTILINE)
print(matches)

#匹配特定字符集
text = "The quick brown fox jumps over the lazy dog."
matches = re.findall("[aeu]", text)
print(matches)

#匹配特定字符集的补集
text = "The quick brown fox jumps over the lazy dog."
matches = re.findall("[^aeiou]", text)
print(matches)

#匹配重复字符集
text = "The quick brown fox jumps over the lazy dog."
matches = re.findall("o+", text)
print(matches)
