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
import rundef
from utils import *


#get the bicone h_N
biconefile = constants.outfolder + '/bicone/100evbiconemeas0deg_hn.npz'
biconeh = loadnpzfile(biconefile)
biconetime = biconeh[0]
biconehn = biconeh[1]

#get thru data:
thrufile = constants.outfolder + '/thru/thruvgain.npz'
thrugain = loadnpzfile(thrufile)
vgainthru = thrugain[1]
fftfreq = thrugain[0] 

meas = rundef.vpoltoptaiwan
#meas = rundef.vpolbottchiba
#meas = rundef.vpolbotttaiwan
#run to compute
name = meas[0]
date = meas[1]

#for run,angle in zip(meas[2][:8],meas[3][:8]): 
for run,angle in zip(meas[2],meas[3]): 
    outfilebase = constants.outfolder+ '/ara/100ev' + name
    fpulse = constants.datafolder+ '/Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel1.data'
    fradio = fpulse = constants.datafolder+ '/Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel2.data'
    nrofev = 100
    wfpulse = getaveragewf(fpulse,nrofev)
    wfradio = getaveragewf(fradio,nrofev)
    vrecfft = np.fft.fft(wfradio[1])
    vsrcfft = np.fft.fft(wfpulse[1])*vgainthru


#get the hn with the bicone hn:
    time = wfpulse[0]
    thnt = gethn1antennas(vsrcfft, vrecfft, biconehn, wfpulse[0], constants.distance)
    hnt = myBPfilter(thnt[1], time[1] - time[0],0.1e9, 1e9)
    #    hnt = thnt[1]
    hn = np.fft.fft(hnt)
    outfilebase = outfilebase + str(angle) + 'deg_'
#save into files
    saveinfo(outfilebase,time,hnt)
