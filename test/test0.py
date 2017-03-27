# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:11:47 2017

@author: nasty
"""

#import pylab as pl
#import numpy as np

import numpy as np
import matplotlib.pyplot as plt
def func(x,p):
    A,K,theta=p
    return A*np.sin(2*np.pi*K*x+theta)
def residuals(p,y,x):
    return y-func(x,p)
x=np.linspace(0,2*np.pi,100)
a,k,theta=10,0.34,np.pi/6
y0=func(x,[a,k,theta])
y1=np.random.randn(len(x))+y0
p0=[7,0.4,0]
from scipy import optimize
ps=optimize.leastsq(residuals,p0,args=(y1,x))
print(ps[0])
plt.plot(x,y1,"o")
plt.plot(x,y0,label=u"真实数据")
plt.plot(x,func(x,ps[0]),label=u"拟合数据")
plt.legend(loc="best")