
##====== 项目2：简易超市销售数据分析项目 ======
#模拟真实销售场景，完成时间趋势分析、品类销量统计、Top 产品筛选

import pandas as pd
import numpy as np

#1.创建模拟销售数据
# date_list = pd.date_range('2026-01-01', periods=7)
date_list = pd.date_range(start='2026-01-01', end='2026-01-07')
df = pd.DataFrame({
    '日期':np.random.choice(date_list, 100),
    '品类':np.random.choice(['零食','饮料','日用品','生鲜'], 100),
    '商品名': np.random.choice(['可乐','薯片','牛奶','纸巾','苹果','面包','矿泉水','洗衣液'], 100),
    '销量':np.random.randint(1, 20, 100),
    '单价':np.random.choice([2.5,3,5,8,10,12,15], 100)
})

print("===== 原始数据 =====")
print(df)

#2.数据加工
df['销售额'] = df['销量'] * df['单价']      #加一列
print(df)

#3.数据统计
print("\n===== 每日销售额统计 =====")
print(df.groupby('日期')['销售额'].sum().sort_index())
print("\n===== 各品类销量&销售额占比 =====")
# print(df.groupby('品类')[['销量','销售额']].sum())
print(df.groupby('品类').agg({'销量':'sum','销售额':'sum'}))    #dict：指定列分别聚合
print("\n===== 销量Top5商品 =====")
print(df.groupby('商品名')['销量'].sum().sort_values(ascending=False).head(5))  #Series的sort_values
print("\n===== 销售额Top3品类 =====")
print(df.groupby('品类')['销售额'].sum().sort_values(ascending=False).head(3))