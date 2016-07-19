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

#constant
distance = constants.distance #m

date = '2015-05-20'
run = 20

datethru = '2015-05-20'
runthru = 42
#get thru gain first (cf findthru.py):
thrufile = constants.outfolder +'/thru/thruvgain.npz'
thrugain = loadnpzfile(thrufile)
vgainthru = thrugain[1]
fftfreq = thrugain[0] 
 
#get the data for the actual radio run
fpulse = constants.datafolder+ '/Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel1.data'
fradio = constants.datafolder+ '/Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel2.data'
nrofev = 100
#get the average waveforms [time, amplitude]
wfpulse = getaveragewf(fpulse,nrofev)
wfradio = getaveragewf(fradio,nrofev)
#do fft
vrecfft = np.fft.fft(wfradio[1])
#multiply by the thru gain (same as divide the rec voltage)
vsrcfft = np.fft.fft(wfpulse[1])*vgainthru
#get the hn:

time = wfpulse[0]
thnt = gethn2antennas(vsrcfft, vrecfft, wfpulse[0], distance)
#hnt = myLPfilter(thnt[1], time[1] - time[0], 2e9)
hnt = thnt[1]
hn = np.fft.fft(hnt)
gain = getgainfromhn(hn,fftfreq)

filebase = constants.outfolder + '/bicone/100evbiconemeas0deg_'
saveinfo(filebase, time, hnt)
print '############################################'
print 'saved bicone info in: ', filebase
print '############################################'
