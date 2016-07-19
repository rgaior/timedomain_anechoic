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

 #constants
c = constants.c
pi = constants.pi
distance = 3.53 #m


fmin = 0e9
fmax = 1e9


#ara hn
angle = 0
arafile = constants.outfolder + '/ara/100evvpolbotttaiwanmean0deg_hnt.npz'
arafile2 = constants.outfolder + '/ara/100evvpoltoptaiwanmean0deg_hnt.npz'
arah = loadnpzfile(arafile)
aratime = arah[0]
arahnt = arah[1]
dtexp = aratime[1] - aratime[0]
aratime = aratime - aratime[0]
arafiltered = myBPfilter(arahnt,dtexp, fmin,fmax) 

arah2 = loadnpzfile(arafile2)
aratime2 = arah2[0]
arahnt2 = arah2[1]
dtexp2 = aratime2[1] - aratime2[0]
aratime2 = aratime2 - aratime2[0]
arafiltered2 = myBPfilter(arahnt2,dtexp2, fmin,fmax) 


#get the simulated ara h_N
sarafile = constants.simfolder +'/ara/sim_0_timehnt.npz'
sarah = loadnpzfile(sarafile)
saratime = sarah[0]
sarahnt = sarah[1]
#renormalize the simulation due to the different sampling
#(here it is tricky but the gain is OK the time has to be normalized)
dtsim = saratime[1] - saratime[0]
dtfactor = dtexp/dtsim
sarahnt = sarahnt*dtfactor
sarafiltered = myBPfilter(sarahnt,dtsim, fmin,fmax) 
 



#newtime = shiftwf(biconetime,filtered)
#newtime2 = shiftwf(sbiconetime,sfiltered)
newtime = shiftwf(aratime,arafiltered)
newtime2 = shiftwf(aratime2,arafiltered2)
newtime3 = shiftwf(saratime,sarafiltered)



f1 = plt.figure(1,figsize=(12,10))
#plt.plot(newtime*1e9,arafiltered,lw=2, label=r'measured $\theta$ = 0 deg')
#plt.plot(newtime2*1e9,arafiltered2,lw=2, label=r'measured $\theta$ = 180 deg')
#plt.plot(newtime*1e9,arafiltered,lw=2, label=r'measured (made in Japan)')
#plt.plot(newtime2*1e9,arafiltered2,lw=2, label=r'measured (made in Taiwan)')
plt.plot(newtime*1e9,arafiltered,lw=2, label=r'measured (bottom)')
plt.plot(newtime2*1e9,arafiltered2,lw=2, label=r'measured (top)')
plt.plot(newtime3*1e9,sarafiltered,lw=2,ls='-', label='simulated')
plt.xlim(-1,20)
plt.xlabel('time [ns]',fontsize=20)
plt.ylabel('h$_{N}$ [a.u.]',fontsize=20)
plt.legend(prop={'size':30}) 
plt.xticks(fontsize = 20)                                                                                                                                     
plt.yticks(fontsize = 20)                                                                                                                                    


f2 = plt.figure(2,figsize=(12,10))
#sim gain
sgarafile = constants.simfolder + '/ara/sim_0_timegain.npz'
sgara = loadnpzfile(sgarafile)
sgarafreq = sgara[0]
sgaragain = sgara[1]

#sim gain
garafile = constants.outfolder + '/ara/100evvpolbotttaiwan0deg_gain.npz'
garafile2 = constants.outfolder + 'ara/100evvpoltoptaiwan0deg_gain.npz'
gara = loadnpzfile(garafile)
garafreq = gara[0]
garagain = gara[1]
gara2 = loadnpzfile(garafile2)
garafreq2 = gara2[0]
garagain2 = gara2[1]
hsize = len(garagain)/2
plt.xlim(0.1,1)
plt.ylim(-15,7)
plt.xlabel('frequency [GHz]',fontsize=20)
plt.ylabel('Gain [dBi]',fontsize=20)
#plt.plot(garafreq[:hsize]/1e9,10*np.log10(garagain[:hsize]),lw=2,label=r'measured $\theta$ = 0 deg')
#plt.plot(garafreq2[:hsize]/1e9,10*np.log10(garagain2[:hsize]),lw=2,label=r'measured $\theta$ = 180 deg')
#plt.plot(garafreq[:hsize]/1e9,10*np.log10(garagain[:hsize]),lw=2,label=r'measured (made in Chiba)')
#plt.plot(garafreq2[:hsize]/1e9,10*np.log10(garagain2[:hsize]),lw=2,label=r'measured (made in Taiwan)')
plt.plot(garafreq[:hsize]/1e9,10*np.log10(garagain[:hsize]),lw=2,label=r'measured (bottom)')
plt.plot(garafreq2[:hsize]/1e9,10*np.log10(garagain2[:hsize]),lw=2,label=r'measured (top)')
plt.plot(sgarafreq[:hsize]/1e9,10*np.log10(sgaragain[:hsize]),ls='-',lw=2,label='simulated')
plt.legend(prop={'size':28}) 
plt.xticks(fontsize = 20)                                                                                                                                     
plt.yticks(fontsize = 20)                                                                                                                                    
#f1.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/araBTTThnt.png') 
#f2.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/araBTTTgain.png') 

#plt.plot(aratime,arahnt)
#plt.plot(saratime,sarhnt)
# plt.plot(newtime,arafiltered)
# plt.plot(newtime2,-arafiltered2)
# plt.plot(newtime3,sarafiltered)




plt.show()

