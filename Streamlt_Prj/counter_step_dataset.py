import pandas as pd
import math
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.font_manager as fm


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


pic_DPI = 70
N_depth_range = [15]
resolution_range = []
# resolution_range.append([72, 36, 8])
resolution_range.append([64, 32, 8])
# resolution_range.append([64, 32, 12])
# for N_depth_i in [10, 11, 12, 13, 14, 15, 16]:
for resolution_range_i in range(len(resolution_range)):
    N_depth = int(N_depth_range[0])
    clk_freq = int(125_000_000)
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
    lowest_resolution = resolution_range[resolution_range_i]
    addr_step_range = [[], [], []]
    step_count_range = [[], [], []]
    state = 0

    for i in range(3):
        addr_step[i] = int(data_depth / lowest_resolution[i] / 2)
        range_float[i] = int(addr_step[i] - 1)
        addr_step_range[i] = [addr_step[i] + x for x in range(-range_float[i], range_float[i] + 1)]

        for j in range(2 * range_float[i] + 1):
            step_count_range[i].append([])
            wave_freq_out_calc_range[i].append([])

    dataset_freq = pd.read_csv(
        'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\频率表格_Python分析.CSV')

    # print(dataset_1024)

    if os.path.exists(
            f'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\DDS_dataset_{2 ** N_depth}_{resolution_range[resolution_range_i][0]}_{resolution_range[resolution_range_i][1]}_{resolution_range[resolution_range_i][2]}'):
        os.chdir(
            f'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\DDS_dataset_{2 ** N_depth}_{resolution_range[resolution_range_i][0]}_{resolution_range[resolution_range_i][1]}_{resolution_range[resolution_range_i][2]}')
    else:
        os.mkdir(
            f'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\DDS_dataset_{2 ** N_depth}_{resolution_range[resolution_range_i][0]}_{resolution_range[resolution_range_i][1]}_{resolution_range[resolution_range_i][2]}')
        os.chdir(
            f'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\DDS_dataset_{2 ** N_depth}_{resolution_range[resolution_range_i][0]}_{resolution_range[resolution_range_i][1]}_{resolution_range[resolution_range_i][2]}')

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
            print(f'Generating Dataset......{(i + 1) / 12709:.2%}')

        addr_step_list.append(addr_step_range[state][dif_min_index])
        step_count_list.append(step_count_range[state][dif_min_index])
        frequency_set_list.append(int(dataset_freq.iat[i, 0] * 10))
        frequency_abs_error_list.append(dif_abs_range[dif_min_index])
        frequency_error_list.append(wave_freq_out_calc_range[state][dif_min_index] - wave_freq_out)

    # 以1V为幅值进行计算
    sin_val_DDS = 0
    sin_val_ORI = 0
    distortion = 0
    # for k in range(len(frequency_set_list)):
    #     distortion = 0
    #     distortion_sum = 0
    #     n = 0
    #     for m in range(2 ** N_depth):
    #         if m % addr_step_list[k] == 0:
    #             n = n + 1
    #         sin_val_DDS = math.sin(addr_step_list[k] * n / (2 ** N_depth) * 2 * math.pi)
    #         sin_val_ORI = math.sin((m / (2 ** N_depth) - addr_step_list[k] / 2 / (2 ** N_depth)) * 2 * math.pi)
    #         distortion_sum = distortion_sum + math.sqrt((sin_val_DDS - sin_val_ORI) ** 2)
    #     distortion = distortion_sum / (2 ** N_depth)
    #     distortion_analysis_list.append(distortion)

    # for k in range(len(frequency_set_list)):
    #     distortion = 0
    #     sin_val_DDS_sum = 0
    #     sin_val_ORI_sum = 0
    #     n = 0
    #     for m in range(int(2 ** N_depth / 2)):
    #         sin_val_ORI_sum = sin_val_ORI_sum + math.sin(m / (2 ** N_depth) * 2 * math.pi) * 2 * math.pi / (
    #                 2 ** N_depth)
    #     for n in range(int(2 ** N_depth / addr_step_list[k] / 2)):
    #         sin_val_DDS_sum = sin_val_DDS_sum + math.sin(addr_step_list[k] * n / (2 ** N_depth) * 2 * math.pi) * \
    #                           addr_step_list[k] * 2 * math.pi / (2 ** N_depth)
    #     distortion = abs(sin_val_ORI_sum - sin_val_DDS_sum) / sin_val_ORI_sum
    #     distortion_analysis_list.append(distortion)
    if os.path.exists(
            f'D:\pythonProject\Python数据分析与办公自动化\DDS_waveform_generator\DDS_dataset_{2 ** N_depth}_{resolution_range[resolution_range_i][0]}_{resolution_range[resolution_range_i][1]}_{resolution_range[resolution_range_i][2]}\distortion_analysis{2 ** N_depth}.coe'):
        with open(f'distortion_analysis{2 ** N_depth}.coe', 'r') as distortion_analysis_file:
            line_content = distortion_analysis_file.readline()
            line_content = distortion_analysis_file.readline()
            for i in range(12709):
                line_content = distortion_analysis_file.readline()
                distortion_analysis_list.append(float(line_content[0:len(line_content) - 2]))
            distortion_analysis_file.close()
            print('distortion_analysis_file Reading......Done')

    else:
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

    # 生成地址步进值的coe文件
    filename1 = f'addr_step_{2 ** N_depth}'
    generate_coe(filename1, addr_step_list)

    # 生成频率计数值的coe文件
    filename2 = f'step_count_{2 ** N_depth}'
    generate_coe(filename2, step_count_list)

    # 生成频率的coe文件
    filename3 = 'frequency_set'
    generate_coe(filename3, frequency_set_list)

    # 生成频率误差绝对值的coe文件
    filename4 = f'frequency_abs_error_{2 ** N_depth}'
    generate_coe(filename4, frequency_abs_error_list)

    # 生成频率误差的coe文件
    filename5 = f'frequency_error_{2 ** N_depth}'
    generate_coe(filename5, frequency_error_list)

    # 生成失真度分析的coe文件
    filename6 = f'distortion_analysis{2 ** N_depth}'
    generate_coe(filename6, distortion_analysis_list)

    with open('.\max_in_data.txt', 'w') as fid:
        fid.write(f'max_in_addr_step_list:{max(addr_step_list)}\n')
        fid.write(f'max_in_step_count_list:{max(step_count_list)}\n')
        fid.write(f'max_in_frequency_set:{max(frequency_set_list)}\n')
        fid.write(f'max_in_frequency_abs_error:{max(frequency_abs_error_list)}\n')
        fid.write(f'max_in_frequency_error:{max(frequency_error_list)}\n')
        fid.write(f'max_in_distortion_analysis:{max(distortion_analysis_list)}\n')
        fid.close()

    frequency_error = []
    frequency_relative_error = []
    wave_freq_out = []

    for i in range(12709):
        wave_freq_out.append(dataset_freq.iat[i, 0])

    with open(f'frequency_error_{2 ** N_depth}.coe', 'r') as frequency_error_file:
        line_content = frequency_error_file.readline()
        line_content = frequency_error_file.readline()
        for i in range(12709):
            line_content = frequency_error_file.readline()
            frequency_error.append(float(line_content[0:len(line_content) - 2]))
            frequency_relative_error.append(float(line_content[0:len(line_content) - 2]) / wave_freq_out[i])
        frequency_error_file.close()

    plt.rcParams.update({"font.size": 24})

    plt.figure(figsize=(16, 9), dpi=pic_DPI)
    plt.title(f'Frequency Error —— [0Hz~10MHz] —— {2 ** N_depth}')
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Frequency Error')
    plt.grid()
    plt.xlim([0, 1e7])
    plt.xscale('symlog')
    plt.scatter(wave_freq_out, frequency_error)
    plt.savefig('./frequency_error_0Hz_10MHz.png')

    plt.figure(figsize=(16, 9), dpi=pic_DPI)
    plt.title(f'Frequency Relative Error —— [0Hz~10MHz] —— {2 ** N_depth}')
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Frequency Relative Error')
    plt.grid()
    plt.xlim([0, 1e7])
    plt.xscale('symlog')
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    plt.scatter(wave_freq_out, frequency_relative_error)
    plt.savefig('./frequency_relative_error_0Hz_10MHz.png')

    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Frequency Error —— [0Hz~1MHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Frequency Error')
    # plt.grid()
    # plt.xlim([0, 1e6])
    # plt.scatter(wave_freq_out[0:11809], frequency_error[0:11809])
    # plt.savefig('./frequency_error_0Hz_1MHz.png')
    #
    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Frequency Relative Error —— [0Hz~1MHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Frequency Relative Error')
    # plt.grid()
    # plt.xlim([0, 1e6])
    # plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    # plt.scatter(wave_freq_out[0:11809], frequency_relative_error[0:11809])
    # plt.savefig('./frequency_relative_error_0Hz_1MHz.png')
    #
    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Frequency Error —— [0Hz~100kHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Frequency Error')
    # plt.grid()
    # plt.xlim([0, 1e5])
    # plt.scatter(wave_freq_out[0:10909], frequency_error[0:10909])
    # plt.savefig('./frequency_error_0Hz_100kHz.png')
    #
    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Frequency Relative Error —— [0Hz~100kHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Frequency Relative Error')
    # plt.grid()
    # plt.xlim([0, 1e5])
    # plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    # plt.scatter(wave_freq_out[0:10909], frequency_relative_error[0:10909])
    # plt.savefig('./frequency_relative_error_0Hz_100kHz.png')

    plt.figure(figsize=(16, 9), dpi=pic_DPI)
    plt.title(f'Analysis of Sine Wave Distortion —— [0Hz~10MHz] —— {2 ** N_depth}')
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Sine Wave Distortion')
    plt.grid()
    plt.xlim([0, 1e7])
    plt.xscale('symlog')
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    plt.scatter(wave_freq_out, distortion_analysis_list)
    plt.savefig('./analysis_of_sine_wave_distortion_0Hz_10MHz.png')


    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Analysis of Sine Wave Distortion —— [0Hz~1MHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Sine Wave Distortion')
    # plt.grid()
    # plt.xlim([0, 1e6])
    # plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    # plt.scatter(wave_freq_out[0:11809], distortion_analysis_list[0:11809])
    # plt.savefig('./analysis_of_sine_wave_distortion_0Hz_1MHz.png')
    #
    # plt.figure(figsize=(16, 9), dpi=pic_DPI)
    # plt.title(f'Analysis of Sine Wave Distortion —— [0Hz~100kHz] —— {2 ** N_depth}')
    # plt.xlabel('Frequency / Hz')
    # plt.ylabel('Sine Wave Distortion')
    # plt.grid()
    # plt.xlim([0, 1e5])
    # plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    # plt.scatter(wave_freq_out[0:10909], distortion_analysis_list[0:10909])
    # plt.savefig('./analysis_of_sine_wave_distortion_0Hz_100kHz.png')

    plt.cla()
    plt.close("all")
