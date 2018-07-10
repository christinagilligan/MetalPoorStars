#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:18:50 2018

@author: christinagilligan
"""

#same as abundanceCalc.py except it compares it to an intermediate metallicity star, TYC6963-610-1

import csv
import numpy as np
import matplotlib.pyplot as plt

wavelength_star=[]
ID_star=[]
EP_star=[]
logGF_star=[]
EWin_star=[]
logRWin_star=[]
abund_star=[]
delavg_star=[]

file = open('fe.b')
#print(file.read())
for line in file:
    if 'correl' not in line and 'avg' not in line and 'abund' not in line and '/' not in line and 'No' not in line and 'Fe' not in line and len(line.strip())!=0:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        wavelength_star.append(line[0])
        ID_star.append(line[1])
        EP_star.append(line[2])
        logGF_star.append(line[3])
        EWin_star.append(line[4])
        logRWin_star.append(line[5])
        abund_star.append(line[6])
        delavg_star.append(line[7])
        #data =np.array(np.asarray(line),dtype=float)

wavelength_star=np.array(wavelength_star,dtype=float)
ID_star=np.array(ID_star,dtype=float)
EP_star=np.array(EP_star,dtype=float)
logGF_star=np.array(logGF_star,dtype=float)
EWin_star=np.array(EWin_star,dtype=float)
logRWin_star=np.array(logRWin_star,dtype=float)
abund_star=np.array(abund_star,dtype=float)
delavg_star=np.array(delavg_star,dtype=float)

#NOTE: Sun file doesn't have the ID column
wavelength_sun=[]
ID_sun=[]
EP_sun=[]
logGF_sun=[]
EWin_sun=[]
logRWin_sun=[]
abund_sun=[]
delavg_sun=[]

file = open('fe.bTYC6963-610-1')
#print(file.read())
for line in file:
    if 'correl' not in line and 'avg' not in line and 'abund' not in line and '/' not in line and 'No' not in line and 'Fe' not in line and len(line.strip())!=0:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        wavelength_sun.append(line[0])
	ID_sun.append(line[1])
        EP_sun.append(line[2])
        logGF_sun.append(line[3])
        EWin_sun.append(line[4])
        logRWin_sun.append(line[5])
        abund_sun.append(line[6])
        delavg_sun.append(line[7])
        #data =np.array(np.asarray(line),dtype=float)

wavelength_sun=np.array(wavelength_sun,dtype=float)
EP_sun=np.array(EP_sun,dtype=float)
logGF_sun=np.array(logGF_sun,dtype=float)
EWin_sun=np.array(EWin_sun,dtype=float)
logRWin_sun=np.array(logRWin_sun,dtype=float)
abund_sun=np.array(abund_sun,dtype=float)
delavg_sun=np.array(delavg_sun,dtype=float)

feIindex=np.flatnonzero(ID_star==26.0)

feIIindex=np.flatnonzero(ID_star==26.1)

feIwavelengths=wavelength_star[feIindex]

feIIwavelengths=wavelength_star[feIIindex]

deltaabFeI=[]
EPFeI=[]
EWFeI=[]

for i in range(len(feIwavelengths)):
    wavelength=feIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabFeI.append(np.float(star_abund-sun_abund))
        EPFeI.append(EPs)
        EWFeI.append(EWs)
    
deltaabFeI=np.array(deltaabFeI,dtype=float)
EPFeI=np.array(EPFeI,dtype=float)
EWFeI=np.array(EWFeI,dtype=float)  

deltaabFeII=[]
EPFeII=[]
EWFeII=[]

for i in range(len(feIIwavelengths)):
    wavelength=feIIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabFeII.append(np.float(star_abund-sun_abund))
        EPFeII.append(EPs)
        EWFeII.append(EWs)
    
deltaabFeII=np.array(deltaabFeII,dtype=float)
EPFeII=np.array(EPFeII,dtype=float)
EWFeII=np.array(EWFeII,dtype=float)  
    
#Graphs to check for trends

plt.figure()
plt.scatter(EWFeI,deltaabFeI,c='k',marker='.')
plt.title('FeI')
plt.xlabel('EW')
plt.ylabel('Delta AB')
plt.show()     

plt.figure()
plt.scatter(EPFeI,deltaabFeI,c='k',marker='.')
plt.title('FeI')
plt.xlabel('EP')
plt.ylabel('Delta AB')
plt.show()   

index=np.flatnonzero(EWFeI>1)
index2=np.flatnonzero(EPFeI>1)
index=np.intersect1d(index,index2)

index2=np.flatnonzero(EWFeII>1)
index3=np.flatnonzero(EPFeII>1)
index2=np.intersect1d(index2,index3)

meanFeI=np.mean(deltaabFeI[index])
meanFeII=np.mean(deltaabFeII[index2])

meanDif=meanFeI-meanFeII

if np.abs(meanDif) > 0.05:
    if meanFeI > meanFeII:
        print('log g is too low!')
        print('Mean difference is: '+str(meanDif))
        print('as a guess your values are '+str(meanFeI+-1.69735365854)+' and '+str(meanFeII+-1.69735365854))
    else:
        print('log g is wrong!')
        print('Mean difference is: '+str(meanDif))
        print('as a guess your values are '+str(meanFeI+-1.69735365854)+' and '+str(meanFeII+-1.69735365854))
else:
    print('[FeI/H] is '+str(meanFeI))
    print('[FeII/H] is '+str(meanFeII))
