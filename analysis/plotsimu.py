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

fgain0 = constants.simfolder +'/ara/sim_0_timegain.npz'
fgain30 = constants.simfolder +'/ara/sim_30_timegain.npz'
fgain50 = constants.simfolder +'/ara/sim_50_timegain.npz'

fhnt0 = constants.simfolder +'/ara/sim_0_timehnt.npz'
fhnt30 = constants.simfolder +'/ara/sim_30_timehnt.npz'
fhnt50 = constants.simfolder +'/ara/sim_50_timehnt.npz'

gain0 = loadnpzfile(fgain0)
gain30 = loadnpzfile(fgain30)
gain50 = loadnpzfile(fgain50)


f1 = plt.figure(1,figsize=(15,10))
plt.plot(gain0[0]/1e9,10*np.log10(gain0[1]),lw=2,label='0 deg.')
plt.plot(gain30[0]/1e9,10*np.log10(gain30[1]),lw=2,label='30 deg.')
plt.plot(gain50[0]/1e9,10*np.log10(gain50[1]),lw=2,label='50 deg.')
plt.xlim(0.1,1)
plt.ylim(-15,5)
plt.xlabel('frequency [GHz]',fontsize=20)
plt.ylabel('gain [dBi]',fontsize=20)
plt.legend(prop={'size':30}) 
plt.xticks(fontsize = 20) 
plt.yticks(fontsize = 20)                        


hnt0 = loadnpzfile(fhnt0)
hnt30 = loadnpzfile(fhnt30)
hnt50 = loadnpzfile(fhnt50)
dt = hnt0[0][1] - hnt0[0][0]
fhnt0 = myBPfilter(hnt0[1],dt,fmin,fmax)
fhnt30 = myBPfilter(hnt30[1],dt,fmin,fmax)
fhnt50 = myBPfilter(hnt50[1],dt,fmin,fmax)

f2 = plt.figure(2,figsize=(15,10))
plt.plot(hnt0[0]*1e9,fhnt0,lw=2,label='0 deg.')
plt.plot(hnt30[0]*1e9,fhnt30,lw=2,label='30 deg.')
plt.plot(hnt50[0]*1e9,fhnt50,lw=2,label='50 deg.')
plt.xlim(0,20)
#plt.ylim(-15,5)
plt.xlabel('time [ns]',fontsize=20)
plt.ylabel('h$_{N}$ [a.u.]',fontsize=20)
plt.legend(prop={'size':30}) 
plt.xticks(fontsize = 20) 
plt.yticks(fontsize = 20)                        


f1.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/gainarasim.png') 
f2.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/hntarasim.png') 
                                   
                                                                      
plt.show()
