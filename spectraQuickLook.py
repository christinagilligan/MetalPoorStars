#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:09:15 2018

@author: christinagilligan
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import csv
import spectres
from sys import argv


#ID Sky Order Object Wavelength
#f = open('TYC4806-2678-1_R.csv')
#csv_f = csv.reader(f)
#next(csv_f)
#R_eric_csv = np.array(list(csv_f),dtype=float)  

#f = open('TYC4806-2678-1_B.csv')
#csv_f = csv.reader(f)
#next(csv_f)
#B_eric_csv = np.array(list(csv_f),dtype=float)  


#R_fits_image_filename = fits.util.get_testdata_filepath('R201711150004.fits')
#B_fits_image_filename = fits.util.get_testdata_filepath('B201711150004.fits')

#to be able to put in fits file name
script, filename = argv

R_hdul = fits.open(str('pR')+str(filename)+str('_obj.fits'))
B_hdul = fits.open(str('pH')+str(filename)+str('_obj.fits'))


#object name
objectName = R_hdul[0].header['OBJECT']

R_data = R_hdul[1].data
B_data = B_hdul[1].data

#orderNumber=80

#mask = R_data['Order'] == orderNumber

#R_newdata = R_data[mask]

#orders=R_eric_csv[:,2]

#for i in range(len(orders)-1):
#    goodOrder = np.flatnonzero(orders == orderNumber)
    
#hdu = fits.PrimaryHDU(np.fliplr([R_eric_csv[:,1]])[0])
#hdu.writeto('new_eric_R.fits')

#hdu = fits.PrimaryHDU(np.fliplr([R_data['Flux']])[0])
#hdu.writeto('new_hrs_R.fits')

#plt.figure()
#plt.plot(np.fliplr([R_data['Wavelength']])[0],np.fliplr([R_data['Flux']])[0],label='HRS')
#plt.plot(np.fliplr([R_eric_csv[goodOrder,4]])[0],np.fliplr([R_eric_csv[goodOrder,3]-R_eric_csv[goodOrder,1]])[0],label='Eric')
#plt.plot(np.fliplr([R_eric_csv[:,4]])[0],np.fliplr([R_eric_csv[:,1]])[0]-29252.320134858313,label='Eric')
#plt.title('Order: '+str(orderNumber))
#plt.xlabel('Wavelength (A)')
#plt.ylabel('Flux')
#plt.legend()
#plt.show()  

#new_wav=np.linspace(5613, 8706,num=120000)
#new_spectra=spectres.spectres(new_wav,data[:,0],data[:,1] ,spec_errs=None)
#savedata=np.vstack((new_wav.astype(float),new_spectra.astype(float)))
#savedata=np.transpose(savedata)
#np.savetxt('spectra.txt',savedata) 


#want our data to be properly sorted in wavelength space
fluxdata = [x for _,x in sorted(zip(R_data['Wavelength'],R_data['Flux']))]
wavelengthdata = sorted(R_data['Wavelength'])
fluxdata=np.asarray(fluxdata)
wavelengthdata=np.asarray(wavelengthdata)

wavelengthdata=np.nan_to_num(wavelengthdata)

#now we need the x-axis (wavelength) to be increasing linearly, which it is not currently doing
new_wave=np.linspace(np.min(R_data['Wavelength'])+0.1, np.max(R_data['Wavelength'])-0.1,num=len(R_data['Wavelength'])+100)
new_spectra=spectres.spectres(new_wave,wavelengthdata,fluxdata ,spec_errs=None)
new_spectra=np.nan_to_num(new_spectra)
new_spectra=new_spectra.astype(float)

spectradata=np.transpose(np.vstack((new_wave,new_spectra)))

np.savetxt(str(objectName)+str('_R.txt'),spectradata)

wave_space =np.array([new_wave[100]-new_wave[99]])

with open ('red_spacing_wavelength.txt', 'a') as f_handle:
    np.savetxt(f_handle, wave_space)




#now do it for the blue chip
fluxdata = [x for _,x in sorted(zip(B_data['Wavelength'],B_data['Flux']))]
wavelengthdata = sorted(B_data['Wavelength'])
fluxdata=np.asarray(fluxdata)
wavelengthdata=np.asarray(wavelengthdata)

wavelengthdata=np.nan_to_num(wavelengthdata)

#now we need the x-axis (wavelength) to be increasing linearly, which it is not currently doing
new_wave=np.linspace(np.min(B_data['Wavelength'])+0.1, np.max(B_data['Wavelength'])-0.1,num=len(B_data['Wavelength'])+100)
new_spectra=spectres.spectres(new_wave,wavelengthdata,fluxdata ,spec_errs=None)
new_spectra=np.nan_to_num(new_spectra)
new_spectra=new_spectra.astype(float)

spectradata=np.transpose(np.vstack((new_wave,new_spectra)))

np.savetxt(str(objectName)+str('_B.txt'),spectradata)

#make files that rpsectext wants
#need a list of the starting wavelengths on the red chip
#same for the blue chip
#and a list of wavelength spacings for the red and blue as well


red_min =np.array([np.min(R_data['Wavelength'])])

blue_min =np.array([np.min(B_data['Wavelength'])])


with open ("red_start_wavelength.txt", 'a')as f_handle:
     np.savetxt(f_handle, red_min)


with open ('blue_start_wavelength.txt', 'a')as f_handle:
     np.savetxt(f_handle, blue_min)

wave_space =np.array([new_wave[100]-new_wave[99]])
     
with open ('blue_spacing_wavelength.txt', 'a')as f_handle:
     np.savetxt(f_handle, wave_space)


