#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:48:22 2020

@author: brianmatejevich
"""

#plotting in matplotlib

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
   (0., 0.),  # left, bottom
   (0., 5.),  # left, top
   (1., 3.),  # right, top
   (10., 1.),  # right, bottom
   (0., 0.),  # ignored
]

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

path = Path(verts, codes)


fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)


verts2=[(95,200-170),(30.5,200-132.5),(35.5,200-123.9),(100,200-161.4),(95,200-170)]
codes2 = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]
path2 = Path(verts2, codes2)
patch2 = patches.PathPatch(path2, facecolor='red', lw=2)
ax.add_patch(patch2)

ax.set_xlim(0, 300)
ax.set_ylim(0, 200)
plt.show()