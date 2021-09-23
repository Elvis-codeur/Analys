# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:23:43 2020

@author: Elvis
"""

import matplotlib.pyplot as plt
a = []
eating = [1,2,3,4,5,14,23]
working = [41,0,21,36,0,14,10]

days =[1,2,3,4,5,6,7]

a.append(eating)
a.append(working)

plt.stackplot(days,a)

plt.show()