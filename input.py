import csv
import bertOA
import numpy as np

analyCSVpath = "data/倾向性分析数据集.csv"  # 已评分数据集(CSV文件)路径

def classi(score):  # 根据评分分成四类
    score = float(score)
    if (score >= 0 and score < 0.25):
        return 0
    if (score >= 0.25 and score < 0.5):
        return 1
    if (score >= 0.5 and score < 0.75):
        return 2
    if (score >= 0.75 and score < 1):
        return 3

fp2 = open(analyCSVpath, 'r', encoding='utf-8')
analyCSV = csv.reader(fp2)
X = []  # 答案内容
y = []  # 对应评分
for i in analyCSV:
    X.append(i[1])
    y.append(classi(i[2]))

def partitioningData(data):
    random_order = range(len(data))
    np.random.shuffle(random_order)
    train_data = [data[j] for i, j in enumerate(random_order) if i % 10 != 0]
    valid_data = [data[j] for i, j in enumerate(random_order) if i % 10 == 0]
    return train_data, valid_data

train_data, valid_data=partitioningData(X)
model=bertOA.train(train_data, valid_data)