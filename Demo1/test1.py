import jieba
excludes = {"瘟疫", "京师", "盛行", "军民", "草诏", "一面","民间","修设","星夜","临朝","信州","御香","误走","妖魔","一个","三清殿","下山"
            ,"次日","诏书","万民","住持","清宫","清宫","清宫","如何","两个","东京","明日","洒家","出来","经略"}#排除词库
txt = open("水浒传.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)#分词处理
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "张天师" or word == "天师":#合并不同称谓
        rword = "张天师"
    elif word == "洪太尉" or word == "洪信" or word == "太尉":
        rword = "洪信"
    elif word == "仁宗" or word == "天子" or word == "上帝":
        rword = "仁宗"
    elif word == "赵哲" or word == "宰相":
        rword = "赵哲"
    elif word == "参政" or word == "文彦博":
        rword = "文彦博"
    elif word == "太乙真君" or word == "真人":
        rword = "真人"
    elif word == "高毬" or word == "高俅":
        rword = "高俅"
    elif word == "柳大郎" or word == "柳世权":
        rword = "柳世权"
    elif word == "王四" or word == "董将士":
        rword = "王四"
    elif word == "端王" or word == "都尉":
        rword = "端王"
    elif word == "王进" or word == "牌头士":
        rword = "王进"
    elif word == "王升" or word == "王太尉":
        rword = "王升"
    elif word == "董生" or word == "董将士":
        rword = "董生"
    elif word == "史大郎" or word == "史进" or word == "大郎":
        rword = "史进"
    elif word == "李吉" or word == "你两个":
        rword = "李吉"
    elif word == "朱武" or word == "朱大人":
        rword = "朱武"
    elif word == "陈达" or word == "陈大人":
        rword = "陈达"
    elif word == "杨春" or word == "杨大人":
        rword = "杨春"
    elif word == "鲁提辖" or word == "鲁达" or word == "提辖":
        rword = "鲁达"
    elif word == "郑屠" or word == "郑大官人":
        rword = "郑屠"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)#排序
print("水浒传人物出场次数前20位:")
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))