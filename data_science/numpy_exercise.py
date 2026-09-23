"""
2026.4.22 周三
1、创建：np.array/zeros(shape,dtype)/ones/empty/arange/reshape/linspace
2、属性：np.ndim/shape/size/dtype/T转置/flat平铺/newaxis升维
3、矩阵：np.dot乘法/linalg.inv求逆/transpose转置
4、其他运算：np.min值/argmin索引位/max/argmax/mean/average/median/nonzero非零索引位/clip(arr,min,max)/flatten
5、索引切片：index/slice
6、复制视图：arr.copy/view
7、迭代：np.nditer
8、连接拆分：np.concatenate/stack/array_split/hsplit/hstack/vsplit/vstack/dsplit/dstack
9、过滤排序：np.where/searchsorted/filter_arr/sort

2026.4.23 周四
1、排列：random.shuffle/permutation
2、画图：seaborn.displot/matplot.pyplot
3、生成随机数：random.randint(n,size)/rand(size)/choice(list,p,size)
4、数据分布：
1.均匀分布uniform(low,high,size)
2.正态分布normal(loc,scale,size)
3.逻辑斯蒂分布logistic(loc,scale,size)
4.泊松分布poisson(lam,size)
5.指数分布exponential(scale,size)
6.卡方分布chisquare(df,size)
7.瑞利分布rayleigh(scale,size)
8.二项分布binomial(n,p,size)
9.多项分布multinomial(n,pvals,size)
10.帕累托分布pareto(a,size)
11.齐夫分布zipf(a,size)

2026.4.24 周五
1、向量化：np.frompyfunc(func,i,o),np.ufunc
2、基本运算（+-*/**%）：np.add/subtract/multiply/divide/power/mod/remainder/divmod/absolute/abs
3、舍入：np.trunc/around/floor/ceil
4、对数：np.log2/log10/log/math.log(x,base)
5、累加/累积/累差：np.sum/cumsum/prod/cumprod/diff
6、最小公倍数/最大公约数：np.lcm/lcm.reduce/gcd/gcd.reduce
7、三角函数：np.sin/cos/tan/np.pi/deg2rad/rad2deg/arcsin/arccos/arctan/hypot
8、双曲函数：np.sinh/cosh/tanh/arcsinh/arccosh/arctanh
9、集合：np.unique/union1d/intersect1d/setdiff1d/setxor1d
"""


import numpy as np
import math
from numpy import random

data = [
    [0, 20], 
    [40, 10]
]

##numpy的属性
# arr = np.array(data)
#print("dimension:", arr.ndim)
#print("shape:",arr.shape)
#print("size:",arr.size)

##numpy的创建array
# arr = np.array(data)
# arr_zero = np.zeros((2, 3))
# arr_one = np.ones((2, 3), dtype=np.int16)
# arr_range = np.arange(10).reshape((2, 5))
# arr_linspace = np.linspace(1, 10, 10)
#print(arr.dtype)

##numpy的基础运算
# arr_random = np.random.random((2, 3))
# sum = np.sum(arr_random)
# min = np.min(arr_random, axis=0)
# max = np.max(arr_random, axis=1)
# arr_a = np.array(data)
# arr_b = np.arange(4).reshape((2, 2))
# plus = arr_a + arr_b
# subtract = arr_a - arr_b
# multiply = np.dot(arr_a, arr_b) #乘法
# multiply_2 = arr_a.dot(arr_b)
# m = np.linalg.inv(arr_a)    #矩阵除法：求逆a^-1, 再乘a*a^-1 = I
# j = np.transpose(arr_a) #转置a^T，一维数组无法用这个方法转置，需要用切片
# power = arr_a**2
# sin = np.sin(arr_a)
# print(arr_b < 3)
# print(sum)
# print(arr_a)
# print(m)
# print(a.T)  #转置

##基础运算2
# a = np.arange(2, 14).reshape(3, 4)
# a = np.array(data)
# b = np.argmin(a)
# c = np.min(a)
# d = np.mean(a, axis=0)
# d2 = a.mean()
# d3 = np.average(a)
# e = np.median(a)
# i = np.sort(a)
# # i2 = a.sort()
# f = a.cumsum()
# g = np.diff(a)
# h = a.nonzero()
# l = np.clip(a, 5, 9)
# print(a)
# print(h)
# print(l)
# print(d)
# print(k)
# print(i2) #返回None


##索引
# arr = np.arange(3, 15).reshape(3, 4)

# for row in arr:   #迭代行
#     print(row)

# for column in arr.T:  #迭代列
#     print(column)

# for item in arr.flat: #平铺属性，返回generator
#     print(item)
# print(arr.flatten())  #平铺方法，返回array

# print(arr)
# print(arr[1][1])
# print(arr[1, 1])
# print(arr[1, :])  #slice
# print(arr[:, 1])
# print(arr[:][1])


##合并
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# a2 = a[np.newaxis,:]  #一维数组升级成二维数组，x轴
# a3 = a[:, np.newaxis] #一维数组升级成二维数组，y轴
# b2 = b[np.newaxis,:]
# b3 = b[:, np.newaxis]
# c = np.vstack((a, b))   #Vertical stack, 纵向堆
# d = np.hstack((a, b))   #Horizontal stack, 横向堆
# e = np.concatenate((a, b), axis=0)        #x轴合，相当于纵向堆
# e2 = np.concatenate((a2, b2), axis=0) 
# e3 = np.concatenate((a3, c.T), axis=1)    #y轴合，相当于横向堆

# print(c)
# print(e)
# print(e2)
# print(e3)


##分割
# a = np.arange(12).reshape((3, 4))
# b = np.split(a, 2, axis=1)          #y轴等分
# b2 = np.hsplit(a, 2)                #横向等分，相当于y轴等分
# c = np.split(a, 3, axis=0)          #x轴等分
# c2 = np.vsplit(a, 3)                #纵向等分，相当于x轴等分
# d = np.array_split(a, 2, axis=0)    #不等分

# print(a)
# print(b)
# print(c)
# print(b2)


##copy
# a = np.arange(4)
# b = a.copy()
# a[1:3] = [11, 22]
# b[0] = 1

# print(a)
# print(b)

##Index
# a = np.array([1,2,3,4,5,6])
# b = a[1:3]                      #view
# b[0:2] = 22                     #broadcasting

# print(a)
# print(a[0])
# print(b)

##Attribute
# c = np.array([1,2,3], dtype='int16')

# print(a.ndim == len(a.shape))
# print(a.size == math.prod(a.shape))
# print(c.dtype)

##Creation
# d = np.zeros(2)
# e = np.ones(2)
# f = np.empty(2)     #speed
# g = np.arange(1,6,2)
# h = np.linspace(1,6,3, dtype='int16')

# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

##Sort & concatenate
# a = np.array([3,2,1,4,5,6])
# sorted_a = np.sort(a)
# concatenate_a = np.concatenate((a, sorted_a))

# print(sorted_a)
# print(concatenate_a)

##====== 练习题 ======
#模块1：数组创建
# print(np.zeros(10))                 #全0数组
# print(np.ones((3,3)))               #全1数组
# # print(np.ones((2,3))*6)
# print(np.array([6]*6).reshape((2,3)))
# print(np.full((2,3),6))             #全6数组
# print(np.arange(10))                #等差数组
# print(np.eye(3))                    #单位矩阵
# print(random.rand(3,4))             #0-1随机数组
# print(random.normal(0,1,size=5))    #正态分布
# print(np.array([1,2,3,4,5]))        #列表创建

#模块2：索引与切片
# arr = np.arange(10)
# print(arr)
# print(arr[2])
# print(arr[2:5])

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[1,2])
# print(arr[0])
# print(arr[:,1])

# arr = np.arange(20)
# filter_arr = (arr > 5) & (arr < 15)   #一定要加 () 和 &，and不行
# print(arr[filter_arr])

#模块3：基础运算与统计
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# arr = np.arange(10)
# print(arr)
# print(arr.sum())
# print(arr.max())
# print(arr.min())

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# print(arr.sum(axis=1))
# print(arr.mean(axis=0))
# print(arr.T)

# arr = np.arange(10)
# print(arr)
# print(arr+5)

# arr = np.array([1,4,9,16,25])
# print(arr)
# print(np.sqrt(arr))               #平方根
