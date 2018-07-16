#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:04:24 2018

@author: christinagilligan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:18:50 2018

@author: christinagilligan
"""

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
EP_sun=[]
logGF_sun=[]
EWin_sun=[]
logRWin_sun=[]
abund_sun=[]
delavg_sun=[]

file = open('abund_sun.b')
#print(file.read())
for line in file:
    if 'correl' not in line and 'avg' not in line and 'abund' not in line and '/' not in line and 'No' not in line and 'Fe' not in line and len(line.strip())!=0:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        wavelength_sun.append(line[0])
        EP_sun.append(line[1])
        logGF_sun.append(line[2])
        EWin_sun.append(line[3])
        logRWin_sun.append(line[4])
        abund_sun.append(line[5])
        delavg_sun.append(line[6])
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
    
goodEWFeIa=np.flatnonzero(EWFeI>=0)
goodEWFeIb=np.flatnonzero(EWFeI<=80)
goodEWFeI=np.intersect1d(goodEWFeIa,goodEWFeIb)

goodEWFeIIa=np.flatnonzero(EWFeII>=0)
goodEWFeIIb=np.flatnonzero(EWFeII<=80)
goodEWFeII=np.intersect1d(goodEWFeIIa,goodEWFeIIb)

meanFeI=np.mean(deltaabFeI[goodEWFeI])
meanFeII=np.mean(deltaabFeII[goodEWFeII])

meanDif=meanFeI-meanFeII


caIindex=np.flatnonzero(ID_star==20.0)
caIwavelengths=wavelength_star[caIindex]

mgIindex=np.flatnonzero(ID_star==12.0)
mgIwavelengths=wavelength_star[mgIindex]

naIindex=np.flatnonzero(ID_star==11.0)
naIwavelengths=wavelength_star[naIindex]

siIindex=np.flatnonzero(ID_star==14.0)
siIwavelengths=wavelength_star[siIindex]

oIindex=np.flatnonzero(ID_star==8.0)
oIwavelengths=wavelength_star[oIindex]

deltaabCaI=[]
EPCaI=[]
EWCaI=[]

for i in range(len(caIwavelengths)):
    wavelength=caIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabCaI.append(np.float(star_abund-sun_abund))
        EPCaI.append(EPs)
        EWCaI.append(EWs)
    
deltaabCaI=np.array(deltaabCaI,dtype=float)
EPCaI=np.array(EPCaI,dtype=float)
EWCaI=np.array(EWCaI,dtype=float) 

deltaabMgI=[]
EPMgI=[]
EWMGI=[]

for i in range(len(mgIwavelengths)):
    wavelength=mgIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabMgI.append(np.float(star_abund-sun_abund))
        EPMgI.append(EPs)
        EWMgI.append(EWs)
    
deltaabMgI=np.array(deltaabMgI,dtype=float)
EPMgI=np.array(EPMgI,dtype=float)
EWMgI=np.array(EWMgI,dtype=float) 

deltaabNaI=[]
EPNaI=[]
EWNaI=[]

for i in range(len(naIwavelengths)):
    wavelength=naIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabNaI.append(np.float(star_abund-sun_abund))
        EPNaI.append(EPs)
        EWNaI.append(EWs)
    
deltaabNaI=np.array(deltaabNaI,dtype=float)
EPNaI=np.array(EPNaI,dtype=float)
EWNaI=np.array(EWNaI,dtype=float) 

deltaabSiI=[]
EPSiI=[]
EWSiI=[]

for i in range(len(siIwavelengths)):
    wavelength=siIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabSiI.append(np.float(star_abund-sun_abund))
        EPSiI.append(EPs)
        EWSiI.append(EWs)
    
deltaabSiI=np.array(deltaabSiI,dtype=float)
EPSiI=np.array(EPSiI,dtype=float)
EWSiI=np.array(EWSiI,dtype=float) 

deltaabOI=[]
EPOI=[]
EWOI=[]

for i in range(len(oIwavelengths)):
    wavelength=oIwavelengths[i]
    star_index=np.flatnonzero(wavelength_star==wavelength)
    sun_index=np.flatnonzero(wavelength_sun==wavelength)
    if len(abund_sun[sun_index]) !=0:
        star_abund=np.float(abund_star[star_index])
        EPs=np.float(EP_star[star_index])
        EWs=np.float(EWin_star[star_index])
        sun_abund=np.float(abund_sun[sun_index])
        deltaabOI.append(np.float(star_abund-sun_abund))
        EPOI.append(EPs)
        EWOI.append(EWs)
    
deltaabOI=np.array(deltaabOI,dtype=float)
EPOI=np.array(EPOI,dtype=float)
EWOI=np.array(EWOI,dtype=float) 

meanCaI=np.mean(deltaabCaI)
meanMgI=np.mean(deltaabMgI)
meanNaI=np.mean(deltaabNaI)
meanSiI=np.mean(deltaabSiI)
meanOI=np.mean(deltaabOI)

CaIabund = meanCaI - meanFeI
MgIabund = meanMgI - meanFeI
NaIabund = meanNaI - meanFeI
SiIabund = meanSiI - meanFeI
OIabund = meanOI - meanFeII

print('[CaI/FeI] = '+str(CaIabund))
print('[MgI/FeI] = '+str(MgIabund))
print('[NaI/FeI] = '+str(NaIabund))
print('[SiI/FeI] = '+str(SiIabund))
print('[OI/FeII] = '+str(OIabund))
