import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns
import pandas as pd

x = np.arange(0, np.pi*2, 0.1)
y = np.sin(x)
z = np.cos(x)

# plt.title("my test", loc="center")
# plt.xlabel("x轴", loc="right")
# plt.ylabel("y轴", loc="top")
# plt.plot(x, y, 'b-o', x, z, 'r')
# plt.grid(c='g', ls='--', lw='1')

# plt.subplot(2, 2, 1)
# plt.plot(x, y, 'b')
# plt.title("plot 1")
# plt.xlabel("x-label")
# plt.ylabel("y-label")

# plt.subplot(2, 2, 2)
# plt.plot(x, z, 'r')
# plt.title("plot 2")

# #plot 3:
# x = np.array([1, 2, 3, 4])
# y = np.array([3, 5, 7, 9])

# plt.subplot(2, 2, 3)
# plt.plot(x,y)
# plt.title("plot 3")

# plt.suptitle("super title")

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, c='b')

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# color = np.random.randint(0, 100, 15)
# plt.scatter(x, y, c=color, alpha=0.5, cmap='viridis')
# plt.colorbar()

# data = np.random.rand(100)    #[0,1)随机数
# data = np.random.randn(100)   #normal随机数
# data2 = np.random.normal(2, 1, 100)   #mean=2 std=1 normal随机数
# print(data2)

# 生成三组随机数据
# data1 = np.random.normal(0, 1, 1000)
# data2 = np.random.normal(2, 1, 1000)
# data3 = np.random.normal(-2, 1, 1000)

# # 绘制直方图
# plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
# plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
# plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# # 设置图表属性
# plt.title('RUNOOB hist() TEST')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# # plt.legend()

# plt.show()

# # 生成一个二维随机数组
# data = np.random.rand(10, 10)
# # print(data)
# # 绘制热力图
# plt.imshow(data, cmap='hot')

# # 显示图像
# # plt.colorbar()
# # plt.show()

# img = Image.open('map.jpg')
# # print(img)
# data = np.array(img)
# # print(data/255)
# # plt.imshow(data/255)
# plt.axis('off')
# # plt.show()

# # 创建一个二维的图像数据
# img_data = np.random.random((100, 100))

# # 显示图像
# # plt.imshow(img_data)

# # 保存图像到磁盘上
# # plt.imsave('runoob-test.png', img_data)

# img_color = np.zeros((100, 100, 3))
# # img_color[:, :, 0] = np.random.random((100, 100))
# # img_color[:, :, 1] = np.random.random((100, 100))
# # img_color[:, :, 2] = np.random.random((100, 100))


# # -------------------------- 设置中文字体 start --------------------------
# plt.rcParams['font.sans-serif'] = [
#     # Windows 优先
#     'SimHei', 'Microsoft YaHei',
#     # macOS 优先
#     'PingFang SC', 'Heiti TC',
#     # Linux 优先
#     'WenQuanYi Micro Hei', 'DejaVu Sans'
# ]
# # 修复负号显示为方块的问题
# plt.rcParams['axes.unicode_minus'] = False
# # -------------------------- 设置中文字体 end --------------------------

# # 生成模拟数据：在正弦曲线基础上加入一些随机噪声
# np.random.seed(42)
# X = np.linspace(0, 10, 20)
# y_true = np.sin(X)                     # 真实的潜在规律（我们不知道）
# y_noise = np.random.randn(20) * 0.3   # 随机噪声
# y = y_true + y_noise                  # 我们实际观测到的数据

# plt.scatter(X, y, label='观测数据 (含噪声)', color='blue', alpha=0.6)
# plt.plot(X, y_true, label='真实规律 (y=sin(x))', color='green', linewidth=2)
# plt.xlabel('X')
# plt.ylabel('y')
# plt.title('数据与潜在规律')
# plt.legend()
# plt.grid(True)
# # plt.show()

# # 创建一个示例数据框
# data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
# df = pd.DataFrame(data)
# # 创建一个相关性矩阵

# correlation_matrix = df.corr()
# # print(df,"\n",correlation_matrix)

# # 生成数据：0 到 10 之间取 100 个等间距点
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)   # 正弦函数
# y2 = np.cos(x)   # 余弦函数


# fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

# x = np.linspace(0, 10, 100)

# # 主图：绘制两条量纲不同的曲线
# ax.plot(x, np.sin(x), 'b-', label='sin(x) [amplitude]')
# ax.set_xlabel('x (radians)')
# ax.set_ylabel('sin(x)', color='blue')
# ax.tick_params(axis='y', labelcolor='blue')

# # 创建双 y 轴（共享 x 轴）
# ax2 = ax.twinx()
# ax2.plot(x, np.exp(x/5), 'r--', label='exp(x/5) [growth]')
# ax2.set_ylabel('exp(x/5)', color='red')
# ax2.tick_params(axis='y', labelcolor='red')

# # 在 ax 中添加嵌入子图（放大局部区域）
# axins = ax.inset_axes([0.15, 0.5, 0.3, 0.35])
# axins.plot(x, np.sin(x), 'b-')
# axins.set_xlim(3, 5)
# axins.set_ylim(-1.2, 1.2)
# axins.set_title('Zoomed Region')
# axins.grid(True, alpha=0.3)

# # 在主图上标记嵌入区域
# ax.indicate_inset_zoom(axins, edgecolor='gray')

# ax.set_title('Dual Y-Axes with Inset Zoom', fontsize=14)
# # plt.show()

# fig, ax = plt.subplots(figsize=(5,5),layout='constrained')
# ax.plot([1,2,3],[4,6,5])
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_title('subplots')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# # plt.show()

# sns.heatmap(annot=True)
# sns.barplot()


