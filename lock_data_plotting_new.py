# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:25:21 2018

@author: zahmed
"""

import pandas as pd
import numpy as np
#import datetime
#from datetime import timedelta

######## open files
df=pd.read_csv('soln_185.csv', header=0)
df1=pd.read_csv('Nuc_soln_185.csv', header=0)
df2=pd.read_csv('CaP_nuc_185.csv', header=0)
####### rename columns
df.columns=['time','wavelength']
df1.columns=['time','wavelength']
df2.columns=['time','wavelength']
####### format time axis
df['time']=pd.to_datetime(df['time'])
df1['time']=pd.to_datetime(df1['time'])
df2['time']=pd.to_datetime(df2['time'])

####### convert to elapsed time
time_zero=df['time'][0]
df['time_elapsed']=df['time']-time_zero
df['time_ms']=df['time_elapsed']/np.timedelta64(1,'ms')

time_zero_1=df1['time'][0]
df1['time_elapsed']=df1['time']-time_zero_1
df1['time_ms']=df1['time_elapsed']/np.timedelta64(1,'ms')

time_zero_2=df2['time'][0]
df2['time_elapsed']=df2['time']-time_zero_2
df2['time_ms']=df2['time_elapsed']/np.timedelta64(1,'ms')
####### plot data
import matplotlib.pyplot as plt
x=df['time_ms'][:150000:500]
y=df['wavelength'][:150000:500]

x1=df1['time_ms'][:150000:500]
y1=df1['wavelength'][:90000:500]

x2=df2['time_ms'][:150000:500]
y2=df2['wavelength'][:150000:500]

plt.plot(x,y, 'b+')
plt.plot(x,y, '.')
plt.plot(x,y, 'g--')

plt.legend(['soln', 'nuc', 'CaP'])
###plt.show()



