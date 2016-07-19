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

datethru = '2015-05-20'
runthru = 42

#get thru data first:
fthrupulse = constants.datafolder+ '/Data_'+datethru+'/Run_'+str(runthru)+'/'+datethru+'_Run_'+str(runthru)+'_channel1.data'
fthruradio = constants.datafolder+ '/Data_'+datethru+'/Run_'+str(runthru)+'/'+datethru+'_Run_'+str(runthru)+'_channel2.data'
#get the average waveform
wfthrupulse = getaveragewf(fthrupulse,100)
wfthruradio = getaveragewf(fthruradio,100)
#perform fft
thruradiofft = np.fft.fft(wfthruradio[1])
thrupulsefft = np.fft.fft(wfthrupulse[1])
#computes gain in voltage
vgainthru = thruradiofft/thrupulsefft
deltat = wfthruradio[0][1]-wfthruradio[0][0]
fftfreq = np.fft.fftfreq(len(thruradiofft),deltat)
#save the gain in V
outfilethru = constants.outfolder + '/thru/thruvgain'
np.savez(outfilethru, fftfreq, vgainthru)
print '#############################################'
print 'saved the thru gain in file', outfilethru+'.npz'
print '#############################################'
