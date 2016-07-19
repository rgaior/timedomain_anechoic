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

datatoplot  = sys.argv[1]

filename = constants.outfolder + datatoplot
xy = loadnpzfile(filename)
dt = xy[0][1] - xy[0][0]
#filtered = myBPfilter(xy[1],dt, 0.1e9,1e9)
plt.plot(xy[0],xy[1])
#plt.plot(xy[0],filtered)
plt.show()
    
