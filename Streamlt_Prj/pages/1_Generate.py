import pandas as pd
import math
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

# 数据缓存
@st.cache_data
def load_data(data):
    return data


# 取得整数
def get_decimal(num):
    if (num - int(num)) >= 0.5:
        return int(num + 1)
    else:
        return int(num)


# coe文件生成函数
def generate_coe(filename, data_range):
    with open(filename + '.coe', 'w') as fid:
        text1 = 'memory_initialization_radix=10;\n'
        text2 = 'memory_initialization_vector='
        fid.write(text1 + text2)
        data_range_len = len(data_range)
        for row in range(data_range_len):
            if row == (data_range_len - 1):
                fid.write(f'\n{data_range[row]};')
            else:
                fid.write(f'\n{data_range[row]},')
        fid.close()


st.title('双参数控制的DDS方法——参数生成APP')
st.caption('本APP由:blue[怕挂科的我，把Python能力点满就对了]提供技术支持')

st.header('波形质量相关参数设定：')
# 0.目录选取
current_path = 'D:\\DDS_param_generator'
if os.path.exists(current_path):
    os.chdir(current_path)
else:
    os.mkdir(current_path)
    os.chdir(current_path)
st.subheader(':red[1.]目录选取')
st.write(f'您当前处于该目录中:red[{current_path}]')
st.write('由于技术原因，目前暂不支持选取文件夹，请将您所使用到的文件放置于该根目录中')
data_dir_name = st.text_input('请为您的数据生成文件夹命名：', 'DDS_dataset')
col1, col2 = st.columns(2)
col1.write('您可以为您的文件夹添加:red[后缀]，以便于区分生成的不同数据集：')
if col2.checkbox('添加日期后缀', value=1):
    date = time.strftime('_%Y-%m-%d', time.localtime())
    data_dir_name = data_dir_name + date
if col2.checkbox('添加时间后缀'):
    date = time.strftime('_%H-%M-%S', time.localtime())
    data_dir_name = data_dir_name + date
data_dir_path = f'{current_path}\{data_dir_name}'
st.write(f'您的数据文件夹绝对路径如下：:red[{data_dir_path}]')
st.markdown('***')

# 1.数据深度
st.subheader(':red[2.]数据深度')
st.write(f'请将数据深度设置为与您所使用的波形数据深度一致')
N_depth = int(st.number_input('设定数据深度', min_value=5, max_value=30, value=10))
st.markdown('***')

# 2.时钟频率[MHz]
st.subheader(':red[3.]时钟频率[MHz]')
st.write('请将时钟频率设置为与您所使用的DDS方法的硬件时钟频率一致')
st.write(':red[FPGA的时钟可能为其系统时钟或由PLL/MMCM控制的时钟，请在确认后进行设定]')
clk_freq = int(st.number_input('设定时钟频率[MHz]', min_value=0, max_value=5000, value=100)) * 1000_000
st.markdown('***')

# 3.频率数据导入
st.subheader(':red[4.]频率数据导入')
st.write('您可以从此处导入频率数据或使用我们为您提供的频率数据集:red[0.1Hz~10MHz]')
using_online_freq_dataset = st.checkbox('使用我们为您提供的频率数据集？', value=1)
resolution_1 = 0
resolution_2 = 0
resolution_3 = 0
if using_online_freq_dataset:
    st.subheader(':red[5.]波形最低分辨率')
    st.write('波形分辨率将对DDS方法生成波形的失真度和频率精度造成较大影响，您可以使用推荐值')
    st.write(':red[推荐值根据您的数据深度推算，为了保证波形的精度，我们强烈建议您使用推荐值]')
    with st.expander('波形最低分辨率'):
        resolution_1 = int(
            st.slider('设定频率0.1Hz~100kHz处的波形分辨率：', 2, int(2 ** N_depth / 8), int(2 ** N_depth / 32)))
        resolution_2 = int(
            st.slider('设定频率100kHz~1MHz处的波形分辨率：', 2, int(2 ** N_depth / 16), int(2 ** N_depth / 64)))
        resolution_3 = int(
            st.slider('设定频率1MHz~10MHz处的波形分辨率：', 2, int(2 ** N_depth / 32), int(2 ** N_depth / 128)))
else:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataset_freq = pd.read_csv(uploaded_file)
        st.write('请确认您的频率数据正确：')
        st.table(dataset_freq.T)
        st.success('导入成功，您可以继续后续步骤', icon="✅")
        freg_dataset_len = len(dataset_freq)

        freq_range = st.slider('设定第一个分辨率区间', 0, int(dataset_freq.iloc[freg_dataset_len - 1, 0]),
                               (int(dataset_freq.iloc[freg_dataset_len - 1, 0] / 100),
                                int(dataset_freq.iloc[freg_dataset_len - 1, 0] / 10)))

        col1, col2, col3 = st.columns(3)

        col1.write('设定您的第一个频率区间')
        resolution_1 = int(
            col1.slider(f'设定频率{dataset_freq.iloc[0, 0]}Hz~{freq_range[0]}kHz处的波形分辨率：', 2,
                        int(2 ** N_depth / 8),
                        int(2 ** N_depth / 32)))
        col2.write('设定您的第二个频率区间')
        resolution_2 = int(
            col2.slider(f'设定频率{freq_range[0]}Hz~{freq_range[1]}kHz处的波形分辨率：', 2, int(2 ** N_depth / 16),
                        int(2 ** N_depth / 64)))
        col3.write('设定您的第三个频率区间')
        resolution_3 = int(
            col3.slider(
                f'设定频率{freq_range[1]}Hz~{int(dataset_freq.iloc[freg_dataset_len - 1, 0])}kHz处的波形分辨率：', 2,
                int(2 ** N_depth / 32),
                int(2 ** N_depth / 128)))
st.markdown('***')
pic_DPI = 70
resolution_range = [resolution_1, resolution_2, resolution_3]

data_depth = int(2 ** N_depth)
wave_freq_out_calc_range = [[], [], []]
addr_step_list = []
step_count_list = []
frequency_set_list = []
frequency_abs_error_list = []
frequency_error_list = []
dif_abs_range = []
distortion_analysis_list = []

addr_step = [[], [], []]
range_float = [[], [], []]
addr_step_range = [[], [], []]
step_count_range = [[], [], []]
state = 0

frequency_error = []
frequency_relative_error = []
wave_freq_out = []
# 5.生成参数并分析
st.header('参数生成与分析')
# 读取数据分析coe文件
st.subheader(':red[1.]加载数据分析文件[可选]')
st.write('如果您有已完成分析的coe文件，可以勾选后面的选框，并选取文件进行加载，从而跳过较为耗时的数据分析过程')
using_analysis_coe = st.checkbox('我有数据分析coe文件')
if using_analysis_coe:
    uploaded_file = st.file_uploader("请选取数据分析coe文件")
st.markdown('***')

# 生成数据文件
st.subheader(':red[2.]生成数据文件')
st.write(
    '下拉选框以选择需要生成的数据文件，并点击按钮以执行生成数据文件：:red[步进值coe文件]、:red[频率计数值coe文件]、:red[频率参数coe文件]、:red[频率误差coe文件]、:red[失真度分析coe文件]')
with st.expander('生成数据文件设定'):
    generate_coe_options = st.multiselect(
        '请选择您需要生成的coe文件',
        ['地址步进值的coe文件', '频率计数值的coe文件', '频率参数coe文件', '频率误差绝对值的coe文件',
         '频率误差的coe文件',
         '失真度分析的coe文件'],
        ['地址步进值的coe文件', '频率计数值的coe文件', '频率误差的coe文件', '失真度分析的coe文件'])
    col1, col2 = st.columns(2)
    col1.write('请确认，您要生成以下数据的coe文件：')
    col1.write(':red[生成文件将会直接覆盖原有的同名文件]')
    col1.write(':red[请自行确认后再点击按钮]')
    col2.write(generate_coe_options)
st.markdown('***')

# 生成分析图像
st.subheader(':red[3.]生成分析图像')
st.write(
    '点击选框以选择生成分析图像：:red[频率失真误差]、:red[频率失真相对误差]、:red[波形失真度分析]')
with st.expander('生成分析图像设定'):
    col1, col2 = st.columns(2)
    col1.write(':red[(1)]生成图像类型选择(多选)')
    pic_type_01 = col1.checkbox('频率失真误差', value=1)
    pic_type_02 = col1.checkbox('频率失真相对误差', value=1)
    pic_type_03 = col1.checkbox('波形失真度分析', value=1)
    col1.write(':red[(2)]图像DPI设置')
    col1.slider('DPI', 1, 300, 70)
    # col2.write(':red[(3)]图像横轴范围选择')
    # range_type = col2.radio('选择横轴范围(单选)', ('0~100kHz', '0~1MHz', '0~10MHz'), index=2)
    col2.write(':red[(3)]横轴设置')
    x_axis_type = col2.checkbox('10的幂为横轴')
    freq_range_dict = {'0Hz': 0, '0.1Hz': 0, '1Hz': 9, '10Hz': 18, '100Hz': 108, '1kHz': 1008, '10kHz': 1908,
                       '100kHz': 10908, '1MHz': 11808, '10MHz': 12708}
    col2.write(':red[(4)]图像横轴范围选择')
    start_freq, end_freq = col2.select_slider(
        '请选择波形频率范围',
        options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
        value=('0Hz', '10MHz'), key='slider_tab')
    st.write('选定的频率范围', start_freq, '~', end_freq)
    data_range_start = freq_range_dict[start_freq]
    data_range_end = freq_range_dict[end_freq]

st.write(
    '点击按钮以生成波形控制参数，并自动进行分析。在分析完成后，将根据您所选择的生成数据与图像内容进行自动生成。该过程需要较多时间，请耐心等待。')
if st.button(f'一键生成'):
    # 读取频率数据
    dataset_freq = pd.read_csv(f'{os.path.dirname(__file__)}/频率表格_Python分析.CSV')
    # 更改所在目录
    if os.path.exists(data_dir_path):
        os.chdir(data_dir_path)
    else:
        os.mkdir(data_dir_path)
        os.chdir(data_dir_path)
    # 开始读条
    progress_bar_01 = st.progress(0, text="正在生成数据，请等待……")
    progress_bar_number = 0
    for i in range(3):
        addr_step[i] = int(data_depth / resolution_range[i] / 2)
        range_float[i] = int(addr_step[i] - 1)
        addr_step_range[i] = [addr_step[i] + x for x in range(-range_float[i], range_float[i] + 1)]
        for j in range(2 * range_float[i] + 1):
            step_count_range[i].append([])
            wave_freq_out_calc_range[i].append([])
    progress_i_last = 0
    for i in range(12709):
        if 0 <= i < 10908:
            state = 0
            wave_freq_out = dataset_freq.iat[i, 0]
            for j in range(2 * range_float[state] + 1):
                addr_step_range_j = addr_step_range[state][j]
                step_count_range_j = addr_step_range_j / (wave_freq_out / (clk_freq / data_depth))
                step_count_range[state][j] = int(get_decimal(step_count_range_j))
                if step_count_range[state][j] == 0:
                    step_count_range[state][j] = int(1)
            wave_freq_out_calc_range[state] = [
                clk_freq / int(data_depth / addr_step_range[state][x] + 1) / int(step_count_range[state][x])
                for x
                in
                range(2 * range_float[state] + 1)]
            dif_abs_range = [abs(x - wave_freq_out) for x in wave_freq_out_calc_range[state]]
            dif_min_index = dif_abs_range.index(min(dif_abs_range))
        elif 10908 <= i < 11808:
            state = 1
            wave_freq_out = dataset_freq.iat[i, 0]
            for j in range(2 * range_float[state] + 1):
                addr_step_range_j = addr_step_range[state][j]
                step_count_range_j = addr_step_range_j / (wave_freq_out / (clk_freq / data_depth))
                step_count_range[state][j] = int(get_decimal(step_count_range_j))
                if step_count_range[state][j] == 0:
                    step_count_range[state][j] = int(1)
            wave_freq_out_calc_range[state] = [
                clk_freq / int(data_depth / addr_step_range[state][x] + 1) / int(step_count_range[state][x])
                for x
                in
                range(2 * range_float[state] + 1)]
            dif_abs_range = [abs(x - wave_freq_out) for x in wave_freq_out_calc_range[state]]
            dif_min_index = dif_abs_range.index(min(dif_abs_range))
        else:
            state = 2
            wave_freq_out = dataset_freq.iat[i, 0]
            for j in range(2 * range_float[state] + 1):
                addr_step_range_j = addr_step_range[state][j]
                step_count_range_j = addr_step_range_j / (wave_freq_out / (clk_freq / data_depth))
                step_count_range[state][j] = int(get_decimal(step_count_range_j))
                if step_count_range[state][j] == 0:
                    step_count_range[state][j] = int(1)
            wave_freq_out_calc_range[state] = [
                clk_freq / int(data_depth / addr_step_range[state][x] + 1) / int(step_count_range[state][x])
                for x
                in
                range(2 * range_float[state] + 1)]
            dif_abs_range = [abs(x - wave_freq_out) for x in wave_freq_out_calc_range[state]]
            dif_min_index = dif_abs_range.index(min(dif_abs_range))

        if (((i + 1) / 12709 - progress_i_last) > 0.01) or ((i + 1) / 12709 == 1):
            progress_i_last = (i + 1) / 12709
            progress_bar_number = progress_bar_number + 1
            print(f'Generating Dataset......{(i + 1) / 12709:.2%}')
            progress_bar_01.progress(progress_bar_number, text="正在生成数据，请等待……")
        addr_step_list.append(addr_step_range[state][dif_min_index])
        step_count_list.append(step_count_range[state][dif_min_index])
        frequency_set_list.append(int(dataset_freq.iat[i, 0] * 10))
        frequency_abs_error_list.append(dif_abs_range[dif_min_index])
        frequency_error_list.append(wave_freq_out_calc_range[state][dif_min_index] - wave_freq_out)
    progress_bar_01.progress(100, text="数据生成完毕，您可以进行后续数据分析")
    st.success('生成完毕，请等待数据分析', icon="✅")
    # addr_step_list = load_data(addr_step_list)
    # step_count_list = load_data(step_count_list)
    # frequency_set_list = load_data(frequency_set_list)
    # frequency_abs_error_list = load_data(frequency_abs_error_list)
    # frequency_error_list = load_data(frequency_error_list)

    # # 6.数据分析
    # st.subheader('6.数据分析/分析数据导入')
    # st.write('点击按钮以对生成的参数进行数据分析')

    # else:
    #     if st.button('开始数据分析'):
    if using_analysis_coe:
        if uploaded_file is not None:
            progress_bar_02 = st.progress(0, text="正在分析数据，请等待……")
            progress_bar_number = 0
            with open(uploaded_file.name, 'r') as distortion_analysis_file:
                distortion_analysis_file.readline()
                distortion_analysis_file.readline()
                for i in range(12709):
                    line_content = distortion_analysis_file.readline()
                    distortion_analysis_list.append(float(line_content[0:len(line_content) - 2]))
                distortion_analysis_file.close()
                print('distortion_analysis_file Reading......Done')
                progress_bar_02.progress(100, text="已读取存在的分析数据，分析完成")
                st.success('读取成功，您可以继续后续步骤', icon="✅")
    else:
        progress_bar_02 = st.progress(0, text="正在分析数据，请等待……")
        progress_bar_number = 0
        sin_val_DDS = 0
        sin_val_ORI = 0
        distortion = 0
        progress_k_last = 0
        for k in range(len(frequency_set_list)):
            distortion = 0
            sin_val_DDS_sum = 0
            sin_val_ORI_sum = 0
            n = 0
            for m in range(int(2 ** N_depth / 2)):
                sin_val_ORI_sum = sin_val_ORI_sum + math.sin(m / (2 ** N_depth) * 2 * math.pi) * 2 * math.pi / (
                        2 ** N_depth)
            for n in range(int(2 ** N_depth / addr_step_list[k] / 2)):
                sin_val_DDS_sum = sin_val_DDS_sum + math.sin(addr_step_list[k] * n / (2 ** N_depth) * 2 * math.pi) * \
                                  addr_step_list[k] * 2 * math.pi / (2 ** N_depth)
            sin_val_DDS_sum = sin_val_DDS_sum * (1 / max(
                [math.sin(addr_step_list[k] * x / (2 ** N_depth) * 2 * math.pi) for x in
                 range(int(2 ** N_depth / addr_step_list[k] / 2))]))
            distortion = abs(sin_val_ORI_sum - sin_val_DDS_sum) / sin_val_ORI_sum
            distortion_analysis_list.append(distortion)
            if (((k + 1) / 12709 - progress_k_last) > 0.01) or ((k + 1) / 12709 == 1):
                progress_k_last = (k + 1) / 12709
                print(f'Distortion Analysising......{(k + 1) / 12709:.2%}')
                progress_bar_number = progress_bar_number + 1
                progress_bar_02.progress(progress_bar_number, text="正在分析数据，请等待……")
        progress_bar_02.progress(100, text="数据分析完毕")
        st.success('分析完毕，等待生成数据文件', icon="✅")
    # 生成数据文件
    # 生成地址步进值的coe文件
    progress_bar_03 = st.progress(0, text="正在生成数据文件，请等待……")
    if '地址步进值的coe文件' in generate_coe_options:
        filename1 = 'addr_step'
        generate_coe(filename1, addr_step_list)
    progress_bar_03.progress(16, text="正在生成数据文件，请等待……")
    # 生成频率计数值的coe文件
    if '频率计数值的coe文件' in generate_coe_options:
        filename2 = 'step_count'
        generate_coe(filename2, step_count_list)
    progress_bar_03.progress(33, text="正在生成数据文件，请等待……")
    # 生成频率参数coe文件
    if '频率参数coe文件' in generate_coe_options:
        filename3 = 'frequency_set'
        generate_coe(filename3, frequency_set_list)
    progress_bar_03.progress(50, text="正在生成数据文件，请等待……")
    # 生成频率误差绝对值的coe文件
    if '频率误差绝对值的coe文件' in generate_coe_options:
        filename4 = 'frequency_abs_error'
        generate_coe(filename4, frequency_abs_error_list)
    progress_bar_03.progress(66, text="正在生成数据文件，请等待……")
    # 生成频率误差的coe文件
    if '频率误差的coe文件' in generate_coe_options:
        filename5 = 'frequency_error'
        generate_coe(filename5, frequency_error_list)
    progress_bar_03.progress(83, text="正在生成数据文件，请等待……")
    # 生成失真度分析的coe文件
    if '失真度分析的coe文件' in generate_coe_options:
        filename6 = 'distortion_analysis'
        generate_coe(filename6, distortion_analysis_list)
    progress_bar_03.progress(100, text="数据文件生成完毕")
    st.success('数据文件生成完毕，您可以查看分析图像', icon="✅")

    # 生成分析图像
    progress_bar_04 = st.progress(0, text="正在生成分析图像，请等待……")
    with open('.\max_in_data.txt', 'w') as fid:
        fid.write(f'max_in_addr_step_list:{max(addr_step_list)}\n')
        fid.write(f'max_in_step_count_list:{max(step_count_list)}\n')
        fid.write(f'max_in_frequency_set:{max(frequency_set_list)}\n')
        fid.write(f'max_in_frequency_abs_error:{max(frequency_abs_error_list)}\n')
        fid.write(f'max_in_frequency_error:{max(frequency_error_list)}\n')
        fid.write(f'max_in_distortion_analysis:{max(distortion_analysis_list)}\n')
        fid.close()
    progress_bar_04.progress(20, text="正在生成分析图像，请等待……")
    wave_freq_out = [].copy()
    # start_freq = 0
    # end_freq = 0
    for i in range(12709):
        wave_freq_out.append(float(dataset_freq.iat[i, 0]))
    # if range_type == 0:
    #     start_freq = 0
    #     end_freq = 10908
    # elif range_type == 1:
    #     start_freq = 0
    #     end_freq = 11809
    # elif range_type == 2:
    #     start_freq = 0
    #     end_freq = 12708
    progress_bar_04.progress(30, text="正在生成分析图像，请等待……")
    with open('frequency_error.coe', 'r') as frequency_error_file:
        frequency_error_file.readline()
        frequency_error_file.readline()
        for i in range(12709):
            line_content = frequency_error_file.readline()
            frequency_error.append(float(line_content[0:len(line_content) - 2]))
            frequency_relative_error.append(float(line_content[0:len(line_content) - 2]) / wave_freq_out[i])
        frequency_error_file.close()
    progress_bar_04.progress(50, text="正在生成分析图像，请等待……")
    plt.rcParams.update({"font.size": 24})
    if pic_type_01:
        plt.figure(figsize=(16, 9), dpi=pic_DPI)
        plt.title(f'Frequency Error —— [{start_freq}~{end_freq}] —— {2 ** N_depth}')
        plt.xlabel('Frequency / Hz')
        plt.ylabel('Frequency Error')
        plt.grid()
        plt.xlim([wave_freq_out[data_range_start], wave_freq_out[data_range_end]])
        if x_axis_type:
            plt.xscale('symlog')
        plt.scatter(wave_freq_out[data_range_start:data_range_end], frequency_error[data_range_start:data_range_end])
        plt.savefig(f'./frequency_error_{start_freq}_{end_freq}.png')
    progress_bar_04.progress(70, text="正在生成分析图像，请等待……")
    if pic_type_02:
        plt.figure(figsize=(16, 9), dpi=pic_DPI)
        plt.title(f'Frequency Relative Error —— [{start_freq}~{end_freq}] —— {2 ** N_depth}')
        plt.xlabel('Frequency / Hz')
        plt.ylabel('Frequency Relative Error')
        plt.grid()
        plt.xlim([wave_freq_out[data_range_start], wave_freq_out[data_range_end]])
        if x_axis_type:
            plt.xscale('symlog')
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
        plt.scatter(wave_freq_out[data_range_start:data_range_end],
                    frequency_relative_error[data_range_start:data_range_end])
        plt.savefig(f'./frequency_relative_error_{start_freq}_{end_freq}.png')
    progress_bar_04.progress(80, text="正在生成分析图像，请等待……")
    if pic_type_03:
        plt.figure(figsize=(16, 9), dpi=pic_DPI)
        plt.title(f'Analysis of Sine Wave Distortion —— [{start_freq}~{end_freq}] —— {2 ** N_depth}')
        plt.xlabel('Frequency / Hz')
        plt.ylabel('Sine Wave Distortion')
        plt.grid()
        plt.xlim([wave_freq_out[data_range_start], wave_freq_out[data_range_end]])
        if x_axis_type:
            plt.xscale('symlog')
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
        plt.scatter(wave_freq_out[data_range_start:data_range_end],
                    distortion_analysis_list[data_range_start:data_range_end])
        plt.savefig(f'./analysis_of_sine_wave_distortion_{start_freq}_{end_freq}.png')
    progress_bar_04.progress(90, text="正在生成分析图像，请等待……")
    plt.cla()
    plt.close("all")
    progress_bar_04.progress(100, text="分析图像生成完毕")
    st.success('分析图像生成完毕，生成过程已完成', icon="✅")
    st.balloons()
    st.markdown('***')

    # 显示图像
    st.subheader(':red[4.]查看分析图像')
    st.write('请跳转到:red[图像分析页]查看生成的分析图像')
# tab_1, tab_2, tab_3 = st.tabs(["频率失真误差", "频率失真相对误差", "波形失真度分析"])
# freq_range_dict = {'0Hz': 0, '0.1Hz': 0, '1Hz': 9, '10Hz': 18, '100Hz': 108, '1kHz': 1008, '10kHz': 1908,
#                    '100kHz': 10908, '1MHz': 11808, '10MHz': 12708}
# st.write(os.getcwd())
# with tab_1:
#     start_freq_1, end_freq_1 = st.select_slider(
#         '请选择波形频率范围',
#         options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
#         value=('0Hz', '10MHz'), key='slider_tab_1')
#     st.write('选定的频率范围', start_freq_1, '~', end_freq_1)
#     data_range_start = freq_range_dict[start_freq_1]
#     data_range_end = freq_range_dict[end_freq_1]
#     chart_data_1 = pd.DataFrame(
#         frequency_error[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
#     )
#     st.area_chart(chart_data_1)
# with tab_2:
#     start_freq_2, end_freq_2 = st.select_slider(
#         '请选择波形频率范围',
#         options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
#         value=('0Hz', '10MHz'), key='slider_tab_2')
#     st.write('您选定的频率范围为', start_freq_2, '~', end_freq_2)
#     data_range_start = freq_range_dict[start_freq_2]
#     data_range_end = freq_range_dict[end_freq_2]
#     chart_data_2 = pd.DataFrame(
#         frequency_relative_error[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
#     )
#     st.area_chart(chart_data_2)
# with tab_3:
#     start_freq_3, end_freq_3 = st.select_slider(
#         '请选择波形频率范围',
#         options=['0Hz', '0.1Hz', '1Hz', '10Hz', '100Hz', '1kHz', '10kHz', '100kHz', '1MHz', '10MHz'],
#         value=('0Hz', '10MHz'), key='slider_tab_3')
#     st.write('选定的频率范围', start_freq_3, '~', end_freq_3)
#     data_range_start = freq_range_dict[start_freq_3]
#     data_range_end = freq_range_dict[end_freq_3]
#     chart_data_3 = pd.DataFrame(
#         distortion_analysis_list[data_range_start:data_range_end], wave_freq_out[data_range_start:data_range_end]
#     )
#     st.area_chart(chart_data_3)
# 侧边栏参数总结
with st.sidebar:
    st.subheader('参数总结：')
    col1, col2, col3 = st.columns(3)
    col1.write('数据深度')
    col2.write(N_depth)
    col3.write('bit')
    col1.write('时钟频率')
    col2.write(clk_freq / 1000_000)
    col3.write('MHz')

    st.subheader('波形最低分辨率：')
    col1, col2 = st.columns(2)
    col1.write('0.1Hz~100kHz')
    col2.write(resolution_1)
    col1.write('100kHz~1MHz')
    col2.write(resolution_2)
    col1.write('1MHz~10MHz')
    col2.write(resolution_3)
