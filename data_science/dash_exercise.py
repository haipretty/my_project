import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output, callback

# 【Dash】
#准备数据
app = Dash(__name__)        #如果不传__name__，Dash内部用的Flask就不知道去哪找静态文件
df = px.data.gapminder()    #全球发展数据

app.layout = html.Div([                 #app布局：html div元素
    html.H1("全球GDP仪表盘"),            #第一行：H1标题
    dcc.Dropdown(                       #第二行：下拉框
        id="year-dropdown",
        options=[{"label":str(y), "value":y} for y in df["year"].unique()],     #下拉框选项
        value=2007                                                              #默认选中2007
    ),
    dcc.Graph(id="gdp-chart")           #第三行：图表
])

@callback(                              #Dash装饰器
    Output("gdp-chart", "figure"),      #将函数返回值，传入id="year-dropdown"控件的figure值
    Input("year-dropdown", "value")     #将id="year-dropdown"控件的value值，传入函数
)
def update_chart(select_year):
    df_filtered = df[df["year"] == select_year]
    return px.scatter(df_filtered, x="gdpPercap", y="lifeExp",
                      color="continent", size="pop",
                      hover_name="country", log_x=True, 
                      title=f"{select_year}年")

if __name__ == "__main__":  #__name__是Python的内置变量，主程序运行时="__main__"
    app.run(debug=True)     #修改代码后页面自动刷新，生产环境设为False

#启动
#浏览器输入：http://localhost:8050