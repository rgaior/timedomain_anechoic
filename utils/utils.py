import scipy.signal as scp
import ROOT
import numpy as np
import constants

c = constants.c
pi = np.pi

#return the average waveform as a np array [time,amplitude]
def getaveragewf(filename, nroffile):
    f = open(filename, 'r')
    time = np.array([])
    amp = np.array([])
    counter = 0
    for line in f:
        if nroffile != 0:
            if counter > nroffile:
                break
        if counter == 0:
            time = np.asarray(line.split()[::2])
            time = time.astype(np.float)
            amp = np.asarray(line.split()[1::2])
            amp = amp.astype(np.float)
        else:
            ampcur = np.asarray(line.split()[1::2])
            ampcur = ampcur.astype(np.float)
            amp = np.add(amp,ampcur)

        counter = counter +1        
    amp = amp/float(counter)
    wf = np.array([time,amp])
    f.close()
    return wf

#return the average waveform as a np array [time,amplitude]
def getaveragewfbetween(filename, nroffile1, nroffile2):
    f = open(filename, 'r')
    time = np.array([])
    amp = np.array([])
    counter = 0
    counter2 = 0
    for line in f:
        counter = counter +1        
        if counter < nroffile1:
            continue
        elif counter > nroffile2:
            break
        elif counter == nroffile1:
            time = np.asarray(line.split()[::2])
            time = time.astype(np.float)
            amp = np.asarray(line.split()[1::2])
            amp = amp.astype(np.float)
            counter2 = counter2+1
        else:
            ampcur = np.asarray(line.split()[1::2])
            ampcur = ampcur.astype(np.float)
            amp = np.add(amp,ampcur)
            counter2 = counter2+1
    amp = amp/float(counter2)
    wf = np.array([time,amp])
    f.close()
    return wf

#return a single waveform as a np array [time,amplitude]
def getwf(filename, filenr):
    f = open(filename, 'r')
    time = np.array([])
    amp = np.array([])
    counter = 0
    headershift = 0
    for line in f:
        if counter != filenr:
            counter = counter +1
            continue
        else:
            time = np.asarray(line.split()[headershift::2])
            time = time.astype(np.float)
            amp = np.asarray(line.split()[headershift+1::2])
            amp = amp.astype(np.float)
        counter = counter +1        
    wf = np.array([time,amp])
    f.close()
    return wf

#return a single waveform as a np array [time,amplitude]
def printline(filename,filenr):
    f = open(filename, 'r')
    time = np.array([])
    amp = np.array([])
    counter = 0
    for line in f:
        if counter != filenr:
            counter = counter +1
            continue
        else:
            print line.split()[:20]

        counter = counter +1        

def loadnpzfile(filename):
    arrays = np.load(filename)
    x = arrays['arr_0']
    y = arrays['arr_1']
    return [x,y]


#input is a waveform i.e. a np array with [time,amp]
#output is [freq, mag, phase]
def getspec(wf):
    foufou = np.fft.fft(wf[1]) 
    mag = np.absolute(foufou)
    phase = np.arctan2(foufou.imag,foufou.real)
    phase = np.unwrap(phase)
    freq = np.fft.fftfreq(len(wf[0]),wf[0][1]-wf[0][0])
    spec = np.array([freq,mag,phase])
    return spec

def getfft(wf):
    foufou = np.fft.fft(wf[1]) 
    return foufou

def getmagphase(wf):
    foufou = np.fft.fft(wf[1]) 
    magphase = fft_to_magphase(foufou)
    return magphase

def fft_to_spec(fft, timestep):
    mag = np.absolute(fft)
    phase = np.arctan2(fft.imag,fft.real)
    phase = np.unwrap(phase)
    freq = np.fft.fftfreq(len(fft),timestep)
    spec = np.array([freq,mag,phase])
    return spec

def fft_to_magphase(fft):
    mag = np.absolute(fft)
    phase = np.arctan2(fft.imag,fft.real)
    magphase = np.array([mag,phase])
    return magphase

def fft_to_magphaseuw(fft):
    mag = np.absolute(fft)
    phase = np.arctan2(fft.imag,fft.real)
    phase = np.unwrap(phase)
    magphase = np.array([mag,phase])
    return magphase

def magphase_to_fft(magphase):
    real = magphase[0]*np.cos(magphase[1])
    im = magphase[0]*np.sin(magphase[1])
    fft = real+1j*im
    return fft

def dividefft(fft1,fft2):
    spec1 = fft_to_magphase(fft1)
    spec2 = fft_to_magphase(fft2)
    divided = np.array([spec1[0]/spec2[0],spec1[1]-spec2[1]])
    divided = magphase_to_fft(divided)
    return divided

def sqrtfft(fft):
    spec = fft_to_magphaseuw(fft)
    squareroot = np.array([np.sqrt(spec[0]),spec[1]/2])
    squareroot = magphase_to_fft(squareroot)
    return squareroot


def myLPfilter(inp, deltat, fmax):
    fftinp = np.fft.fft(inp)
    freqarray = np.fft.fftfreq(inp.size, deltat)
    filtered = np.array([])
    for fft, freq in zip(fftinp, freqarray):
        if freq > fmax or freq < -fmax:
            filtered = np.append(filtered, 0.)
        else:
            filtered = np.append(filtered, fft)
    filtered[0] = 0
    filtered = np.fft.ifft(filtered)
    return filtered


def myBPfilter(inp, deltat,fmin, fmax):
    fftinp = np.fft.fft(inp)
    freqarray = np.fft.fftfreq(inp.size, deltat)
    filtered = np.array([])
    for fft, freq in zip(fftinp, freqarray):
        if freq > fmax or freq < -fmax:
            filtered = np.append(filtered, 0)
        elif (freq > 0 and freq < fmin):
            filtered = np.append(filtered, 0)
        elif (freq < 0 and freq > -fmin):
            filtered = np.append(filtered, 0)
        else:
            filtered = np.append(filtered, fft)
    filtered[0] = 0
    filtered = np.fft.ifft(filtered)
    return filtered


def readXFfreqgain(filename):    
    f = open(filename, 'r')
    freq = np.array([])
    gain = np.array([])
    counter = 0
    for line in f:
#        print line
#        print line.split()[0], ' ' , line.split()[1]
        if counter > 0:
            freq = np.append(freq,float(line.split()[0]))
            gain = np.append(gain,float(line.split()[1]))
        counter = counter+1
    fg = [freq, gain]
    return fg


def getgraphinarray(tfilename, tgraphname):
    f = ROOT.TFile(tfilename)
    g = f.Get(tgraphname)
    entries = g.GetN()
    y = g.GetY()
    x = g.GetX()
    # xyarr = np.array([])
    xarr = np.array([])
    yarr = np.array([])
    for i in range(entries):
        xarr = np.append(xarr,x[i])
        yarr = np.append(yarr,y[i])
    return [xarr,yarr]


#function definition
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
def bipolar(x, mu, sig):
    bipol = -(x-mu)*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    max = np.max(bipol)
    return bipol/max
def dirac(x, mu):
    indexofmu = int((mu-x[0])/(x[1] -x[0]))
#    print indexofmu
    y = np.zeros(len(x))
    y[indexofmu] = 1
    print 'lenx -' , len(x) , 'len(y) = ', len(y)
    return y
    # bipol = -(x-mu)*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    # max = np.max(bipol)
    # return bipol/max


#computation of hn 
# in the case of two same antennas:
#(refractive index to be added when doing it for ice)
def gethn2antennas(vsrcfft, vrecfft, t, distance):
    dt = t[1] -t[0]
    fftfreq = np.fft.fftfreq(len(vrecfft),dt)
    omega = 2*pi*fftfreq
    jomega = 1j*omega
    jomega[0] = 1
    expterm = np.exp(-jomega*distance/c)
    hnsq = (vrecfft/vsrcfft)*( (2*pi*c)/jomega) * (distance/expterm)
    hn = sqrtfft(hnsq)
    hn[0] = 1
    hnt = np.fft.ifft(hn)
    return [t, hnt]

#computation of hn 
# in the case of two different antennas:
#(refractive index to be added when doing it for ice)
def gethn1antennas(vsrcfft, vrecfft, hnfft, t, distance):
    dt = t[1] -t[0]
    fftfreq = np.fft.fftfreq(len(vrecfft),dt)
    omega = 2*pi*fftfreq
    jomega = 1j*omega
    jomega[0] = 1
    expterm = np.exp(-jomega*distance/c)
#    print np.where(hnfft.real == 0)[0]    
#    print np.isnan(1/hnfft.real)
#    print 1/hnfft
    hn = (vrecfft/vsrcfft)*( (2*pi*c)/jomega) * (distance/expterm) * (1/hnfft)
    hn[0] = 1
    hnt = np.fft.ifft(hn)
    return [t, hnt]

#get effective area from hn
def getaefffromhn(hnfft):
    return np.absolute(hnfft)*np.absolute(hnfft)

#get gain from hn
def getgainfromhn(hnfft,freq):
    aeff = getaefffromhn(hnfft)
    gain = (4*pi/(c*c))*freq*freq*aeff
    return gain


#input filebase, hnt, time
#saves: hnt, hn, aeff, gain, and hnt 
def saveinfo(filebase, time, hnt):
    #save hnt
    hntfilename = filebase + 'hnt'
    np.savez(hntfilename, time, hnt.real)   
    #save aeff
    hn = np.fft.fft(hnt)
    fftfreq = np.fft.fftfreq(len(hnt),time[1] - time[0]) 
    hnfilename = filebase + 'hn'
    np.savez(hnfilename, fftfreq, hn)   
    #save aeff
    aeff = getaefffromhn(hn)
    aefffilename = filebase + 'aeff'
    np.savez(aefffilename, fftfreq, aeff)
    #save gain 
    gain = getgainfromhn(hn, fftfreq)
    gainfilename = filebase + 'gain'
    np.savez(gainfilename, fftfreq, gain)

    

#shifts the waveform w.r.t. its maximum
def shiftwf(x,y):
    indexofmax = np.argmax(y)
    timeofmax = x[indexofmax]
    x = x - timeofmax
    return x
