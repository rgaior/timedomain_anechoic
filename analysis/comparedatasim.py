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
c = constants.c
pi = constants.pi
distance = 3.53 #m


fmin = 0e9
fmax = 1e9

#get the bicone h_N
biconefile = constants.outfolder +'/ bicone/100evbiconemeas0deg_hnt.npz'
biconeh = loadnpzfile(biconefile)
biconetime = biconeh[0]
biconehnt = biconeh[1]
dtexp = biconetime[1] - biconetime[0]
biconetime = biconetime - biconetime[0]
filtered = myBPfilter(biconehnt,dtexp, fmin,fmax) 


#get the simulated bicone h_N
sbiconefile = constants.simfolder +'/bicone/sim_0_timehnt.npz'
sbiconeh = loadnpzfile(sbiconefile)
sbiconetime = sbiconeh[0]
sbiconehnt = sbiconeh[1]
#renormalize the simulation due to the different sampling
#(here it is tricky but the gain is OK the time has to be normalized)
dtsim = sbiconetime[1] - sbiconetime[0]
dtfactor = dtexp/dtsim
sbiconehnt = sbiconehnt*dtfactor
sfiltered = myBPfilter(sbiconehnt,dtsim, fmin,fmax) 


#ara hn
angle = 0
arafile = constants.outfolder +'/ara/100evvpoltoptaiwan0deg_hnt.npz'
#arafile = constants.outfolder +'/ara/100evvpolbotttaiwan180deg_hnt.npz'
arah = loadnpzfile(arafile)
aratime = arah[0]
arahnt = arah[1]
dtexp = aratime[1] - aratime[0]
aratime = aratime - aratime[0]
arafiltered = myBPfilter(arahnt,dtexp, fmin,fmax) 


#get the simulated ara h_N
sarafile = constants.simfolder + '/ara/sim_0_timehnt.npz'
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
newtime2 = shiftwf(saratime,sarafiltered)

#plt.plot(biconetime,biconehnt)
#plt.plot(sbiconetime,sbiconehnt)
plt.plot(newtime,arafiltered)
plt.plot(newtime2,sarafiltered)




plt.show()

