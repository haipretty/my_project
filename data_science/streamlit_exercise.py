import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st

# 【streamlit】
#准备数据
np.random.seed(2026)
df = pd.DataFrame({
    "地区": np.random.choice(["黑龙江", "山东", "辽宁", "北京"], 12),
    "月份": [f"{i}月" for i in range(1, 13)],
    "销售额": np.random.randint(100, 1000, 12)
})

#开始画图
#侧边栏筛选
region = st.sidebar.selectbox("选择地区", df['地区'].unique())
df_filtered = df[df["地区"] == region]

#body第一行：展示标题
st.title("销售数据仪表盘")

#body第二行：展示图表
fig = px.bar(df_filtered, x="月份", y="销售额", text_auto=True)
st.plotly_chart(fig, width="content")

#body第三行：展示数据表格
st.dataframe(df_filtered)

#body第四行：展示指标卡片
st.metric("总销售额", f"{df_filtered["销售额"].sum():,.0f}")

#命令行启动
#streamlit run d:/workspace/python/data_science/plotly_exercise.py [ARGUMENTS]