import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="珠江入海口水文站水样eDNA数据分析",  # 页面标题
    page_icon="🌊",  # icon
    layout='centered',  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)


# 设置网页标题
st.title('Here Are Some Info About Flow-ecology Relationship')
st.caption('This APP is provided with technical support by :blue[怕挂科的我，把Python能力点满就对了]')

st.markdown('***')
st.subheader(':red[Shannon Wiener Curve]')
with st.expander('Shannon Wiener Curve', expanded=1):
    # 制作图表，并说明这是香农系数图，用于评估生物样本容量是否充足
    st.write('')
    st.write('')
    st.write('')
    st.write("Here are the pictures of shannon wiener curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of shannon wiener curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of shannon wiener curve and all of them refer to the 7 samples")
    st.write("the important thing should be told 3 times")
    st.write('')
    st.write('')
    st.write('')

    # A1-1的香农曲线
    chart_data1 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve1.csv', usecols=[1, 2, 3]))
    show1 = st.checkbox(
        "Here is the first picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A1-1")
    if show1:
        st.line_chart(chart_data1)
    if st.checkbox('Show dataframe of A1-1', key='1'):  # 增加交互，可查询数据
        chart_data1

    # A4-1的香农曲线
    chart_data2 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve2.csv', usecols=[1, 2, 3]))
    show2 = st.checkbox(
        "Here is the second picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A4-1")
    if show2:
        st.line_chart(chart_data2)
    if st.checkbox('Show dataframe of A4-1', key='2'):
        chart_data2

    # A9-Z的香农曲线
    chart_data3 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve3.csv', usecols=[1, 2, 3]))
    show3 = st.checkbox(
        "Here is the third picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A9-Z")
    if show3:
        st.line_chart(chart_data3)
    if st.checkbox('Show dataframe of A9-Z', key='3'):
        chart_data3

    # A11的香农曲线
    chart_data4 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve4.csv', usecols=[1, 2, 3]))
    show4 = st.checkbox(
        "Here is the fourth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A11")
    if show4:
        st.line_chart(chart_data4)
    if st.checkbox('Show dataframe of A11', key='4'):
        chart_data4

    # A15的香农曲线
    chart_data5 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve5.csv', usecols=[1, 2, 3]))
    show5 = st.checkbox(
        "Here is the fifth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A15")
    if show5:
        st.line_chart(chart_data5)
    if st.checkbox('Show dataframe of A15', key='5'):
        chart_data5

    # A18的香农曲线
    chart_data6 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve6.csv', usecols=[1, 2, 3]))
    show6 = st.checkbox(
        "Here is the sixth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A18")
    if show6:
        st.line_chart(chart_data6)
    if st.checkbox('Show dataframe of A18', key='6'):
        chart_data6

    # A21的香农曲线
    chart_data7 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve7.csv', usecols=[1, 2, 3]))
    show7 = st.checkbox(
        "Here is the seventh picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A21")
    if show7:
        st.line_chart(chart_data7)
    if st.checkbox('Show dataframe of A21', key='7'):
        chart_data7

st.markdown('***')
st.subheader(':red[Rarefaction Curve]')
with st.expander('Rarefaction Curve', expanded=1):
    # 设置7个样本的稀释性曲线（Rarefaction curve）
    st.write('')
    st.write('')
    st.write('')
    st.write("Here are the pictures of Rarefaction curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of Rarefaction curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of Rarefaction curve and all of them refer to the 7 samples")
    st.write("the important thing should be told 3 times")
    st.write('')
    st.write('')
    st.write('')

    # A1-1的稀释性曲线
    chart_data1a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve1.csv', usecols=[1, 2, 3]))
    show1a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A1-1")
    if show1a:
        st.line_chart(chart_data1a)
    if st.checkbox('Show dataframe of A1-1', key='1a'):  # 增加交互，可查询数据
        chart_data1a

    # A4-1的稀释性曲线
    chart_data2a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve2.csv', usecols=[1, 2, 3]))
    show2a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A4-1")
    if show2a:
        st.line_chart(chart_data2a)
    if st.checkbox('Show dataframe of A4-1', key='2a'):  # 增加交互，可查询数据
        chart_data2a

    # A9-Z的稀释性曲线
    chart_data3a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve3.csv', usecols=[1, 2, 3]))
    show3a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A9-Z")
    if show3a:
        st.line_chart(chart_data3a)
    if st.checkbox('Show dataframe of A9-Z', key='3a'):  # 增加交互，可查询数据
        chart_data3a

    # A11的稀释性曲线
    chart_data4a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve4.csv', usecols=[1, 2, 3]))
    show4a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A11")
    if show4a:
        st.line_chart(chart_data4a)
    if st.checkbox('Show dataframe of A11', key='4a'):  # 增加交互，可查询数据
        chart_data4a

    # A15的稀释性曲线
    chart_data5a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve5.csv', usecols=[1, 2, 3]))
    show5a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A15")
    if show5a:
        st.line_chart(chart_data5a)
    if st.checkbox('Show dataframe of A15', key='5a'):  # 增加交互，可查询数据
        chart_data5a

    # A18的稀释性曲线
    chart_data6a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve6.csv', usecols=[1, 2, 3]))
    show6a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A18")
    if show6a:
        st.line_chart(chart_data6a)
    if st.checkbox('Show dataframe of A18', key='6a'):  # 增加交互，可查询数据
        chart_data6a

    # A23的稀释性曲线
    chart_data7a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve7.csv', usecols=[1, 2, 3]))
    show7a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A23")
    if show7a:
        st.line_chart(chart_data7a)
    if st.checkbox('Show dataframe of A23', key='7a'):  # 增加交互，可查询数据
        chart_data7a

st.markdown('***')
st.subheader(':red[Rank Abundance Curve]')
with st.expander('Rank Abundance Curve', expanded=1):
    st.write('')
    st.write('')
    st.write('')
    st.write("Here are the pictures of rank abundance curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of rank abundance curve and all of them refer to the 7 samples")
    st.write("Here are the pictures of rank abundance curve and all of them refer to the 7 samples")
    st.write("the important thing should be told 3 times")
    st.write('')
    st.write('')
    st.write('')

    chart_datara = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rank abundance curve1.csv', usecols=[1, 2, 3]))
    showra = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the samples")
    if showra:
        st.line_chart(chart_datara)
    if st.checkbox('Show dataframe of ', key='8a'):  # 增加交互，可查询数据
        chart_datara

    # 作出三个取样点的地图，并且随机分布数个取样点作为随机取样的模拟样例说明，三个地点分别是竹银、横山、白蕉。
    chart_datazy = pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [22.22, 113.11],
        columns=['lat', 'lon'])
    st.map(chart_datazy)

st.markdown('***')
st.write(":red[streamlit] is an awesome new tool that helps to solve the problems quickly")
