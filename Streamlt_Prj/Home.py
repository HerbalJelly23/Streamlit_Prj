import pandas as pd
import math
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.font_manager as fm
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="双参数控制的DDS方法——参数生成APP",    #页面标题
    page_icon=":wheelchair:",        #icon
    layout="wide",                #页面布局
    initial_sidebar_state="auto"  #侧边栏
)


os.chdir(os.path.dirname(__file__))

st.title('双参数控制的DDS方法——参数生成APP')
st.caption('本APP由:blue[怕挂科的我，把Python能力点满就对了]提供技术支持')
st.header('双参数控制的DDS方法简要介绍')
with st.expander('点击以展开双参数控制的DDS方法简要介绍'):
    st.subheader(':red[1.]基本DDS技术原理介绍')
    st.write(
        'DDS技术是指直接数字合成技术（Direct Digital Synthesis），它是一种基于数字逻辑和数字信号处理技术的直接频率合成技术，它可以通过数字信号处理器（DSP）或者可编程逻辑器件（FPGA）等数字电路实现。相位控制字可以控制初相。频率控制字控制每次相位的步进，进而控制产生信号的频率。')
    DDS_image = Image.open('DDS_basic.png')
    st.image(DDS_image, caption='常见DDS信号发生器原理框图')
    st.subheader(':red[2.]双参数控制的DDS方法改进原理')
    st.markdown('***')

    col1, col2 = st.columns(2)
    col1.markdown('##### 改进原因：')
    col1.markdown('- 基本的DDS方法仅用单一参数对频率进行控制，频率分辨率较低')
    col1.markdown('- 基本的DDS方法难以对波形的失真度进行调控')
    col1.markdown('- 基本的DDS方法应对多种波形数据不够灵活')
    col2.markdown('##### 改进方法：')
    col2.markdown('- 使用双参数对频率进行控制:red[存储步进值]、:red[存储计数次数]')
    col2.markdown('- 设计专用于双参数控制的DDS方法的参数生成APP (如该APP)')
    st.markdown('***')
    st.markdown('##### 改进原理：')
    st.markdown(
        '每当计数器计满:red[存储计数次数]后，波形地址进行步进，步进值为:red[存储步进值]。当波形地址步进满后，波形地址归零，重新步进，波形数据不断循环变化，实现波形的发生。')
    st.markdown('***')
    st.markdown('##### 双参数控制的DDS方法原理流程：')
    DDS_image = Image.open('DDS_improved.png')
    st.image(DDS_image, caption='双参数控制的DDS信号发生器原理框图')

st.header('参数生成APP使用说明')
with st.expander('点击以展开参数生成APP使用说明', expanded=1):
    st.subheader(':red[1.]数据生成APP，使用说明：')
    st.write(':red[(1)]根据[:red[Generate]](https://herbaljelly-dds-generator.streamlit.app/Generate)页面的操作步骤提示，分别进行以下步骤确定:red[目录选取]、设定:red[数据深度]、设定:red[时钟频率]、导入:red[频率数据]、设定:red[波形最低分辨率]')
    st.write(':red[(2)]完成波形质量相关参数设定中的前置操作后，根据您的需求设定:red[加载数据分析文件]、:red[生成数据文件]、:red[生成分析图像]。这些步骤都是允许客制化的，您也可以不做操作，:red[保持默认]即可')
    st.write(':red[(3)]在完成所有相关参数的设定后，您应该根据:red[侧边栏]显示的内容反复确认您的设定是否正确，并在确认:red[文件生成路径]和您需要生成的:red[参数文件]后点击:red[**一键生成**]')
    st.write(':red[(4)]在看到庆祝的气球放出后，证明生成过程已全部完成，届时您可以根据提示，移步至:red[Analysis]界面查看数据分析图像，并查看相应数据')
    st.write(':red[(5)]在[:red[Analysis]](https://herbaljelly-dds-generator.streamlit.app/Analysis)界面，您可以再次对图像展示的内容进行设定，该操作并:red[不会对已生成的数据或图像造成影响]')
    st.markdown('***')
    st.subheader(':red[2.]数据生成APP，注意事项：')
    st.write(':red[(1)]程序中出现的问题可能并未被正确排除，欢迎您在使用时进行指出')
    st.write(':red[(2)]如遇图像或数据无法加载，请检查您的:red[文件路径]')
    st.write(':red[(3)]该程序完全开放使用，欢迎您前来本人的[:blue[GitHub]](https://github.com/HerbalJelly23)交流')
    st.write(':red[(4)]本APP由:blue[怕挂科的我，把Python能力点满就对了]提供技术支持，感谢您的使用')
