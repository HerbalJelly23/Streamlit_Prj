import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="国内生产总值GDP数据可视化APP",  # 页面标题
    page_icon="💴",  # icon
    layout="centered",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)
# data_dir_path = os.path.dirname(__file__)
# data_dir_path = data_dir_path.replace('\\', '/')

# streamlit交互
# 设置网页标题
st.title('通过Streamlit展示国内生产总值GDP的相关数据')
# #展示数据
# 展示一级标题
st.header('1. 国内生产总值GDP的数据展示')
data = pd.read_csv(f'{os.path.dirname(__file__)}经济方面.csv', encoding='gb18030')
# print(data.head()) # 默认打出五行数据
st.dataframe(data)

# #展示图片（如果可以，就直接与上述过程交互，不行就直接放图片）
# 展示一级标题
st.header('2. 对获取的国内生产总值GDP相关的数据进行相关性分析')
# st.pyplot(sns.heatmap(corr))

image = Image.open(f'{os.path.dirname(__file__)}corr.jpg')
st.image(image, caption='国内生产总值GDP相关的数据进行相关性分析')
st.text('同时我们猜测，国内生产总值GDP与时间是线性相关的')

# 展示一级标题
st.header('3. 对获取的国内生产总值GDP数据使用LinearRegression、Ridge、Lasso进行预测')
# # 展示二级标题
st.subheader('3.1 使用LinearRegression进行预测')

image = Image.open(f'{os.path.dirname(__file__)}LinearRegression().jpg')
st.image(image, caption='LinearRegression')
# # 展示二级标题
st.subheader('3.2 使用Ridge进行预测')

image = Image.open(f'{os.path.dirname(__file__)}Ridge().jpg')
st.image(image, caption='Ridge')
# # 展示二级标题
st.subheader('3.3 使用Lasso进行预测')

image = Image.open(f'{os.path.dirname(__file__)}Lasso().jpg')
st.image(image, caption='Lasso')

# 展示一级标题
st.header('4. 对国内各省份生产总值GDP进行直观展示')
st.subheader('4.1 国内各省份GDP数据')
data = pd.read_csv(f'{os.path.dirname(__file__)}province.csv', encoding='utf8')
# print(data.head()) # 默认打出五行数据
st.dataframe(data)
st.subheader('4.2 国内各省份GDP数据地图')
# 用province省份作图-可以实现，但怎么样和streamlit交互-不行还是要采用streamlit本身生态


data3 = pd.read_csv('province.csv', encoding='utf8')
# print(data3)
# 处理数据
Year = '2022'
info = data3[['地区', Year]]
# print(info)
info_list = info.values.tolist()  # 将数据转换为列表-因为echarts使用的数据为列表形式
# print(info_list)
# 绘制地图
map = Map()
map.add(
    series_name='地区生产总值',
    data_pair=info_list,
    maptype='china',
    zoom=1
)

map.set_global_opts(
    title_opts=opts.TitleOpts(
        subtitle='数据来源：国家统计局',
        pos_right='center',
        pos_top='5%'
    ),
    visualmap_opts=opts.VisualMapOpts(
        max_=12900000000000,
        min_=213000000000,
        range_color=['#1E9600', '#FFF200', '#FF0000']
    )
)

tu = map.render_embed()
components.html(tu, height=600)
