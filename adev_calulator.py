# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:26:28 2018

@author: zahmed
"""
"""
import numpy as np
import pandas as pd
df=pd.read_table('WAVEMETER_ACETYLENE_SIDE OF FRINGE.txt')
df.columns=['o','ET','wavelength', 'V', 'R', 'T','TP']
#x=df['time']
y=df['wavelength']
#xx=np.sin(x)+np.cos(2*x)+y
#x1=x[::30000]
#y1=y[::30000]
import matplotlib.pyplot as plt
#plt.plot(x,y)
#plt.show()
plt.psd(y,Fs=50)
plt.show()
#plt.xlim(0,10)
ys=y.values
y0=ys[0]
yd=ys/y0
import allantools
import pylab as plt
t= np.logspace(0,10,100)
r=100
(t2, ad, ade, adn) = allantools.adev(yd, rate=r, data_type="freq", taus='all')
fig = plt.loglog(t2, ad)
plt.show('figure 3')
"""

import numpy as np
import pandas as pd
#read in the file as a table
df=pd.read_csv('sensor1_20C.csv')
#assign coumln headers
df.columns=['time','wavelength']

####### format time axis
df['time']=pd.to_datetime(df['time'])
####### convert to elapsed time
time_zero=df['time'][0]
df['time_elapsed']=df['time']-time_zero
df['time_ms']=df['time_elapsed']/np.timedelta64(1,'ms')
######
y=df['wavelength']
import matplotlib.pyplot as plt
ys=y.values
yd=ys/ys[0]
import allantools
t= np.logspace(0,10,100)
r=35
(t2, ad, ade, adn) = allantools.adev(yd, rate=r, data_type="freq", taus='all')
fig = plt.loglog(t2, ad)
plt.show('figure 1')
plt.figure