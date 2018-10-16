# -*- coding: utf-8 -*-
"""
20181010
ciklaminima
"""
import numpy as np
import matplotlib.pyplot as plt
import os 
import pandas as pd
import _dataPostprLib_ as lib
import seaborn as sns
import importlib 
#%%
sns.set()
#sns.set_context("poster")
sns.set_context("paper")
#sns.color_palette("Paired")
seq_col_brew = sns.color_palette('hls', 12)
sns.set_palette(seq_col_brew)

plt.close('all')
path_glob = r'U:\projects\0005_Moventas_RCA\40_measurement'
test_bench_name = ['Data_test_run_63526_PPH-5700', 'Data_test_run_63527_PPH-5700']
#%%
path_test_bench_i = path_glob + '\\' + test_bench_name[0]
path_meas = os.listdir(path_test_bench_i)
#%% 
i = 0

lc_repos = []
for lc in path_meas:
    
#load_collection = path_meas[0] 
    load_collection = lc 
    #load_collection = path_meas[-1] 
    path_mea_i = path_test_bench_i  + '\\' + load_collection 
    meas_i = os.listdir(path_mea_i)
    
    data_repos = []
    for mf in meas_i:
        h_,r_,freq_,name_  = lib.catch_mea(mf)
        mea_file = path_mea_i + '\\' + mf 
        data_i = pd.read_csv(mea_file,sep=';',header=3, skiprows = [4])
        t_i = lib.time_vector(freq_,data_i)
        mea_dict = {'data': data_i,  
                    't': t_i,
                    'name': name_,
                    'load': load_collection}
        
        data_repos.append(mea_dict)
#    lib.plot_Torque_Temp_pls1(data_repos)
#    lib.plot_Torque_Temp_pls2(data_repos)
    lib.plot_Torque_Temp_pls(data_repos)
    lc_repos.append(data_repos)
#    data_repos_actual = data_repos[i]
#%%
#    lib.plot_Torque_Temp_pls1(data_repos)
#    lib.plot_Torque_Temp_pls2(data_repos)
#    lib.plot_Torque_Temp_pls(data_repos)
#    i += 1