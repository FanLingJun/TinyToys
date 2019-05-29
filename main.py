# _*_ coding:utf-8 _*_

import pandas as pd
import json
import os

# 获取当前工作路径
os.getcwd()

def To_DataFrame():
  # 读入数据/注意编码问题
  data_json = open('recordnumber.json', 'r', encoding='utf-8').read()
  # 转为DataFrame
  data_list = json.loads(data_json)
  data = [[d['name'], d['price'], d['speed'], d['weight'], d['displacement'], d['power']] for d in data_list]
  df = pd.DataFrame(data, columns=['name', 'price', 'speed', 'weight', 'displacement', 'power'])
  return df

def WashData(df):

  df.dropna(axis = 0,inplace=True)
  print(df.describe().transpose())

def ShowDataFrame(df):
  print(df.describe().transpose())

def ShowPowerStatistic(df):
  print(df['power'])
  bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 200, 1000]
  data_cut = pd.cut(df['power'], bins)
  array = data_cut.value_counts()
  print(array)
  print(data_cut.value_counts())

def ShowPriceStatistic(df):
  print(df['price'])
  bins = [1, 5, 10, 15, 20, 25, 30, 35, 50, 100, 300, 1000, 10000]
  price_cut = pd.cut(df['price'], bins)
  print(price_cut.value_counts())

def ShowSpeedStatistic(df):
  print(df['speed'])
  bins = [0, 100, 150, 170, 175, 180, 185, 190, 200, 205, 210, 220, 300, 1000]
  data_cut = pd.cut(df['speed'], bins)
  print(data_cut)
  print(data_cut.value_counts())

def main():
  df = To_DataFrame()
  ShowDataFrame(df)

if __name__ == '__main__':
  main()
