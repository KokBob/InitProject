# -*- coding: utf-8 -*-
"""
20181008
@author: CIKLAMINIMA
https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
https://www.novixys.com/blog/list-directory-python/
"""
import numpy as np
import matplotlib.pyplot as plt
import os 
import pandas as pd
import seaborn as sns

def catch_mea(measurement_file_name):
    ''' to receive:
    header, skiprows =3, [4]
    '''
    current_measurement_name = measurement_file_name.split('.')[0]
    
    if current_measurement_name == 'P_pressures':
        print(current_measurement_name)
        header_, skiprows_ = 3, [4]
        freq_ = 10
        
    elif current_measurement_name == 'Q_flow_rates':
        print(current_measurement_name)
        header_, skiprows_ = 3, [4]
        freq_ = 1
    elif current_measurement_name == 'RPM_signal':
        print(current_measurement_name)
        header_, skiprows_ = 0, [1,2,3,4]
        freq_ = .1
    elif current_measurement_name == 'Torque_signal':
        print(current_measurement_name)
        header_, skiprows_ =3, [4]
        freq_ = 100
    elif current_measurement_name == 'T_temperatures':
        print(current_measurement_name)
        header_, skiprows_ =3, [4]
        freq_ = 10
    else:
        print('error: no definede measurement')
    return header_, skiprows_, freq_, current_measurement_name 

def time_vector(freq_,data_):
    freq = freq_
    period = '{}N'.format( int(1e9 / freq))
    start_time = data_['Unnamed: 0'][1]
    t_ = pd.date_range(start=start_time, periods=len(data_), freq=period)
    return t_

def get_overview_plot(mea_dict, save_fig = False):
#    for i in len(mea_dict['data'].keys())
    fig = plt.figure(figsize=[12,7])
    ax = plt.subplot(1,1,1)
    for key in mea_dict['data'].keys():
        if key == 'Unnamed: 0':
            continue
        else:
            plt.plot(mea_dict['t'], mea_dict['data'][key], label = key)
            plt.title(mea_dict['load'] + '\n' + mea_dict['name'])
            
            handles, labels = ax.get_legend_handles_labels()
            lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
            plt.legend()
            plt.tight_layout()
def plot_temperatures_PLS1(mea_dict, save_fig = False):
    fig = plt.figure(figsize=[12,7])
    ax = plt.subplot(1,1,1)         
            
    PLS1 = ['T31M PLS1 PW1 RS bearing',
       'T32M PLS1 PW1 GS bearing', 'T33M PLS1 PW2 RS bearing',
       'T34M PLS1 PW2 GS bearing', 'T35M PLS1 PW3 RS bearing',
       'T36M PLS1 PW3 GS bearing', 'T37M PLS1 PW4 RS bearing',
       'T38M PLS1 PW4 GS bearing', 'T39M PLS1 PW5 RS bearing',
       'T40M PLS1 PW5 GS bearing', 'T50M PLS1 carrier cast surface temperature']
#    'T50M PLS1 carrier cast surface temperature'

    for pls1 in PLS1:
        ax.plot(mea_dict['t'], mea_dict['data'][pls1], label = pls1)
        handles, labels = ax.get_legend_handles_labels()
        lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.legend()
        plt.tight_layout()
        ax.set_ylim([50,110])
        
def plot_temperatures_PLS2(mea_dict, save_fig = False):
    fig = plt.figure(figsize=[12,7])
    ax = plt.subplot(2,1,1)         
            
    PLS2 = ['T41M PLS2 PW1 RS bearing',
       'T42M PLS2 PW1 GS bearing', 'T43M PLS2 PW2 RS bearing',
       'T44M PLS2 PW2 GS bearing', 'T45M PLS2 PW3 RS bearing',
       'T46M PLS2 PW3 GS bearing','T51M PLS2 carrier cast surface temperature']

    for pls2 in PLS2:
        ax.plot(mea_dict['t'], mea_dict['data'][pls2], label = pls2)  
        handles, labels = ax.get_legend_handles_labels()
        lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.legend()
        plt.tight_layout()
        ax.set_ylim([60,80])
#    ax.plot(mea_dict['t'], mea_dict['data'][pls2], label = pls2)
def plot_Torque_Temp_pls1(data_repos):
    mea_dict_temp = data_repos[-1]
    
    
    fig = plt.figure(figsize=[15,8])
    ax = plt.subplot(2,1,1)     
    ax2 = plt.subplot(2,1,2)  
    
    
    PLS1 = ['T31M PLS1 PW1 RS bearing',
       'T32M PLS1 PW1 GS bearing', 'T33M PLS1 PW2 RS bearing',
       'T34M PLS1 PW2 GS bearing', 'T35M PLS1 PW3 RS bearing',
       'T36M PLS1 PW3 GS bearing', 'T37M PLS1 PW4 RS bearing',
       'T38M PLS1 PW4 GS bearing', 'T39M PLS1 PW5 RS bearing',
       'T40M PLS1 PW5 GS bearing', 'T50M PLS1 carrier cast surface temperature']
#    'T50M PLS1 carrier cast surface temperature'

    for pls1 in PLS1:
        ax.plot(mea_dict_temp['t'], mea_dict_temp['data'][pls1], label = pls1)
        handles, labels = ax.get_legend_handles_labels()
        lgd = ax.legend(handles, labels, loc='upper left')
#        plt.legend()
#        plt.tight_layout()
        ax.set_ylim([60,100])
        
#    fig = plt.figure(figsize=[8,74])
#    ax = plt.subplot(2,1,1)     
#    ax2 = plt.subplot(2,1,2)     
    
    ax2.plot(data_repos[3]['t'],data_repos[3]['data']['Torque'])        
    plt.legend()
    plt.tight_layout()
def plot_Torque_Temp_pls2(data_repos):
    mea_dict_temp = data_repos[-1]
    
    
    fig = plt.figure(figsize=[15,8])
    ax = plt.subplot(2,1,1)     
    ax2 = plt.subplot(2,1,2)        
            
    PLS2 = ['T41M PLS2 PW1 RS bearing',
       'T42M PLS2 PW1 GS bearing', 'T43M PLS2 PW2 RS bearing',
       'T44M PLS2 PW2 GS bearing', 'T45M PLS2 PW3 RS bearing',
       'T46M PLS2 PW3 GS bearing','T51M PLS2 carrier cast surface temperature']

    for pls2 in PLS2:
        ax.plot(mea_dict_temp['t'], mea_dict_temp['data'][pls2], label = pls2)  
        handles, labels = ax.get_legend_handles_labels()
        lgd = ax.legend(handles, labels, loc='upper left')
        
        ax.set_ylim([50,80])
        

    ax2.plot(data_repos[3]['t'],data_repos[3]['data']['Torque'])
    plt.legend()
    plt.tight_layout()



def plot_Torque_Temp_pls(data_repos):
    mea_dict_temp = data_repos[-1]
    
    
    fig = plt.figure(figsize=[15,8])
    ax = plt.subplot(3,1,1)     
    ax2 = plt.subplot(3,1,2)  
    ax3 = plt.subplot(3,1,3)  
    
    
    PLS1 = ['T31M PLS1 PW1 RS bearing',
       'T32M PLS1 PW1 GS bearing', 'T33M PLS1 PW2 RS bearing',
       'T34M PLS1 PW2 GS bearing', 'T35M PLS1 PW3 RS bearing',
       'T36M PLS1 PW3 GS bearing', 'T37M PLS1 PW4 RS bearing',
       'T38M PLS1 PW4 GS bearing', 'T39M PLS1 PW5 RS bearing',
       'T40M PLS1 PW5 GS bearing', 'T50M PLS1 carrier cast surface temperature']
#    'T50M PLS1 carrier cast surface temperature'

    for pls1 in PLS1:
        ax.plot(mea_dict_temp['t'], mea_dict_temp['data'][pls1], label = pls1)
        handles, labels = ax.get_legend_handles_labels()
        lgd = ax.legend(handles, labels, loc='upper left')
        ymax = data_repos[-1]['data'][PLS1].max().max()
        ymin = data_repos[-1]['data'][PLS1].mean().min()
        ax.set_ylim([ymin - 20, ymax + 2])
        

   
            
    PLS2 = ['T41M PLS2 PW1 RS bearing',
       'T42M PLS2 PW1 GS bearing', 'T43M PLS2 PW2 RS bearing',
       'T44M PLS2 PW2 GS bearing', 'T45M PLS2 PW3 RS bearing',
       'T46M PLS2 PW3 GS bearing','T51M PLS2 carrier cast surface temperature']

    for pls2 in PLS2:
        ax2.plot(mea_dict_temp['t'], mea_dict_temp['data'][pls2], label = pls2)  
        handles, labels = ax2.get_legend_handles_labels()
        lgd = ax2.legend(handles, labels, loc='upper left')    
        ymax = data_repos[-1]['data'][PLS2].max().max()
        ymin = data_repos[-1]['data'][PLS2].mean().min()
        ax2.set_ylim([ymax - 20, ymax + 2])

        

    
    ax3.plot(data_repos[3]['t'],data_repos[3]['data']['Torque'])
    
    ax.set_title(data_repos[0]['load'])
    plt.legend()
    plt.tight_layout()
    plt.savefig(data_repos[0]['load'])
    