import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#====== 基础设置 =====#
# Matplotlib 全局中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常
plt.rcParams['font.size'] = 12

#设置随机种子
np.random.seed(2026)
#====== 基础设置完成 =====#


#第一部分：Matplotlib基础绘图
#对应知识点：折线图、柱状图、时间序列、对比图
#====== 准备数据 =====#
#1.生成函数曲线数据
x = np.linspace(0, 2*np.pi, 100)            #x轴
y_sin = np.sin(x)
y_cos = np.cos(x)

#2.产品销量数据
product_list = ["产品A", "产品B", "产品C", "产品D", "产品E"]
sales_data = [120, 85, 160, 95, 130]

#3. 30天时间序列销售数据
data_range = pd.date_range(start="2026-06-01", periods=30, freq="D")    #日期
daily_sales = 1000 + np.random.randn(30)*150

#4.双Y周月度数据
months = [f"{i}月" for i in range(1,13)]                #月份
month_sales = np.random.randint(500, 2000, size=12)
month_profit = np.random.uniform(0.1, 0.3, size=12)
#====== 准备数据完成 =====#

#题目1：单折线图
# fig, ax = plt.subplots(figsize=(16,8), layout='constrained')  #自动优化布局，避免标签重叠
# ax.plot(x, y_sin, c='b', lw=2)
# ax.set_xlabel("x值")
# ax.set_ylabel("sin(x)")
# ax.set_title("正弦函数曲线")
# ax.grid(alpha=0.3, ls='--')                   #浅色网格线#
# plt.show()

#题目2：多折线对比图
# fig, ax = plt.subplots(figsize=(16, 8), layout='constrained')
# ax.plot(x, y_sin, c='r', label='y_sin')
# ax.plot(x, y_cos, c='b', label='y_cos')
# ax.legend(loc='upper right')                   #必须有label，loc#
# # ax.set_xlim(0, 2*np.pi)                       #限定x轴0~2π#
# # ax.set_ylim(-1.2, 1.2)                        #限定y轴-1.2~1.2#
# ax.axis([0, 2*np.pi, -1.2, 1.2])
# plt.show()

#题目3：基础柱状图
# fig, ax = plt.subplots(figsize=(12,6), layout='constrained')
# bars = ax.bar(product_list, sales_data)
# ax.bar_label(bars, fmt='%d', padding=3, fontsize=11)     #顶部标注具体数值#
# ax.set_ylim(0, max(sales_data)*1.15)                     #y轴从0开始#
# ax.set_title('产品销量对比')
# plt.show()

#题目4：时间序列可视化
# fig, ax = plt.subplots(figsize=(12,8), layout='constrained')
# ax.plot(data_range, daily_sales)    
# max_idx = daily_sales.argmax()
# min_idx = daily_sales.argmin()
# ax.annotate(f'销售额最高:{daily_sales.max():.0f}元',                 #标注销售额最高、最低的两个点位并配箭头#
#             xy=(data_range[max_idx], daily_sales[max_idx]), 
#             xytext=(data_range[max_idx-5], daily_sales[max_idx]+20), 
#             arrowprops=dict(facecolor='black', shrink=0.05, width=1))
# ax.annotate(f'销售额最低:{daily_sales.min():.0f}元', 
#             xy=(data_range[min_idx], daily_sales[min_idx]), 
#             xytext=(data_range[min_idx+1], daily_sales[min_idx]-10), 
#             arrowprops=dict())       
# ax.set_xticklabels(labels=data_range, rotation=45, ha='right')     #x轴日期标签旋转45°#
# plt.show()

#题目5：双Y轴对比图
# fig, ax = plt.subplots(figsize=(12,6), layout='constrained')
# ax.bar(months, month_sales, label='月度销量', color='y', alpha=0.5)
# ax.set_ylabel('销量')
# ax2 = ax.twinx()
# ax2.plot(months, month_profit, label='月度利润率', color='b')
# ax2.set_ylabel('利润率')                        
# handle1, label1 = ax.get_legend_handles_labels()
# handle2, label2 = ax2.get_legend_handles_labels()
# ax.legend(handle1 + handle2, label1 + label2, loc='upper right')      #添加双轴标签和图例#
# plt.show()


#对应知识点：散点图、直方图、箱线图、子图布局、分布分析
#====== 准备数据2 =====#
#1.正态分布散点数据
scatter_x = np.random.randn(100)
scatter_y = np.random.randn(100)

#2.正态分布直方图数据
hist_data = np.random.normal(loc=5, scale=2, size=1000)

#3.三组对比箱线图数据
box_data = [
    np.random.normal(2, 0.8, 200),
    np.random.normal(5, 1.0, 200),
    np.random.normal(8, 0.9, 200)
]
box_labels = [f"组别{i}" for i in range(4) if i != 0]

#4.分类散点数据
classA_x = np.random.normal(2, 0.6, 50)
classA_y = np.random.normal(3, 0.6, 50)
classB_x = np.random.normal(5, 0.7, 50)
classB_y = np.random.normal(6, 0.7, 50)

#5.四种分布数据
dist_norm = np.random.normal(0, 1, 500)
dist_uniform = np.random.uniform(-3, 3, 500)
dist_poisson = np.random.poisson(2, 500)
dist_exp = np.random.exponential(1, 500)
dist_list = [dist_norm, dist_uniform, dist_poisson, dist_exp]
dist_names = ["正态分布", "均匀分布", "泊松分布", "指数分布"]
#====== 准备数据2完成 =====#

#题目1：散点图
# fig, ax = plt.subplots(figsize=(8, 6), layout='constrained')
# ax.scatter(scatter_x, scatter_y, s=25, alpha=0.6, c='darkgreen')
# ax.set_title("随机正态分布散点图")
# plt.grid(alpha=0.3)
# plt.show()

#题目2：直方图
# fig, ax = plt.subplots(figsize=(8,6), layout='constrained')
# ax.hist(hist_data, bins=20, edgecolor='black')      #柱子边框黑色#
# ax.set_xlabel('x轴')
# ax.set_ylabel('y轴')
# ax.grid(axis='y', alpha=0.3)
# plt.show()

#题目3：箱线图
# fig, ax = plt.subplots(figsize=(8,6), layout='constrained')
# ax.boxplot(box_data, tick_labels=box_labels)
# ax.set_title('三组数据分布对比箱线图')
# plt.show()

#题目4：子图
# fig, ax = plt.subplots(2, 2, figsize=(16,8), layout='constrained')
# ax[0, 0].plot(x, y_sin)
# ax[0, 0].set_title('正弦折线图')

# bars = ax[0, 1].bar(product_list, sales_data)
# ax[0, 1].bar_label(bars)
# ax[0, 1].set_title('销量柱状图')
# ax[0,1].tick_params(axis='x', rotation=30)      #与ax.set_xticklabels()等价

# ax[1, 0].scatter(scatter_x,scatter_y)
# ax[1, 0].set_title('正态散点图')

# ax[1, 1].hist(hist_data)
# ax[1, 1].set_title('分布直方图')
# plt.show()

#题目5：分类散点图
# fig, ax = plt.subplots(figsize=(8, 6), layout='constrained')
# ax.scatter(classA_x, classA_y, c='b', label='class A')
# # ax.annotate('A中心点', xy=(classA_x.mean(), classA_y.mean()), 
# #             xytext=(classA_x.mean()+0.2, classA_y.mean()),
# #             arrowprops=dict(arrowstyle='->', color='r'))
# ax.scatter(classB_x, classB_y, c='y', label='class B')
# # ax.annotate('B中心点', xy=(classB_x.mean(), classB_y.mean()), 
# #             xytext=(classB_x.mean()+0.2, classB_y.mean()),
# #             arrowprops=dict(arrowstyle='->', color='r'))
# a_center_x, a_center_y = classA_x.mean(), classA_y.mean()
# b_center_x, b_center_y = classB_x.mean(), classB_y.mean()
# ax.scatter(a_center_x, a_center_y, s=100, c='r', marker='*', zorder=5)            #标注中心点#
# ax.scatter(b_center_x, b_center_y, s=100, c='r', marker='*', zorder=5)
# ax.text(a_center_x+0.1, a_center_y, f'中心点({a_center_x:.1f}, {a_center_y:.1f})')
# ax.text(b_center_x+0.1, b_center_y, f'中心点({b_center_x:.1f}, {b_center_y:.1f})')
# ax.legend()
# plt.show()

#题目6：多分布子图
# fig, ax = plt.subplots(1, 4, figsize=(16, 8), layout='constrained', sharey=True)    #统一y轴范围#
# for i in range(4):
#     ax[i].hist(dist_list[i])
#     ax[i].set_title(dist_names[i])
# plt.suptitle('四种概率分布', y=1.05)        
# plt.show()


#第二部分：图表美化与样式配置
#对应知识点：中文显示、样式表、自定义配置、标注、专业排版
#数据
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)

product_list = ["产品A", "产品B", "产品C", "产品D", "产品E"]
sales_data = [120, 85, 160, 95, 130]

#题目1：样式表对比
#分别使用ggplot、fivethirtyeight、dark_background三种内置样式绘制同一条sin曲线，观察视觉差异
# style_list = ["ggplot", "fivethirtyeight", "dark_background"]
# for style in style_list:
#     with plt.style.context(style):        #临时生效样式，不影响全局
#         fig, ax = plt.subplots(figsize=(8, 6), layout='constrained')
#         ax.plot(x, y_sin, lw=2)
#         ax.set_title(f"当前样式：{style}")
#         plt.show()

#题目2：关键点标注
#绘制sin(x)曲线，在(π/2, 1)处标注「最大值」、(3π/2, -1)处标注「最小值」，均配箭头指向
# fig, ax = plt.subplots(figsize=(16,8), layout='constrained')
# ax.plot(x, y_sin)
# ax.annotate('最大值', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 1), arrowprops=dict())
# ax.annotate('最小值', xy=(np.pi*3/2, -1), xytext=(np.pi*3/2+1, -1), arrowprops=dict())
# plt.show()

#题目3：全局样式自定义
#通过rcParams全局设置：默认线宽2、主色墨绿色、网格虚线、坐标轴标签字号14，绘制折线图验证效果
# with plt.rc_context({                     #临时修改全局配置
#     "lines.linewidth": 12,
#     "lines.color": "darkgreen",
#     "grid.linestyle": "--",
#     "axes.labelsize": 30,
#     "axes.titlesize": 40
# }):
#     fig, ax = plt.subplots(figsize=(8,6), layout='constrained')
#     ax.plot(x, y_sin)
#     ax.set_xlabel("x轴")
#     ax.set_ylabel("y轴")
#     ax.set_title("全局自定义样式")
#     ax.grid(alpha=0.5)
#     plt.show()

#题目4：出版级柱状图美化
#绘制销量柱状图，要求：去掉顶部/右侧边框、自定义渐变色、柱子顶部标数值、水平网格置于底层、排版整齐无溢出
# fig, ax = plt.subplots(figsize=(8,6), layout='constrained')

# # 渐变色柱子
# colors = ["#e0f2fe", "#7dd3fc", "#0ea5e9", "#0284c7", "#0369a1"]
# bars = ax.bar(product_list, sales_data, color=colors, zorder=5)     # 渐变色柱子
# ax.bar_label(bars, fmt='%d', padding=2)                 # 柱子顶部标注数值

# # ax.spines["top"].set_visible(False)
# # ax.spines["right"].set_visible(False)
# ax.spines[["top", "right"]].set_visible(False)          # 去掉顶部和右侧边框

# # ax.yaxis.grid(True, alpha=0.3, linestyle="--")
# # ax.set_axisbelow(True)
# ax.grid(axis='y', alpha=0.3, linestyle="--", zorder=0)  # 网格置于底层
# plt.show()


#第三部分：Seaborn统计图表
#对应知识点：热力图、分布图、配对图、联合分布图
# 加载seaborn内置数据集
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
# print(iris.head())      #columns: sepal_length  sepal_width  petal_length  petal_width species(Setosa、Versicolor、Virginica)
# print(tips.head())

#题目1：相关性热力图
#计算iris数据集4个数值特征的相关系数矩阵，绘制热力图，格子显示系数数值，配色RdBu_r
# plt.figure(figsize=(16,8))
# corr_matrix = iris.select_dtypes("number").corr()
# sns.heatmap(corr_matrix, cmap="RdBu_r", annot=True, fmt=".2f")
# plt.tight_layout()

#题目2：单变量分布图
#绘制tips数据集total_bill列的直方图+核密度曲线；再绘制按sex分组的核密度对比图
# plt.figure(figsize=(16,8))
# sns.histplot(x='total_bill', data=tips, kde=True)
# sns.kdeplot(x='total_bill', hue='sex', data=tips, shade=True)
# plt.tight_layout()

#题目3：多变量配对图
#对iris数据集绘制pairplot，按species分类上色，观察不同品种的特征差异
# sns.pairplot(data=iris, hue='species', palette="Set2", corner=True)

# #题目4：联合分布分析
#tips数据集x=消费总额、y=小费，绘制kind=reg的jointplot，展示散点、回归线和边缘分布
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

# #题目5：箱线图叠加散点
#按日期分组绘制消费总额箱线图，叠加stripplot展示原始数据点，商务风配色
# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.stripplot(x='day', y='total_bill', data=tips, jitter=0.2)
# plt.show()

#对应知识点：回归图、分类图、小提琴图、分面网格
#plotly内置数据集
anscombe = sns.load_dataset("anscombe")     #安斯库姆四重奏
# print(anscombe.head(1))

#题目1：线性回归图
# plt.figure(figsize=(7, 5))
# sns.regplot(data=tips, x="total_bill", y="tip", color="#4C72B0",
#             scatter_kws={"alpha":0.6, "s":30}, 
#             line_kws={"linewidth":2})                   #95%置信区间？
# plt.title("消费金额与小费线性回归")
# plt.grid(alpha=0.3)
# plt.tight_layout()

#题目2：分类柱状图
# df = tips.groupby('day')['total_bill'].mean()             #按日期分组展示每日平均消费金额
# sns.barplot(df)
# sns.barplot(data=tips, x="day", y="total_bill", 
#             palette="Set2", errorbar="sd")                #自动显示误差棒？
# plt.title("每日平均消费金额（带误差棒）")
# plt.ylabel("平均消费金额（美元）")

#题目3：分组小提琴图
# sns.violinplot(data=tips, x="day", y="total_bill", hue="sex",
#                split=True, palette="Set2", inner="quartile")
# plt.title("不同日期、性别的消费分布小提琴图")
# plt.ylabel("消费总额（美元）")

#题目4：分面网格图？
#行=用餐时段、列=性别，每个子图绘制「日期-消费总额」的箱线图
# g = sns.FacetGrid(tips, row="time", col="sex", height=3, margin_titles=True)
# g.map(sns.boxplot, "day", "total_bill", order=["Thur", "Fri", "Sat", "Sun"], palette="Set2")
# g.set_axis_labels("日期", "消费总额")
# plt.suptitle("分时段、分性别消费分布", y=1.02)

#题目5：安斯库姆四重奏验证？
#对四组数据分别绘制lmplot，观察回归直线的一致性与数据分布的差异性
# sns.lmplot(data=anscombe, x="x", y="y", col="dataset", hue="dataset",
#            col_wrap=2, ci=None, palette="Set2", height=3.5,
#            scatter_kws={"s": 50, "alpha": 0.8})
# plt.suptitle("安斯库姆四重奏：相同回归，不同分布", y=1.02)
# plt.show()


#第四部分：Plotly交互式可视化
#对应知识点：Plotly Express基础交互式图表
import plotly.express as px

# 函数曲线数据
x = np.linspace(0, 2*np.pi, 100)
df = pd.DataFrame({
    "x": x,
    "sin(x)": np.sin(x),
    "cos(x)": np.cos(x)
})
df_line = df.melt(id_vars="x", var_name="函数", value_name="y值")   #宽表转长表

# print(df.head())
# print(df_line.head())
# sns.lineplot(data=df_line, x="x", y="y值", hue="函数")    #通过hue分组，sin和cos函数一起画
# plt.show()

# 产品销量数据
df_sales = pd.DataFrame({
    "产品": [f"产品{i}" for i in "ABCDE"],      #列表生成式
    "销量": [120, 85, 160, 95, 130],
    "利润": [30, 20, 45, 25, 35]
})

# plotly内置数据集
iris = px.data.iris()
gapminder = px.data.gapminder()

#题1：交互式折线图
# fig = px.line(df_line, x="x", y="y值", color="函数", 
#               title="交互式折线图",
#               labels={"x":"x值", "y值":"y值"})    #labels#
# fig.update_layout(                                #调整布局
#     hovermode="x unified",
#     title="交互式折线图",
#     xaxis_title="x轴",
#     yaxis_title="y轴"
# )

#题2：多维度散点图
# print(iris.head())
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", 
#                  color="species", size="petal_length",
#                  hover_data=["petal_width"],                #悬停额外显示字段
#                  title="鸢尾花特征多维度散点图",
#                  labels={"sepal_width": "花萼宽度", "sepal_length": "花萼长度", "species": "品种"})      

#题目3：交互式柱状图
# df_sales_melt = df_sales.melt(id_vars="产品", var_name="指标", value_name="数值")
# fig = px.bar(df_sales_melt, x="产品", y="数值", color="指标", 
#              barmode="group", text_auto=True)             #并排显示，显示数值

#题目4：时间动画散点图
# fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", 
#                  color="continent", hover_name="country", 
#                  animation_frame="year", animation_group="country",
#                  log_x=True, size_max=60,
#                  range_x=[100, 100000], range_y=[25, 90],
#                  title="全球人均GDP与预期寿命变化趋势（1952-2007）",
#                  labels={"gdpPercap": "人均GDP", "lifeExp": "预期寿命", "continent": "大洲"})

# fig.show()


#对应知识点：Streamlit / Dash 简易仪表盘
import streamlit as st
from dash import Dash, html, dcc, callback, Output, Input

# st.set_page_config(page_title="仪表盘", layout="wide")
# st.title("streamlit 仪表盘")

# #侧边栏配置
# with st.sidebar:
#     st.header("图表配置")
#     data_source = st.radio("选择数据源", ["内置Tips数据集", "上传CSV文件"])     #单选框


#     if data_source == "上传CSV文件":
#         upload_file = st.file_uploader("上传CSV文件", type="csv")
#         if upload_file:
#             df2 = pd.read_csv(upload_file)
#         else:
#             st.info("请上传CSV文件")
#     else:
#         df2 = px.data.tips()
    
#     numeric_cols = df2.select_dtypes("number").columns.tolist()
#     x_col = st.selectbox("选择x轴字段", numeric_cols, index=0)      #默认选0索引位
#     y_col = st.selectbox("选择y轴字段", numeric_cols, index=1)      #默认选1索引位
#     chart_type = st.selectbox("选择图表类型", ["折线图", "散点图", "柱状图", "箱线图"])

# #主区域渲染图表
# col1, col2 = st.columns([2, 1])             #把页面切成2:1的两列
# with col1:
#     if chart_type == "折线图":
#         fig = px.line(df2, x=x_col, y=y_col, title=f"{y_col}随{x_col}变化趋势")
#     elif chart_type == "散点图":
#         fig = px.scatter(df2, x=x_col, y=y_col, title=f"{x_col}和{y_col}散点分布")
#     elif chart_type == "柱状图":
#         fig = px.bar(df2, x=x_col, y=y_col, title=f"{x_col}对应{y_col}统计")
#     elif chart_type == "箱线图":
#         fig = px.box(df2, x=x_col, y=y_col, title=f"{x_col}分组下{y_col}分布")
#     st.plotly_chart(fig, width="content")

# with col2:
#     st.subheader("数据概览")
#     st.dataframe(df2.describe(), width="content")

# # 启动
# # streamlit run d:/workspace/python/data_science/data_visualization.py


#对应知识点：地图可视化
#准备数据
carshare = px.data.carshare()
# print(gapminder.head())

#题目1：散点地图
# fig = px.scatter_map(carshare, lat="centroid_lat", lon="centroid_lon", 
#                      color="peak_hour", size="car_hours", 
#                      size_max=15, hover_name="peak_hour", 
#                      color_continuous_scale=px.colors.cyclical.IceFire, 
#                      zoom=10, center=dict(lat=45.48, lon=-73.59), 
#                      map_style="carto-positron", 
#                      title="车辆租赁")

#题目2：分级填色地图
#模拟世界各国GDP数据
countries = ["China", "United States", "Japan", "Germany", "India", 
             "United Kingdom", "France", "Brazil", "Italy", "Canada"]
gdp_values = [18000, 26000, 4200, 4500, 3800, 3200, 3000, 2100, 2200, 2000]
df_gdp = pd.DataFrame({
    "country": countries, 
    "gdp_billion": gdp_values
    })

# fig = px.choropleth(gapminder, locations="iso_alpha", 
#                     color="gdpPercap", hover_name="country", 
#                     color_continuous_scale="Viridis_r", 
#                     hover_data=["continent", "year", "pop"], 
#                     title="全球GDP数据")

# fig = px.choropleth(df_gdp, locations="country", locationmode="country names", 
#                     color="gdp_billion", hover_name="country", 
#                     color_continuous_scale="Viridis_r", 
#                     title="全球GDP数据")

# fig.show()


#第五部分：综合项目与阶段复习
#综合项目：零售销售数据可视化分析报告
#项目需求：基于模拟零售销售数据，完成完整的可视化分析，包含核心指标、趋势、品类、分布、关联、热力矩阵6大模块

#准备数据
np.random.seed(2026)
dates = pd.date_range("2026-01-01", "2026-06-30", freq="D")
categories = ["食品", "服装", "家电", "日用品", "美妆"]
regions = ["华东", "华南", "华北", "西南", "华中"]

#生成销售明细数据
sales_data = []
for date in dates:
    for region in regions:
        for category in categories:
            sales = np.random.randint(500, 5000)            #销售额
            orders = np.random.randint(20, 200)             #订单量
            profit = sales * np.random.uniform(0.15, 0.35)  #利润[0.15, 0.35)
            sales_data.append([date, region, category, sales, orders, profit])
df_sales = pd.DataFrame(sales_data, columns=["日期", "地区", "品类", "销售额", "订单量", "利润"])
# print(df_sales.head())

#开始
#===== 1.核心指标 =====
total_sales = df_sales["销售额"].sum()
total_orders = df_sales["订单量"].sum()
avg_price = total_sales/total_orders
month_growth = 0.085    #模拟环比数据

# print(f"总销售额：{total_sales:,d}元")
# print(f"总订单量：{total_orders:,}单")
# print(f"平均客单价：{avg_price:,.2f}元")
# print(f"月度环比增长率：{month_growth*100:.1f}%")

#===== 2.月度销售趋势 =====
# monthly_sales = df_sales.groupby(df_sales["日期"].dt.to_period("M"))["销售额"].sum().reset_index()
monthly_sales = df_sales.set_index("日期")["销售额"].resample("MS").sum().reset_index()
# monthly_sales["日期"] = monthly_sales["日期"].astype(str)
# monthly_sales["日期"] = monthly_sales["日期"].dt.strftime("%Y-%m-%d")
# print(monthly_sales.dtypes)

#画图
# fig = px.line(monthly_sales, x="日期", y="销售额", 
#               title="2026年上半年月度销售额趋势",
#               markers=True, text="销售额")
# fig.update_traces(texttemplate="%{text:,.0f}", textposition="top center")
# fig.show()

#===== 3.品类销售分析 =====
cate_sales = df_sales.groupby("品类")["销售额"].sum().reset_index()
cate_sales_sorted = cate_sales.sort_values("销售额", ascending=False)
# print(cate_sales)

# fig1 = px.pie(cate_sales, names="品类", values="销售额", hole=0.3, 
#               title="各品类销售额占比")
# fig1.update_layout(template="plotly_white")
# fig1.show()

# fig2 = px.bar(cate_sales_sorted, x="品类", y="销售额", text_auto=True, 
#               title="各品类销售额占比")
# fig2.update_layout(template="plotly_white")
# fig2.show()

#===== 4.分布分析 =====
# daily_sales = df_sales.groupby("日期")["销售额"].sum().reset_index()
# fig = px.histogram(daily_sales, x="销售额", nbins=20, marginal="box",  
#                    title="日销售额分布分析")
# fig.show()

# region_box = df_sales.groupby(["日期","地区"])["销售额"].sum().reset_index()
# fig = px.box(region_box, x="地区", y="销售额",
#              title="各地区日销售额分布箱线图")
# fig.show()

#===== 5.关联分析 =====
# fig = px.scatter(df_sales, x="销售额", y="利润", color="品类", 
#                  color_continuous_scale="Blues",
#                  trendline="ols", title="销售额与利润的关系")
# fig.update_layout(template="plotly_white")
# fig.show()

#===== 6.地区 品类的热力矩阵 =====
pivot_sales = df_sales.pivot_table(index="地区", columns="品类", values="销售额", aggfunc="sum")
# plt.figure(figsize=(16,8))
# sns.heatmap(pivot_sales, annot=True, fmt=",.0f", cmap="Blues", linewidths=0.5)
# plt.title("各地区分品类销售额热力图")
# plt.tight_layout()
# plt.show()

# print(pivot_sales.head())
# fig = px.density_heatmap(pivot_sales, color_continuous_scale="Viridis")
# fig.show()

# print(df_sales.head())
# plt.figure(figsize=(10,8))
# sns.barplot(df_sales.groupby("日期")["销售额"].sum().reset_index().head(), x="日期", y="销售额")
# plt.title("seaborn画柱状图")
# plt.tight_layout()
# plt.show()
