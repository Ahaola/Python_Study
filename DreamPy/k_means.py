import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


def loadDate(filePath):
    f = open(filePath, 'rb')  # 以二进制打开文件

    data = []
    img = image.open(f)  # 以列表形式储存图片像素值
    m, n = img.size  # 获得图片大小，为便利每个像素准备
    for i in range(m):
        for j in range(n):
            x, y, z = img.getpixel((i, j))
            # getpixel返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            data.append([x / 256.0, y / 256.0, z / 256.0])  # 将每个像素归一化成0-1
    f.close()
    return np.array(data), m, n  # 返回矩阵形式的data，以及图片的大小


imgData, row, col = loadDate("C:/Users/ASUS/Desktop/cat.png")
# 使用loadData方法处理图片
label = KMeans(n_clusters=3).fit_predict(imgData)
# 聚类获取每个像素所属类别
label = label.reshape([row, col])
# 创建一张灰度图保存聚类后的结果
pic_new = image.new("L", (row, col))
# 根据所属类别向图片中添加灰度值

for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), int(256 / (label[i][j] + 1)))
pic_new.save("C:/Users/ASUS/Desktop/new_cat.png", "JPEG")  # 保存处理后的图片