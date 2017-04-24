# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:04:48 2017

@author: nasty
"""

def format(f, n):  
    if round(f)==f:  
        m = len(str(f))-1-n  
        if f/(10**m) ==0.0:  
            return f  
        else:  
            return float(int(f)/(10**m)*(10**m))  
    return round(f, n - len(str(int(f)))) if len(str(f))>n+1 else f 			