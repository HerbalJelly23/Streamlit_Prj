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
    st.markdown('***')
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
    st.markdown('***')
    chart_data1 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve1.csv', usecols=[1, 2, 3]))
    show1 = st.checkbox(
        "Here is the first picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A1-1")
    if show1:
        st.line_chart(chart_data1)
    if st.checkbox('Show dataframe of A1-1', key='1'):  # 增加交互，可查询数据
        chart_data1

    # A4-1的香农曲线
    st.markdown('***')
    chart_data2 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve2.csv', usecols=[1, 2, 3]))
    show2 = st.checkbox(
        "Here is the second picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A4-1")
    if show2:
        st.line_chart(chart_data2)
    if st.checkbox('Show dataframe of A4-1', key='2'):
        chart_data2

    # A9-Z的香农曲线
    st.markdown('***')
    chart_data3 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve3.csv', usecols=[1, 2, 3]))
    show3 = st.checkbox(
        "Here is the third picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A9-Z")
    if show3:
        st.line_chart(chart_data3)
    if st.checkbox('Show dataframe of A9-Z', key='3'):
        chart_data3

    # A11的香农曲线
    st.markdown('***')
    chart_data4 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve4.csv', usecols=[1, 2, 3]))
    show4 = st.checkbox(
        "Here is the fourth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A11")
    if show4:
        st.line_chart(chart_data4)
    if st.checkbox('Show dataframe of A11', key='4'):
        chart_data4

    # A15的香农曲线
    st.markdown('***')
    chart_data5 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve5.csv', usecols=[1, 2, 3]))
    show5 = st.checkbox(
        "Here is the fifth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A15")
    if show5:
        st.line_chart(chart_data5)
    if st.checkbox('Show dataframe of A15', key='5'):
        chart_data5

    # A18的香农曲线
    st.markdown('***')
    chart_data6 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve6.csv', usecols=[1, 2, 3]))
    show6 = st.checkbox(
        "Here is the sixth picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A18")
    if show6:
        st.line_chart(chart_data6)
    if st.checkbox('Show dataframe of A18', key='6'):
        chart_data6

    # A21的香农曲线
    st.markdown('***')
    chart_data7 = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/shannon curve7.csv', usecols=[1, 2, 3]))
    show7 = st.checkbox(
        "Here is the seventh picture of shannon wiener curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A21")
    if show7:
        st.line_chart(chart_data7)
    if st.checkbox('Show dataframe of A21', key='7'):
        chart_data7
# 制作图表，并说明这是稀释性曲线，用于评估生物样本容量是否充足
st.markdown('***')
st.subheader(':red[Rarefaction Curve]')
with st.expander('Rarefaction Curve', expanded=1):
    st.markdown('***')
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
    st.markdown('***')
    chart_data1a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve1.csv', usecols=[1, 2, 3]))
    show1a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A1-1")
    if show1a:
        st.line_chart(chart_data1a)
    if st.checkbox('Show dataframe of A1-1', key='1a'):  # 增加交互，可查询数据
        chart_data1a

    # A4-1的稀释性曲线
    st.markdown('***')
    chart_data2a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve2.csv', usecols=[1, 2, 3]))
    show2a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A4-1")
    if show2a:
        st.line_chart(chart_data2a)
    if st.checkbox('Show dataframe of A4-1', key='2a'):  # 增加交互，可查询数据
        chart_data2a

    # A9-Z的稀释性曲线
    st.markdown('***')
    chart_data3a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve3.csv', usecols=[1, 2, 3]))
    show3a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A9-Z")
    if show3a:
        st.line_chart(chart_data3a)
    if st.checkbox('Show dataframe of A9-Z', key='3a'):  # 增加交互，可查询数据
        chart_data3a

    # A11的稀释性曲线
    st.markdown('***')
    chart_data4a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve4.csv', usecols=[1, 2, 3]))
    show4a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A11")
    if show4a:
        st.line_chart(chart_data4a)
    if st.checkbox('Show dataframe of A11', key='4a'):  # 增加交互，可查询数据
        chart_data4a

    # A15的稀释性曲线
    st.markdown('***')
    chart_data5a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve5.csv', usecols=[1, 2, 3]))
    show5a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A15")
    if show5a:
        st.line_chart(chart_data5a)
    if st.checkbox('Show dataframe of A15', key='5a'):  # 增加交互，可查询数据
        chart_data5a

    # A18的稀释性曲线
    st.markdown('***')
    chart_data6a = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rarefaction curve6.csv', usecols=[1, 2, 3]))
    show6a = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the sample A18")
    if show6a:
        st.line_chart(chart_data6a)
    if st.checkbox('Show dataframe of A18', key='6a'):  # 增加交互，可查询数据
        chart_data6a


    # A23的稀释性曲线
    st.markdown('***')
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
    st.markdown('***')
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

    st.markdown('***')
    chart_datara = pd.DataFrame(
        data=pd.read_csv(f'{os.path.dirname(__file__)}/rank abundance curve1.csv', usecols=[0, 1, 2]))
    showra = st.checkbox(
        "Here is the first picture of rarefaction curve,which is used to evaluate whether the sample size is sufficient.And it is referred to the samples")
    if showra:
        st.line_chart(chart_datara)
    if st.checkbox('Show dataframe of ', key='8a'):  # 增加交互，可查询数据
        chart_datara

# 绘制三个水文站站点在地图中的位置，三个站点分别为横山、竹银、白蕉
st.markdown('***')
st.subheader(':red[the position of HengShan hydrologic station]')
with st.expander('the position of HengShan hydrologic station', expanded=1):
    st.markdown('***')
    chart_datahs = pd.read_csv(f'{os.path.dirname(__file__)}/HenShan.csv')
    drawhs = st.checkbox("click here to check the position of HengShan hydrologic station", key='hs')
    if drawhs:
        st.map(chart_datahs)
    st.markdown('***')
    chart_datazy = pd.read_csv(f'{os.path.dirname(__file__)}/ZhuYin.csv')
    drawzy = st.checkbox("click here to check the position of ZhuYin hydrologic station", key='zy')
    if drawzy:
        st.map(chart_datazy)
    st.markdown('***')
    chart_databj = pd.read_csv(f'{os.path.dirname(__file__)}/BaiJiao.csv')
    drawbj = st.checkbox("click here to check the position of BaiJiao hydrologic station", key='bj')
    if drawbj:
        st.map(chart_databj)
#作一点没有意义的颜文字和emoji，尝试一下丰富画面
st.markdown('***')
st.subheader(':red[Here are some emojis and a printed picture]')
with st.expander('Here are some emojis and a printed picture', expanded=1):
    st.markdown('***')
    painting = st.checkbox("click here to show the emojis and picture", key='dr')
    if painting:
        st.markdown('***')
        st.write("Here are some emojis and a printed picture")
        st.caption(':sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses::sunglasses:')
        st.text("&&&&&&&&&&&&／＞　　フ&&&")
        st.text("&&&&&&&&&&&|  _　 _ | &")
        st.text("&&&&&&&&&&／` ミ＿xノ&&&")
        st.text("&&&&&&&&/　　　 　 |&&&&")
        st.text("&&&&&&&/　 ヽ　　 ﾉ&&&&&")
        st.text("&&&&&&│　　|　|　|&&&&&&")
        st.text("&&／￣|　　 |　|　|&&&&&&")
        st.text("&&| (￣ヽ＿_ヽ_)__)&&&&&")
        st.text("&&＼二つ&&&&&&&&&&&&&&&&")
        st.markdown('***')
st.title("Thx 4 ur reading.Hope that these info and pictures can be of use to u readers")
st.write(":red[Streamlit] is an awesome new tool that helps to solve the problems quickly")
