#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:07:30 2018

@author: christinagilligan
"""
#convert csv to a MOOG input file

import csv
import numpy as np
import matplotlib.pyplot as plt


ion=[]
wavelength=[]
eqwA=[]
eqwmA=[]
Notes=[]
extra1=[]
extra2=[]
extra3=[]
extra4=[]
extra5=[]

#change starname to whatever to make the file
starname='HIP106924'
filename=str(starname)+'abund.csv'

f = open(filename)
csv_f = csv.reader(f)
next(csv_f)
abund = np.array(list(csv_f))

ion=np.array(abund[:,0])
wavelength=np.array(abund[:,1],dtype=float)
eqwA=np.array(abund[:,2])
eqwmA=np.array(abund[:,3],dtype=float)




#need to find loggf and ep values for each wavelength
wavelength_all=[]
ep=[]
loggf=[]

#only get Fe lines
file = open('metalpoorfe.dat')
for line in file:
    if 'Fe' not in line and 'Wavelength' not in line and len(line.strip())!=0:
        line=line.strip()
        line=line.split()
        line=np.asarray(line)
        wavelength_all.append(line[0])
        ep.append(line[2])
        loggf.append(line[3])
        
wavelength_all=np.asarray(wavelength_all)

file = open(str(starname)+'.dat','w') 
file.write('Fe Lines in '+str(starname)+'\n')
for i in range(0,len(ion)-1):

    if eqwmA[i]!= 0 and ion[i]=='FeI':
        index=np.flatnonzero(float("{0:.2f}".format(wavelength[i])) == wavelength_all.astype(float))
        loggf_value=loggf[index[0]]
        ep_value=ep[index[0]]
        file.write('  '+"{0:.2f}".format(wavelength[i])+'       '+str(26.0)+'      '+str(ep_value)+'     '+str(loggf_value)+'                          '+str(eqwmA[i])+'\n')

    if eqwmA[i]!= 0 and ion[i]=='FeII':
        index[0]=np.flatnonzero(float("{0:.2f}".format(wavelength[i])) == wavelength_all.astype(float))
        loggf_value=loggf[index[0]]
        ep_value=ep[index[0]]
        file.write('  '+"{0:.2f}".format(wavelength[i])+'       '+str(26.1)+'      '+str(ep_value)+'     '+str(loggf_value)+'                          '+str(eqwmA[i])+'\n')

 
file.close() 
