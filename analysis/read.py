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

day = sys.argv[1]
runnr = sys.argv[2]
radioorpulse = sys.argv[3]

#constant
pi = math.pi
c = constants.c
distance = 3.53 #m

date = '2015-05-'+str(day)
run = int(runnr) 

fpulse = constants.datafolder + '/Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel1.data'
fradio = constants.datafolder + 'Data_'+date+'/Run_'+str(run)+'/'+date+'_Run_'+str(run)+'_channel2.data'
nrofev = 10
wfpulse = getaveragewf(fpulse,1)
wfradio = getaveragewf(fradio,1)
vrecfft = np.fft.fft(wfradio[1])
vsrcfft = np.fft.fft(wfpulse[1])
deltat = wfradio[0][1]-wfradio[0][0]
fftfreq = np.fft.fftfreq(len(vsrcfft),deltat)

f, (ax1,ax2) = plt.subplots(2,1)
f.set_size_inches(8,8)

if radioorpulse== 'radio':
    ax1.plot(wfradio[0],wfradio[1] ,label='radio')
    ax2.plot(fftfreq/1e9, np.absolute(vrecfft),label='radio')
if radioorpulse== 'pulse':
    ax1.plot(wfpulse[0],wfpulse[1] ,label='radio')
    ax2.plot(fftfreq/1e9, np.absolute(vsrcfft),label='radio')
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

ax1.set_xlabel('time [s] ')
ax2.set_xlabel('frequency [GHz] ')
ax1.set_ylabel('amplitude [V] ')
ax2.set_ylabel('spectrum [a.u.] ')

plt.legend()
plt.show()
