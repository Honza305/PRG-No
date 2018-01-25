#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:56:28 2018

@author: mah35070
"""

from pylab import imshow, show

data = []

for i in range(64):
    barva = 1
    radek = []
    for j in range(64):
        if j % 2 == 0 :
            radek.append(0)
        else:
            radek.append(1) 
    for k in range(64):
        if k
        
    data.append(radek)
    
    
imshow(data, interpolation='none', cmap='binary_r')


show()