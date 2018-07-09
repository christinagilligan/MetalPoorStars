#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:21:30 2018

@author: christinagilligan
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import matplotlib

Bmag=[]
Vmag=[]
Gmag=[]
Jmag=[]
Hmag=[]
Kmag=[]
FeH=[]
Dis=[]
DisLow=[]
DisHigh=[]

filename='metalpoorstarsfinished.csv'

f = open(filename)
csv_f = csv.reader(f)
next(csv_f)
data = np.array(list(csv_f))
Name=np.array(data[:,0],dtype=str)
names=list(Name)
Bmag=np.array(data[:,1],dtype=float)
Vmag=np.array(data[:,2],dtype=float)
Gmag=np.array(data[:,3],dtype=float)
Jmag=np.array(data[:,4],dtype=float)
Hmag=np.array(data[:,5],dtype=float)
Kmag=np.array(data[:,6],dtype=float)
FeH=np.array(data[:,7],dtype=float)
Dis=np.array(data[:,8],dtype=float)
DisLow=np.array(data[:,9],dtype=float)
DisHigh=np.array(data[:,10],dtype=float)

MB=Bmag-5*np.log10(Dis)+5
MBLow=Bmag-5*np.log10(DisLow)+5
MBHigh=Bmag-5*np.log10(DisHigh)+5

MV=Vmag-5*np.log10(Dis)+5
MVLow=Vmag-5*np.log10(DisLow)+5
MVHigh=Vmag-5*np.log10(DisHigh)+5

MG=Gmag-5*np.log10(Dis)+5
MGLow=Gmag-5*np.log10(DisLow)+5
MGHigh=Gmag-5*np.log10(DisHigh)+5

MJ=Jmag-5*np.log10(Dis)+5
MJLow=Jmag-5*np.log10(DisLow)+5
MJHigh=Jmag-5*np.log10(DisHigh)+5

MH=Hmag-5*np.log10(Dis)+5
MHLow=Hmag-5*np.log10(DisLow)+5
MHHigh=Hmag-5*np.log10(DisHigh)+5

MK=Kmag-5*np.log10(Dis)+5
MKLow=Kmag-5*np.log10(DisLow)+5
MKHigh=Kmag-5*np.log10(DisHigh)+5

BIso1=[]
VIso1=[]
JIso1=[]
HIso1=[]
KIso1=[]

file = open('isochrone-0.79.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso1.append(line[6])
        VIso1.append(line[7])
        JIso1.append(line[10])
        HIso1.append(line[11])
        KIso1.append(line[12])

BIso1=np.array(BIso1,dtype=float)
VIso1=np.array(VIso1,dtype=float)
JIso1=np.array(JIso1,dtype=float)
HIso1=np.array(HIso1,dtype=float)
KIso1=np.array(KIso1,dtype=float)

BIso2=[]
VIso2=[]
JIso2=[]
HIso2=[]
KIso2=[]

file = open('isochrone-1.99.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso2.append(line[6])
        VIso2.append(line[7])
        JIso2.append(line[10])
        HIso2.append(line[11])
        KIso2.append(line[12])

BIso2=np.array(BIso2,dtype=float)
VIso2=np.array(VIso2,dtype=float)
JIso2=np.array(JIso2,dtype=float)
HIso2=np.array(HIso2,dtype=float)
KIso2=np.array(KIso2,dtype=float)

BIso25=[]
VIso25=[]
JIso25=[]
HIso25=[]
KIso25=[]

file = open('isochrone-2.49.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso25.append(line[6])
        VIso25.append(line[7])
        JIso25.append(line[10])
        HIso25.append(line[11])
        KIso25.append(line[12])

BIso25=np.array(BIso25,dtype=float)
VIso25=np.array(VIso25,dtype=float)
JIso25=np.array(JIso25,dtype=float)
HIso25=np.array(HIso25,dtype=float)
KIso25=np.array(KIso25,dtype=float)

BIso15=[]
VIso15=[]
JIso15=[]
HIso15=[]
KIso15=[]

file = open('isochrone-1.29.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso15.append(line[6])
        VIso15.append(line[7])
        JIso15.append(line[10])
        HIso15.append(line[11])
        KIso15.append(line[12])

BIso15=np.array(BIso15,dtype=float)
VIso15=np.array(VIso15,dtype=float)
JIso15=np.array(JIso15,dtype=float)
HIso15=np.array(HIso15,dtype=float)
KIso15=np.array(KIso15,dtype=float)

BIso0=[]
VIso0=[]
JIso0=[]
HIso0=[]
KIso0=[]

file = open('isochrone0.01.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso0.append(line[6])
        VIso0.append(line[7])
        JIso0.append(line[10])
        HIso0.append(line[11])
        KIso0.append(line[12])

BIso0=np.array(BIso0,dtype=float)
VIso0=np.array(VIso0,dtype=float)
JIso0=np.array(JIso0,dtype=float)
HIso0=np.array(HIso0,dtype=float)
KIso0=np.array(KIso0,dtype=float)

BIso05=[]
VIso05=[]
JIso05=[]
HIso05=[]
KIso05=[]

file = open('isochrone-0.29.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso05.append(line[6])
        VIso05.append(line[7])
        JIso05.append(line[10])
        HIso05.append(line[11])
        KIso05.append(line[12])

BIso05=np.array(BIso05,dtype=float)
VIso05=np.array(VIso05,dtype=float)
JIso05=np.array(JIso05,dtype=float)
HIso05=np.array(HIso05,dtype=float)
KIso05=np.array(KIso05,dtype=float)

BIso049=[]
VIso049=[]
JIso049=[]
HIso049=[]
KIso049=[]

file = open('isochrone-0.49.txt')
for line in file:
    if '#' not in line:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        BIso049.append(line[6])
        VIso049.append(line[7])
        JIso049.append(line[10])
        HIso049.append(line[11])
        KIso049.append(line[12])

BIso049=np.array(BIso049,dtype=float)
VIso049=np.array(VIso049,dtype=float)
JIso049=np.array(JIso049,dtype=float)
HIso049=np.array(HIso049,dtype=float)
KIso049=np.array(KIso049,dtype=float)

FirstBinIndex=np.flatnonzero(FeH<-1.5)

a=np.flatnonzero(-1.5<FeH)
b=np.flatnonzero(FeH<-1.0)
SecondBinIndex=np.intersect1d(a,b)

a=np.flatnonzero(-1.0<FeH)
b=np.flatnonzero(FeH<-0.5)
ThirdBinIndex=np.intersect1d(a,b)


a=np.flatnonzero(-0.5<FeH)
b=np.flatnonzero(FeH<0)
FourthBinIndex=np.intersect1d(a,b)

FifthBinIndex=np.flatnonzero(FeH>0)
def myplot(choicelist):
    absmag = 0
    lowmag = 0
    highmag = 0
    absiso0 = 0
    absiso05 = 0
    absiso1 = 0
    absiso15 =0
    absiso2 = 0
    absiso049 = 0
    if choicelist[0] == 'B':
        absmag=MB
        lowmag=MBLow
        highmag=MBHigh
        absiso0=BIso0
        absiso05=BIso05
        absiso1=BIso1
        absiso15=BIso15
        absiso2=BIso2
        absiso049=BIso049
    if choicelist[0] == 'V':
        absmag=MV
        lowmag=MVLow
        highmag=MVHigh
        absiso0=VIso0
        absiso05=VIso05
        absiso1=VIso1
        absiso15=VIso15
        absiso2=VIso2
        absiso049=VIso049
    if choicelist[0] == 'J':
        absmag=MJ
        lowmag=MJLow
        highmag=MJHigh
        absiso0=JIso0
        absiso05=JIso05
        absiso1=JIso1
        absiso15=JIso15
        absiso2=JIso2
        absiso049=JIso049
    if choicelist[0] == 'H':
        absmag=MH
        lowmag=MHLow
        highmag=MHHigh
        absiso0=HIso0
        absiso05=HIso05
        absiso1=HIso1
        absiso15=HIso15
        absiso2=HIso2
        absiso049=HIso049
    if choicelist[0] == 'K':
        absmag=MK
        lowmag=MKLow
        highmag=MKHigh
        absiso0=KIso0
        absiso05=KIso05
        absiso1=KIso1
        absiso15=KIso15
        absiso2=KIso2
        absiso049=KIso049
    if choicelist[1] == 'B':
        colormag1=Bmag
        firstiso0=BIso0
        firstiso05=BIso05
        firstiso1=BIso1
        firstiso15=BIso15
        firstiso2=BIso2
        firstiso049=BIso049
    if choicelist[1] == 'V':
        colormag1=Vmag
        firstiso0=VIso0
        firstiso05=VIso05
        firstiso1=VIso1
        firstiso15=VIso15
        firstiso2=VIso2
        firstiso049=VIso049
    if choicelist[1] == 'J':
        colormag1=Jmag
        firstiso0=JIso0
        firstiso05=JIso05
        firstiso1=JIso1
        firstiso15=JIso15
        firstiso2=JIso2
        firstiso049=JIso049
    if choicelist[1] == 'H':
        colormag1=Hmag
        firstiso0=HIso0
        firstiso05=HIso05
        firstiso1=HIso1
        firstiso15=HIso15
        firstiso2=HIso2
        firstiso049=HIso049
    if choicelist[1] == 'K':
        colormag1=Kmag
        firstiso0=KIso0
        firstiso05=KIso05
        firstiso1=KIso1
        firstiso15=KIso15
        firstiso2=KIso2
        firstiso049=KIso049
    if choicelist[2] == 'B':
        colormag2=Bmag
        secondiso0=BIso0
        secondiso05=BIso05
        secondiso1=BIso1
        secondiso15=BIso15
        secondiso2=BIso2
        secondiso049=BIso049
    if choicelist[2] == 'V':
        colormag2=Vmag
        secondiso0=VIso0
        secondiso05=VIso05
        secondiso1=VIso1
        secondiso15=VIso15
        secondiso2=VIso2
        secondiso049=VIso049
    if choicelist[2] == 'J':
        colormag2=Jmag
        secondiso0=JIso0
        secondiso05=JIso05
        secondiso1=JIso1
        secondiso15=JIso15
        secondiso2=JIso2
        secondiso049=JIso049
    if choicelist[2] == 'H':
        colormag2=Hmag
        secondiso0=HIso0
        secondiso05=HIso05
        secondiso1=HIso1
        secondiso15=HIso15
        secondiso2=HIso2
        secondiso049=HIso049
    if choicelist[2] == 'K':
        colormag2=Kmag 
        secondiso0=KIso0
        secondiso05=KIso05
        secondiso1=KIso1
        secondiso15=KIso15
        secondiso2=KIso2
        secondiso049=KIso049
    norm = matplotlib.colors.Normalize(vmin=np.min(FeH), vmax=np.max(FeH), clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.coolwarm)
    mapper.set_array(FeH)
    plt.figure()
    plt.errorbar(colormag1-colormag2, absmag, yerr=[absmag-lowmag, highmag-absmag], fmt = 'none', marker=None, mew=10, c=mapper.to_rgba(FeH))    

    plt.scatter(colormag1-colormag2, absmag,c=mapper.to_rgba(FeH),edgecolor='face',s=50)

#    for i, (color1, color2, absm, mag, maglow, maghigh, metal) in enumerate(zip(colormag1, colormag2, absmag, MJ, MJLow, MJHigh, FeH)):
#        color = mapper.to_rgba(metal)
#        lowerr=mag-maglow
#        higherr=maghigh-mag
#        print(lowerr)
#        print(higherr)
#        plt.errorbar(color1-color2, absm, yerr=[-lowerr, -higherr], linestyle='', c=color)

#   plot a specific point with a big black point to check a specific star's position on the HR diagram
#    abs=8.808-5*np.log10(71.50512977)+5
#    plt.scatter(8.808-8.33,abs,c='k',s=75)

    plt.plot(firstiso0-secondiso0, absiso0,c=mapper.to_rgba(0.01))#fifth
    plt.plot(firstiso05-secondiso05, absiso05,c=mapper.to_rgba(-0.29))#fourth
    plt.plot(firstiso1-secondiso1, absiso1,c=mapper.to_rgba(-0.79))#third
    plt.plot(firstiso15-secondiso15, absiso15,c=mapper.to_rgba(-1.29))#second
    plt.plot(firstiso2-secondiso2, absiso2,c=mapper.to_rgba(-1.99))#first
    plt.plot(firstiso049-secondiso049, absiso049,c=mapper.to_rgba(-0.49))

    plt.gca().invert_yaxis()
    plt.xlabel(str(choicelist[1])+'-'+str(choicelist[2]))
    plt.ylabel('M_'+str(choicelist[0]))
#    plt.legend(numpoints = 1 )
    cbar = plt.colorbar(mapper)
    cbar.set_label('[Fe/H]',rotation=270,labelpad=10)
    
    plt.show()  
