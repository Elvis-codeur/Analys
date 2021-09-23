# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:05:23 2020

@author: Elvis
"""
import numpy as np

def expo_proba(lamb,x1,x2):
    def a(l,x):
        return -np.exp(-l*x)
    return  a(lamb,x2) -a(lamb,x1)

def expo_dist(lamb,x1,x2):
    x = np.arange(x1,x2,abs(x1-x2)/1000)
    return lamb*np.exp(-lamb*x)
            
print(expo_dist(1.1,0,2))
    