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

#meas = rundef.vpoltoptaiwan
#meas = rundef.vpolbottchiba
meas = rundef.vpolbotttaiwan
#run to compute
name = meas[0]
date = meas[1]
size = len(meas[2])
for run,angle in zip(meas[2][:size/4],meas[3][:size/4]): 
#for run,angle in zip(meas[2][0:2],meas[3][0:2]): 
    infilebase = constants.outfolder + '/ara/100ev' + name
    infile0 = infilebase + str(angle) + 'deg_' + 'hnt.npz'
    if angle == 0:
        otherangle = 180
        otherrun = run + otherangle/10
        hntbase = loadnpzfile(infile0)
        infile1 = infilebase + str(otherangle) + 'deg_' + 'hnt.npz'
        hntbase1 = loadnpzfile(infile1)
        meanhnt = np.add(hntbase[1],-hntbase1[1])
        meanhnt = meanhnt/2
        outfile = infilebase + 'mean' + str(angle) + 'deg_'
        saveinfo(outfile,hntbase[0],meanhnt)
        # plt.plot(hntbase[0],hntbase[1])
        # plt.plot(hntbase1[0],-hntbase1[1])
        # plt.plot(hntbase[0],meanhnt)
        #        print 'angle = ', angle, 'other abgke = ', otherangle, ' run = ' , run , ' itherrun =' , otherrun
    else:
        otherangle1 = 180-angle
        otherrun1 = run + otherangle1/10
        otherangle2 = 180+angle
        otherrun2 = run + otherangle2/10
        otherangle3 = 360-angle
        otherrun3 = run + otherangle3/10
        hntbase = loadnpzfile(infile0)
        infile1 = infilebase + str(otherangle1) + 'deg_' + 'hnt.npz'
        hntbase1 = loadnpzfile(infile1)
        infile2 = infilebase + str(otherangle2) + 'deg_' + 'hnt.npz'
        hntbase2 = loadnpzfile(infile2)
        infile3 = infilebase + str(otherangle3) + 'deg_' + 'hnt.npz'
        hntbase3 = loadnpzfile(infile3)
        meanhnt = np.add(hntbase[1],-hntbase1[1])
        meanhnt = np.add(meanhnt,-hntbase2[1])
        meanhnt = np.add(meanhnt,hntbase3[1])
        meanhnt = meanhnt/4
        outfile = infilebase + 'mean' + str(angle) + 'deg_'
        saveinfo(outfile,hntbase[0],meanhnt)
        # plt.plot(hntbase[0],hntbase[1])
        # plt.plot(hntbase1[0],-hntbase1[1])
        # plt.plot(hntbase2[0],-hntbase2[1])
        # plt.plot(hntbase3[0],hntbase3[1])
        # plt.plot(hntbase[0],meanhnt,'--')
        

#        print 'angle = ', angle, ' other abgke = ', otherangle, ' other abgke2 = ', otherangle2, ' other abgke3 = ', otherangle3 
#        print ' run = ' , run , ' otherrun1 =' , otherrun1,' otherrun2 =' , otherrun2,' otherrun3 =' , otherrun3
        
plt.show()        

