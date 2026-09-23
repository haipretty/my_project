import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##创建pandas数据
##一维数组
s = pd.Series([1, 2, 3, np.nan, 4, 5])
# print(s)

##日期
dates = pd.date_range('20260410', periods=6)
# print(dates)

##二维数组
df = pd.DataFrame(np.random.randn(6, 4), index=s, columns=['a', 'b', 'c', 'd'])
# print(np.random.randn(3, 4))
# print(df)

df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(df2)

df3 = pd.DataFrame({'A':1, 'B':2}, index=[1])
# print(df3)

# print(df)
# index = df.a > 0
# print(index)
# print(df.a[index])
# print(df[index])

##各种属性
# print(df)
# print(df.dtypes)        #数据类型
# print(df.index)         #行表头
# print(df.columns)       #列表头
# print(df.values)        #值
# print(df.describe())    #个数/平均值/标准差
# print(df.T)             #转置

##排序
# sort_index_df = df.sort_index(axis=0, ascending=True)   #按照index排序
# print(sort_index_df)

# sort_values_df = df.sort_values(axis=0, by="a", ascending=True) #x轴上，根据a列排序
# print(sort_values_df)

# sort_values_df2 = df.sort_values(axis=1, by=1, ascending=True)  #y轴上，根据1行排序
# print(sort_values_df2)

dates = pd.date_range('20260410', periods=3)
df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=dates, columns=["a", "b", "c", "d"])
# print(df)

##Select数据筛选
# print(df["a"])                    #单列访问
# print(df.a)
# print(df[0:2])                    #行切片访问
# print(df["20260410":"20260411"])
#print(df["20260410"])              #不能访问某一行！
#print(df["a":"c"])                 #不能根据列切片！

##Select by label——按标签
# print(df.loc["20260410"])         #可以访问某一行
# print(df.loc[:, ["a", "c"]])
# print(df.loc["20260410":"20260411", ["a", "c"]])

##Select by position——按索引位置
# print(df.iloc[1])               #第二行数据
# print(df.iloc[0, 1])            #第一行第二列数据
# print(df.iloc[:, 1])            #第二列数据
# print(df.iloc[[0, 2], 0:2])     #单选第1行和第3行，1-2列数据

##Mixed select——标签+索引位置
#print(df.ix[0:2, ["a", "c"]])      #ix索引已废弃！

##Boolean indexing
# print(df[df.a > 1])


##赋值
dates = pd.date_range('20260411', periods=3)
df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=dates, columns=["a", "b", "c", "d"])

# df.iloc[0, 1] = 11              #索引位赋值
# df.loc['20260411', 'a'] = 99    #标签赋值
# df[df.a > 6] = 6
# #df.a[df.a > 6] = 6             #不行！
# df['e'] = np.nan
# df['f'] = pd.Series([1, 2, 3], index=pd.date_range('20260411', periods=3))
# print(df)


##处理丢失数据
# df.iloc[0, 0] = np.nan
# df.iloc[1, 1] = np.nan

# print(df)
# print(df.dropna(axis=0, how='any'))     #how=('any', 'all')
# print(df.fillna(value=0))
# print(np.any(df.isnull()) == True)


##导入导出
# data = pd.read_csv('csv.csv')
# print(data)

# data.to_pickle('csv.pickle')        #二进制流
# pickle = pd.read_pickle('csv.pickle')
# print(pickle)


##合并
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
df4 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1,2,3])
df5 = pd.DataFrame(np.ones((3, 4)), columns=['b', 'c', 'd', 'e'], index=[2,3,4])

# print(df1)
# print(df2)
# print(df3)
# print(df4)
# print(df5)

##concatenate
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)     #x轴（默认）
# res2 = pd.concat([df1, df2, df3], axis=1, ignore_index=True)    #y轴
# # print(res)
# # print(res2)

# ##join = ('inner', 'outer')
# res3 = pd.concat([df4, df5], join='inner')  #交集
# res4 = pd.concat([df4, df5], join='outer')  #并集（默认）
# # print(res3)
# # print(res4)

# ## join_axes（废弃）
# # res5 = pd.concat([df4, df5], axis=1, join_axes=[df4.index])  
# # print(res5)

# ##append（废弃）
# # res6 = df4.append(df5, ignore_index=True)
# # print(res6)

# s = pd.Series([1,2,3,4], index=['a','b','c','d'])   #Series是一列数据               
# res7 = pd.concat([df4, s.to_frame().T])    #将Series转成DataFrame格式，再转置
# print(res7)

##merge
# l = pd.DataFrame({'key':['k0','k1','k2','k3'],
#                      'a':['a0','a1','a2','a3'],
#                      'b':['b0','b1','b2','b3']})    #字典在这里是按列展示的
# r = pd.DataFrame({'key':['k0','k1','k2','k3'], 
#                      'c':['c0','c1','c2','c3'],
#                      'd':['d0','d1','d2','d3']})
# l2 = pd.DataFrame({'key':['k0','k0','k1','k2'],
#                     'key2':['k0','k1','k0','k1'],
#                      'a':['a0','a1','a2','a3'],
#                      'b':['b0','b1','b2','b3']})
# r2 = pd.DataFrame({'key':['k0','k1','k1','k2'], 
#                     'key2':['k0','k0','k0','k0'], 
#                      'c':['c0','c1','c2','c3'],
#                      'd':['d0','d1','d2','d3']})
# l3 = pd.DataFrame({'key':[0,1],
#                    'col_left':['a','b']})
# r3 = pd.DataFrame({'key':[1,2,2],
#                    'col_right':[2,2,2]})
# l4 = pd.DataFrame({'a':['a0','a1','a2'],
#                      'b':['b0','b1','b2']}, index=[1,2,3])
# r4 = pd.DataFrame({'c':['c0','c1','c2'],
#                      'd':['d0','d1','d2']}, index=[2,3,4])
# l5 = pd.DataFrame({'key':[0,1],
#                    'col':['a','b']})
# r5 = pd.DataFrame({'key':[1,2,2],
#                    'col':[2,2,2]})

# print(l)
# print(r)
# print(l2)
# print(r2)
# print(l3)
# print(r3)
# print(l4)
# print(r4)
# print(l5)
# print(r5)

# #merge by key column
# res = pd.merge(l, r, on='key')

# #merge by key columns
# res = pd.merge(l2, r2, on=['key','key2'], how='inner')   #交集（默认）
# res = pd.merge(l2, r2, on=['key','key2'], how='outer')   #并集
# res = pd.merge(l2, r2, on=['key','key2'], how='left')    #左key对齐
# res = pd.merge(l2, r2, on=['key','key2'], how='right')   #右key对齐
# #res = pd.merge(l2, r2, on=['key','key2'], how='cross')   #数据不支持

# #merge with indicator
# res = pd.merge(l3, r3, on='key', how='outer', indicator=True)           #指出哪边有值
# res = pd.merge(l3, r3, on='key', how='outer', indicator='indicator')    #指定指示器名词

# #merge by index
# res = pd.merge(l4, r4, left_index=True, right_index=True, how='outer')

# #handle overlapping column
# res = pd.merge(l5, r5, on='key', how='outer', suffixes=['_left','_right'])

# print(res)


##画线型图plot=('bar','hist','box','kde','area','scatter','hexbin','pie')
#by Series
data = pd.Series(np.random.randn(10), index=np.arange(10))
# print(data)
# data.plot()                     #画图，x轴=index，y轴=values
# data_cum_sum = data.cumsum()    #累加
# data_cum_sum.plot()             #画图
# plt.show()                      #展示图

#by DataFrame
data2 = pd.DataFrame(np.random.randn(10, 4),        #10行4列的数据
                     index=np.arange(1, 11),
                     columns=list("abcd"))
# print(data2.head(5))            #前5个数据（默认）
# data2 = data2.cumsum()
# data2.plot()                    #画图，x轴=index，y轴=values，每个列一条线
# plt.show()

#散点图plot.scatter
# ax = data2.plot.scatter(x='a', y='b', color='DarkBlue', label='Class 1')
# data2.plot.scatter(x='a', y='c', color='DarkGreen', label='Class 2', ax=ax)
# plt.show()


##====== 练习题 ======
#模块1：Series 与 DataFrame 创建
# print(pd.Series([10,20,30,40,50], index=list("abcde")))
# print(pd.DataFrame({
#     '姓名':['张三','李四','王五'],
#     '年龄':[20,21,22],
#     '成绩':[85,90,78]
#     }))
# df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"))
# print(df)
# print(df.info())
# print(df.columns)
# print(df.index)
# print(df.shape)
# print(df.head(2))         #前2行
# print(df['A'])            #DataFrame的每一列都是一个Series
# df.to_csv("test.csv",index=False)
# df = pd.read_csv("test.csv")
# print(df.to_string(index=False))

#模块2：数据筛选与清洗
# df = pd.DataFrame({
#     '姓名':['张三','李四','王五','赵六'],
#     '成绩':[85,90,78,92],
#     '班级':['一班','二班','一班','二班']
# })
# print(df[df['成绩']>85])
# print(df[df['班级']=='一班'])
# print(df[(df['成绩']>80) & (df['班级']=='二班')])   #必须加() 和 &，and不行

df_nan = pd.DataFrame({
    'A':[1,2,np.nan,4],
    'B':[5,np.nan,7,8]
})
# print(df_nan.isnull())
# print(df_nan.fillna(0,inplace=True))
# print(df_nan)
# print(type(df_nan.mean()))
# print(df_nan.fillna(df_nan.mean()))     #每一列都填充平均值
# print(df_nan.dropna())
# print(df_nan.mode().iloc[0])
# df_nan.median()
# df_nan.fillna(method="ffill")
# df_nan.fillna(method="bfill")
# df_dup = pd.DataFrame({
#     'A':[1,2,2,3],
#     'B':[4,5,5,6]
# })
# print(df_dup)
# print(df_dup.duplicated())
# print(df_dup.drop_duplicates())

# df['总分'] = df['成绩']+10            #DataFrame新增一列，与字典一样
# print(df)

#模块 3：分组与聚合统计（像成绩管理系统了）
# df = pd.DataFrame({
#     '班级':['一班','二班','一班','二班','一班','二班'],
#     '成绩':[85,90,78,92,88,80],
#     '性别':['男','女','女','男','男','女']
# })
# print(df.groupby('班级')['成绩'].mean())                  #每个班，平均成绩
# print(df.groupby(['班级','性别'])['成绩'].mean())         #每个班+性别，平均成绩
# print(df.groupby('班级')['成绩'].agg(['max','min','sum','mean','median','std']))    #聚合函数
# print(df['班级'].value_counts())                          #班级人数（值个数）
# print(df.sort_values('成绩', ascending=False))            #按成绩排序
# df['成绩等级'] = pd.cut(df['成绩'],bins=[0,80,90,101],labels=['C','B','A'],right=False,include_lowest=True)     #连续值分区
# print(pd.pivot_table(df,index='班级',columns='性别',values='成绩',aggfunc='mean'))  #重塑+聚合
# print(df['成绩等级'].value_counts())                      #成绩等级人数


