# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:46:41 2018

@author: zahmed
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
x=np.arange(-100,100,1)
y=np.arange(-100,100,1)
X, Y = np.meshgrid(x, y)
Z = (X,Y)
#plt.plot(Z)
g= 2*np.exp(-0.5*((x+1)/10)**2)
g2= 2*np.exp((-0.5*((x+2)/20)**2))
g3= 2*np.exp((-0.5*((x+4)/25)**2))
g4= 2*np.exp((-0.5*((x+6)/30)**2))
g5= 2*np.exp((-0.5*((x+8)/40)**2))
plt.figure()
plt.plot(g3)
plt.plot(g)
plt.plot(g2)
plt.plot(g4)
plt.plot(g5)

#corr=signal.correlate2d(a,g)
corr1 =  signal.correlate(g,g2)
corr2 = signal.correlate(g,g3)
corr3 = signal.correlate(g,g4)
corr4 = signal.correlate(g,g5)
plt.show('Figure 2')
plt.plot(corr1, '+')
plt.plot(corr2, 'o')
plt.plot(corr3, '+')
plt.plot(corr4, 'o')
#plt.plot(corr3, 'x')

#contour plot
y=np.arange(0.5,200,0.5)
G=(y,corr1)
G1=(y,corr2)
G2=(y,corr3)
G3=(y,corr4)
#G1=(x,g2)
plt.figure()
plt.xlim(0,400)
plt.ylim(0,1)
plt.contour(G)
plt.contour(G1)
plt.contour(G2)
plt.contour(G3)