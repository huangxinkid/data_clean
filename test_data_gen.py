# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:48:20 2018

@author: Administrator
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import datetime 
from scipy import interpolate
from pandas import DataFrame,Series

#num_pi为要产生几个π的sin数据，num_ex为异常点的个数,num_gap为段缺失数据的个数，num_bk为单个缺失值的个数
def test_data_gen(num_pi,num_ex,num_gap,num_bk):
    if (num_pi>0) :
        num_point=72*num_pi
        x=np.linspace(0,np.pi*num_pi,num_point)
        signal1=[(math.sin(i)+1) for i in x] #产生测试用的num_pi个sin数据
        noise=np.random.normal(0,0.1,num_point)#numpy.random.normal(噪声均值, 噪声标准差, 噪声的shape)
        signal1=signal1+noise#在sin数据上添加噪声
    else:
        print("Please input valid num_pi")
        return

    if (num_ex>0) :
        #随机添加异常值
        point_ex=[]
        for i in range(num_ex):
            point_ex.append(np.random.randint(0,len(signal1))) #异常值的位置
        for _ in point_ex:
            signal1[_]=signal1[_]*1.8
    else:
        pass
    if (num_gap>0) :    
        #随机添加段数据缺失
        longth_gap=np.random.randint(15)+5 #缺口大小5~20

        point_gap=[]   #缺口的位置
        for i in range(num_gap):
            point_gap.append(np.random.randint(num_point-20))

        for i in point_gap:
            for j in range(longth_gap):  
                signal1[i+j]=None
    else:
        pass
    if (num_bk>0) :        
        #随机添加单点缺失值
        point_break=[]
        for i in range(num_bk):
            point_break.append(np.random.randint(num_point))        
        for _ in point_break:
            signal1[_]=None
    else:
        pass
    #产生时间序列，每隔5分钟一个点
    date_need=[]
    start_dt = datetime.datetime(2017, 1, 1) 
    interval = datetime.timedelta(seconds=300) 
    for i in range(num_point): 
        date_need.append(start_dt + interval * i)

    df = DataFrame(signal1,index = date_need[0:num_point])
    df.to_excel('data_test.xlsx')        
    plt.figure(figsize=(10,5))
    plt.plot(signal1)
    plt.show()

    return signal1
#增加备注
#再添加一条备注
#再试试
#再熟练一下