import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import streamlit as st
import time

st.set_page_config(
    page_title="双参数控制的DDS方法——参数生成APP",    #页面标题
    page_icon=":wheelchair:",        #icon
    layout="wide",                #页面布局
    initial_sidebar_state="auto"  #侧边栏
)

st.title('查看分析图像')

# 切换目录
current_path = 'D:\\DDS_param_generator'
if os.path.exists(current_path):
    os.chdir(current_path)
else:
    os.mkdir(current_path)
    os.chdir(current_path)
data_dir_name = st.text_input('请填写您的数据文件夹名称：', 'DDS_dataset')
col1, col2 = st.columns(2)
col1.write('您可以为您的文件夹添加:red[后缀]，以便于区分生成的不同数据集：')
if col2.checkbox('添加日期后缀', value=1):
    date = time.strftime('_%Y-%m-%d', time.localtime())
    data_dir_name = data_dir_name + date
if col2.checkbox('添加时间后缀'):
    date = time.strftime('_%H-%M-%S', time.localtime())
    data_dir_name = data_dir_name + date
data_dir_path = f'{current_path}\{data_dir_name}'
st.write(f'您当前处于该数据目录中:red[{data_dir_path}]')
# st.markdown('***')
# 切换目录
if os.path.exists(data_dir_path):
    os.chdir(data_dir_path)
else:
    os.mkdir(data_dir_path)
    os.chdir(data_dir_path)

# 读取频率数据
dataset_freq = pd.read_csv(f'{os.path.dirname(__file__)}/频率表格_Python分析.CSV')
wave_freq_out = [].copy()
for i in range(12709):
    wave_freq_out.append(float(dataset_freq.iat[i, 0]))

# 读取频率误差及失真分析数据
frequency_error = []
frequency_relative_error = []
distortion_analysis_list = []
addr_step_list = []
step_count_list = []
with open('distortion_analysis.coe', 'r') as distortion_analysis_file:
    distortion_analysis_file.readline()
    distortion_analysis_file.readline()
    for i in range(12709):
        line_content = distortion_analysis_file.readline()
        distortion_analysis_list.append(float(line_content[0:len(line_content) - 2]))
    distortion_analysis_file.close()
with open('frequency_error.coe', 'r') as frequency_error_file:
    frequency_error_file.readline()
    frequency_error_file.readline()
    for i in range(12709):
        line_content = frequency_error_file.readline()
        frequency_error.append(float(line_content[0:len(line_content) - 2]))
        frequency_relative_error.append(float(line_content[0:len(line_content) - 2]) / wave_freq_out[i])
    frequency_error_file.close()
with open('addr_step.coe', 'r') as addr_step_file:
    addr_step_file.readline()
    addr_step_file.readline()
    for i in range(12709):
        line_content = addr_step_file.readline()
        if line_content[0:len(line_content) - 2] == '':
            addr_step_list.append(float(1))
        else:
            addr_step_list.append(float(line_content[0:len(line_content) - 2]))
    addr_step_file.close()
with open('step_count.coe', 'r') as step_count_file:
    step_count_file.readline()
    step_count_file.readline()
    for i in range(12709):
        line_content = step_count_file.readline()
        if line_content[0:len(line_content) - 2] == '':
            step_count_list.append(float(1))
        else:
            step_count_list.append(float(line_content[0:len(line_content) - 2]))
    step_count_file.close()
with st.sidebar:
    st.subheader('双参数显示')
    col1, col2 = st.columns(2)
    # col1.write('地址步进值参数显示：')
    if col1.checkbox('地址步进值', value=1):
        col1.table(addr_step_list)
    # col2.write('步进计数值参数显示：')
    if col2.checkbox('步进计数值', value=1):
        col2.table(step_count_list)
# st.markdown('***')

# 显示图像
tab_1, tab_2, tab_3 = st.tabs(["频率失真误差", "频率失真相对误差", "波形失真度分析"])
freq_range_dict = {'0Hz': 0, '0.1Hz': 0, '1Hz': 9, '10Hz': 18, '100Hz': 108, '1kHz': 1008, '10kHz': 1908,
                   '100kHz': 10908, '1MHz': 11808, '10MHz': 12708}
with tab_1:
    st.subheader('频率失真误差')
    col2, col1 = st.columns(2)
    start_freq_1, end_freq_1 = col1.select_slider(
        '请选择波形频率范围',
        options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
        value=('0Hz', '10MHz'), key='slider_tab_1')
    st.write('您选定的频率范围为', start_freq_1, '~', end_freq_1)
    data_range_start = freq_range_dict[start_freq_1]
    data_range_end = freq_range_dict[end_freq_1] + 1
    chart_data_1 = pd.DataFrame(
        frequency_error[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
    )
    pic_type_select_1 = col2.radio(
        "选择您需要的图形样式：",
        ('面积图', '折线图', '生成图像样式'), index=0, key='pic_type_select_1')
    if pic_type_select_1 == '面积图':
        st.area_chart(chart_data_1)
    elif pic_type_select_1 == '折线图':
        st.line_chart(chart_data_1)
    elif pic_type_select_1 == '生成图像样式':
        plt.rcParams.update({"font.size": 10})
        py_type_pic, my_pic = plt.subplots()
        # plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
        my_pic.scatter(wave_freq_out[data_range_start:data_range_end],
                       frequency_error[data_range_start:data_range_end])
        my_pic.grid()
        st.pyplot(py_type_pic)
    check_1 = st.checkbox('显示频率失真误差数据列表？')
    if check_1:
        st.table(chart_data_1.T)
with tab_2:
    st.subheader('频率失真相对误差')
    col2, col1 = st.columns(2)
    start_freq_2, end_freq_2 = col1.select_slider(
        '请选择波形频率范围',
        options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
        value=('0Hz', '10MHz'), key='slider_tab_2')
    st.write('您选定的频率范围为', start_freq_2, '~', end_freq_2)
    data_range_start = freq_range_dict[start_freq_2]
    data_range_end = freq_range_dict[end_freq_2] + 1
    chart_data_2 = pd.DataFrame(
        frequency_relative_error[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
    )
    pic_type_select_2 = col2.radio(
        "选择您需要的图形样式：",
        ('面积图', '折线图', '生成图像样式'), index=0, key='pic_type_select_2')
    if pic_type_select_2 == '面积图':
        st.area_chart(chart_data_2)
    elif pic_type_select_2 == '折线图':
        st.line_chart(chart_data_2)
    elif pic_type_select_2 == '生成图像样式':
        plt.rcParams.update({"font.size": 10})
        py_type_pic, my_pic = plt.subplots()
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
        my_pic.scatter(wave_freq_out[data_range_start:data_range_end],
                       frequency_relative_error[data_range_start:data_range_end])
        my_pic.grid()
        st.pyplot(py_type_pic)
    check_2 = st.checkbox('显示频率失真相对误差数据列表？')
    if check_2:
        st.table(chart_data_2.T)
with tab_3:
    st.subheader('波形失真度分析')
    col2, col1 = st.columns(2)
    start_freq_3, end_freq_3 = col1.select_slider(
        '请选择波形频率范围',
        options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
        value=('0Hz', '10MHz'), key='slider_tab_3')
    st.write('您选定的频率范围为', start_freq_3, '~', end_freq_3)
    data_range_start = freq_range_dict[start_freq_3]
    data_range_end = freq_range_dict[end_freq_3] + 1
    chart_data_3 = pd.DataFrame(
        distortion_analysis_list[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
    )
    pic_type_select_3 = col2.radio(
        "选择您需要的图形样式：",
        ('面积图', '折线图', '生成图像样式'), index=0, key='pic_type_select_3')
    if pic_type_select_3 == '面积图':
        st.area_chart(chart_data_3)
    elif pic_type_select_3 == '折线图':
        st.line_chart(chart_data_3)
    elif pic_type_select_3 == '生成图像样式':
        plt.rcParams.update({"font.size": 10})
        py_type_pic, my_pic = plt.subplots()
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
        my_pic.scatter(wave_freq_out[data_range_start:data_range_end],
                       distortion_analysis_list[data_range_start:data_range_end])
        my_pic.grid()
        st.pyplot(py_type_pic)
    check_3 = st.checkbox('显示波形失真度分析数据列表？')
    if check_3:
        st.table(chart_data_3.T)
