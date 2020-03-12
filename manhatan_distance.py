#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:45:28 2020

@author: brianmatejevich
"""

#manhatan distance

def man_dist(x1,y1,x2,y2):
    xdiff = abs(x1-x2)
    ydiff = abs(y1-y2)
    return(xdiff+ydiff)
    
    
a = man_dist(2,2,4,5)
print(a)