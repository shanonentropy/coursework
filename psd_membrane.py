# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:25:21 2018

@author: zahmed
"""

import pandas as pd
import numpy as np
#import datetime
#from datetime import timedelta


df=pd.read_csv('n185.csv', header=0)
df.columns=['time','wavelength']
df['time']=pd.to_datetime(df['time'])
time_zero=df['time'][0]
df['time_elapsed']=df['time']-time_zero
df['time_ms']=df['time_elapsed']/np.timedelta64(1,'ms')
df['time_s']=df['time_ms']/1000


import matplotlib.pyplot as plt
x=df['time_s']
y=df['wavelength']
plt.plot(x,y, 'o')
###plt.show()



