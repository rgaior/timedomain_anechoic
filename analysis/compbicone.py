import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import sys
import math
sys.path.append('/home/romain/ara/timedomain/measurement/script/utils/')
from utils import *
import constants
import rundef

#constant
c = constants.c
pi = constants.pi
distance = 3.53 #m


fmin = 0e9
fmax = 1e9

#get the bicone h_N
biconefile = '/home/romain/ara/timedomain/measurement/script/results/bicone/100evbiconemeas0deg_hnt.npz'
biconeh = loadnpzfile(biconefile)
biconetime = biconeh[0]
biconehnt = biconeh[1]
dtexp = biconetime[1] - biconetime[0]
biconetime = biconetime - biconetime[0]
filtered = myBPfilter(biconehnt,dtexp, fmin,fmax) 


#get the simulated bicone h_N
sbiconefile = '/home/romain/ara/timedomain/measurement/script/results/simu/bicone/sim_0_timehnt.npz'
sbiconeh = loadnpzfile(sbiconefile)
sbiconetime = sbiconeh[0]
sbiconehnt = sbiconeh[1]
#renormalize the simulation due to the different sampling
#(here it is tricky but the gain is OK the time has to be normalized)
dtsim = sbiconetime[1] - sbiconetime[0]
dtfactor = dtexp/dtsim
sbiconehnt = sbiconehnt*dtfactor
sfiltered = myBPfilter(sbiconehnt,dtsim, fmin,fmax) 


newtime = shiftwf(biconetime,filtered)
newtime2 = shiftwf(sbiconetime,sfiltered)
#newtime = shiftwf(aratime,arafiltered)
#newtime2 = shiftwf(saratime,sarafiltered)

f1 = plt.figure(1,figsize=(12,10))
#plt.plot(biconetime,biconehnt)
#plt.plot(sbiconetime,sbiconehnt)
plt.plot(newtime*1e9,filtered,lw=2, label='measured')
plt.plot(newtime2*1e9,sfiltered,lw=2,ls='-', label='simulated')
plt.xlim(-1,20)
plt.xlabel('time [ns]',fontsize=20)
plt.ylabel('h$_{N}$ [a.u.]',fontsize=20)
plt.legend(prop={'size':30}) 
plt.xticks(fontsize = 20)                                                                                                                                     
plt.yticks(fontsize = 20)                                                                                                                                    
f2 = plt.figure(2,figsize=(12,10))
#sim gain
sgbiconefile = '/home/romain/ara/timedomain/measurement/script/results/simu/bicone/sim_0_timegain.npz'
sgbicone = loadnpzfile(sgbiconefile)
sgbiconefreq = sgbicone[0]
sgbiconegain = sgbicone[1]

#sim gain
gbiconefile = '/home/romain/ara/timedomain/measurement/script/results/bicone/100evbiconemeas0deg_gain.npz'
gbicone = loadnpzfile(gbiconefile)
gbiconefreq = gbicone[0]
gbiconegain = gbicone[1]
hsize = len(gbiconegain)/2
plt.xlim(0.1,1)
plt.ylim(-10,5)
plt.xlabel('frequency [GHz]',fontsize=20)
plt.ylabel('Gain [dBi]',fontsize=20)
plt.plot(gbiconefreq[:hsize]/1e9,10*np.log10(gbiconegain[:hsize]),lw=2,label='measured')
plt.plot(sgbiconefreq[:hsize]/1e9,10*np.log10(sgbiconegain[:hsize]),ls='-',lw=2,label='simulated')
plt.legend(prop={'size':30}) 
plt.xticks(fontsize = 20)                                                                                                                                     
plt.yticks(fontsize = 20)                                                                                                                                    
f1.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/biconehnt.png') 
f2.savefig('/home/romain/ara/timedomain/measurement/script/plots/20150916/biconegain.png') 


plt.show()

