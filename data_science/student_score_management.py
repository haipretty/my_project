
##====== 项目1：学生成绩管理与分析项目 ======
#数据流程：创建 - 清洗 - 统计 - 筛选

import numpy as np
import pandas as pd

#1.创建数据
df = pd.DataFrame({
    '学号':[101,102,103,104,105,106,107,108],
    '姓名':['张三','李四','王五','赵六','孙七','周八','吴九','郑十'],
    '班级':['一班','一班','一班','一班','二班','二班','二班','二班'],
    '语文':[85, 92, 78, np.nan, 88, 95, 76, 82],
    '数学':[90, 85, 96, 88, 79, 92, 85, np.nan],
    '英语':[88, 76, 90, 92, 85, 78, 93, 86]
})

print("===== 原始数据 =====")
print(df)

#2.数据清洗
print("缺失数据用科目平均分填充")
# df_clean = df.fillna(df.mean(numeric_only=True))
df_clean = df.fillna({'语文':df['语文'].mean(),'数学':df['数学'].mean(),'英语':df['英语'].mean()})  #dict：指定列分别填充值

print("\n===== 清洗后完整数据 =====")
print(df_clean)

#3.数据统计
print("新增总分、平均分")
# df_clean["总分"] = df_clean[["语文","数学","英语"]].sum(axis=1)           #跨列相加
df_clean['总分'] = df_clean['语文'] + df_clean['数学'] + df_clean['英语']
df_clean["平均分"] = df_clean["总分"] / 3

print("\n===== 统计后完整数据 =====")
print(df_clean)

#4.数据筛选
print("\n===== 各班平均分统计 =====")
print(df_clean.groupby("班级")[["语文","数学","英语","总分"]].mean())       #四列分别平均
print("\n===== 总分前3名学生 =====")
print(df_clean.sort_values("总分",ascending=False).head(3))
print("\n===== 平均分≥80分的学生 =====")
print(df_clean[df_clean["平均分"]>=80])

