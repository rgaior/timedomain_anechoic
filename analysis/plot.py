import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import sys
import os
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import math
import constants
from utils import *


fmin = 0.1e9
fmax = 1e9
typetoplot = sys.argv[1]
datatoplot = sys.argv[2:]
print datatoplot

for data in  datatoplot:
    filename = constants.outfolder + data + '_'
    if typetoplot == 'gain':
        filename = filename + 'gain.npz'
        xy = loadnpzfile(filename)
        plt.plot(xy[0],xy[1])
    if typetoplot == 'hnt':
        filename = filename + 'hnt.npz'
        xy = loadnpzfile(filename)
        dt = xy[0][1] - xy[0][0] 
        filtered = myBPfilter(xy[1],dt,fmin,fmax)
        plt.plot((xy[0]-xy[0][0])*1e9,filtered,c='b',lw=2)
        
plt.xlim(0,20)
plt.xlabel('time [ns]')
plt.ylabel('antenna time response [a.u.]')
plt.show()
    
