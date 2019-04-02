# _*_ coding:utf-8 _*_

'''
求数据的各项均值，最大值最小值以及各项指标
2019-4-2
'''

import pandas as pd
import json

# 读入数据/注意编码问题
data_json = open('number.json','r',encoding='UTF-8').read()
# print(data_json)

# 转为DataFrame
data_list = json.loads(data_json)
data = [[d['price'], d['speed'],d['weight'],d['displacement'],d['power']] for d in data_list]
df = pd.DataFrame(data, columns=['price','speed','weight','displacement','power'])

print(df.describe().transpose())
# print(df)
















