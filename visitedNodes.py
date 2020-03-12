#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:34:42 2020

@author: brianmatejevich
"""

#create dictionary to check duplicate nodes
d = {}

for x in range(30*2):
    for y in range(20*2):
        for z in range(12):
            string = str(x/2)+","+str(y/2)+","+str(z)
            d[string] = 0