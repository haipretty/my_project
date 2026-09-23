import plotly.express as px
import pandas as pd
import numpy as np


# 【plotly】
#准备数据
np.random.seed(2026)
dates = pd.date_range("2026-06-01", "2026-06-30", freq="D")
regions = ["华南", "华北", "华东", "华西"]
cities = ["深圳", "上海", "北京", "陕西"]
categories = ["电子", "母婴", "衣服", "饰品"]
sales_data = []
for date in dates:
    for region in regions:
        for city in cities:
            for category in categories:
                sales = np.random.randint(100, 1000)
                sales_data.append([date, region, city, category, sales])
df = pd.DataFrame(sales_data, columns=["日期", "地区", "城市", "品类", "销售额"])

# df = pd.DataFrame({
#     "日期": date,
#     "地区": np.random.choice(["华南", "华北", "华东", "华西"], 30),
#     "城市": np.random.choice(["深圳", "上海", "北京", "陕西"], 30),
#     "品类": np.random.choice(["电子", "母婴", "衣服", "饰品"], 30),
#     "销售额": np.random.randint(100, 1000, 30),

# })

df_person = pd.DataFrame({
    "姓名": ["赵1", "钱2", "孙3", "李4"],
    "性别": ["男", "女", "男", "女"],
    "年龄": [18, 19 ,20, 21],
    "身高": [150, 160, 170, 180],
    "体重": [50, 60, 70, 80]

})

# # 折线图
fig = px.line(df, x='日期', y='销售额', color='地区', line_group='品类')    #按"品类"分组画线

# # 散点图
# fig = px.scatter(df_person, x='身高', y='体重', color='性别', size='年龄',
#                  hover_data=['姓名'], title='身高体重分布')

# # 柱状图
# fig = px.bar(df, x='日期', y='销售额', color='品类', barmode='group')

# # 直方图
# fig = px.histogram(df, x='城市', nbins=4, marginal='rug')

# # 饼图 / 旭日图
# fig = px.pie(df, values='销售额', names='地区', hole=0.3)
# fig = px.sunburst(df, path=['地区', '城市'], values='销售额')

# # 箱线图 / 小提琴图
# fig = px.box(df, x='品类', y='销售额', color='品类')
# fig = px.violin(df, x='品类', y='销售额', box=True)

# # 调整参数
# fig.update_traces(pull=[0, 0.1, 0, 0])	# 调整标记大小
# fig.update_layout(					# 修改布局
#     title='图表标题',
#     xaxis_title='X轴',
#     yaxis_title='Y轴',
#     hovermode='x unified',     		# 悬停时统一显示
#     template='plotly_white',       	# 白色主题
#     width=800, height=500
# )
# fig.write_html('chart.html')

# # 显示
fig.show()


# 【地图可视化】
#准备数据
df_2007 = px.data.gapminder().query("year==2007")

df_line = pd.DataFrame({
    'route': ['Flight1', 'Flight1', 'Flight1', 'Flight1'],
    'city': ['Beijing', 'Shanghai', 'Tokyo', 'New York'],
    'lat': [39.9, 31.2, 35.7, 40.7],
    'lon': [116.4, 121.5, 139.7, 174.0],
    'pop': [2000, 1000, 300, 400]
})

np.random.seed(42)
df_random = pd.DataFrame({
    'lat': np.random.normal(39.9, 0.1, 500),   # 北京附近
    'lon': np.random.normal(116.4, 0.1, 500),
    'value': np.random.randint(10, 100, 500)
})


#choropleth等值区域图
# fig = px.choropleth(df_2007, locations='iso_alpha', color='gdpPercap',
#                     hover_name="country", color_continuous_scale="Viridis",
#                     title="2007年全球人均GDP")

#连线地图
# fig = px.line_geo(df_line, lat='lat', lon='lon', color='route', 
#                   hover_name='city',
#                   projection='orthographic')        # 地球仪效果

#散点地图
# fig = px.scatter_geo(df_line, lat="lat", lon="lon", 
#                      color="city", size="pop",
#                      hover_name="city", projection="natural earth")

#密度地图
# fig = px.density_map(df_random, lat="lat", lon="lon", z="value",
#                         radius=10, zoom=8, 
#                         center=dict(lat=39.9, lon=116.4), 
#                         map_style="carto-darkmatter")

#显示
# fig.show()


