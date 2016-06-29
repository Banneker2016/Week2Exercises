# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:54:58 2016

@author: Rachel
"""
import numpy as np 
import matplotlib.pyplot as plt
from astropy.io import fits

def makeGaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)
#Equation for Gaussian made by giessel from GitHub    

#Made a simple array and assigned a gaussian flux (Dr. Johnson's idea)   
pixels = np.array(100)  
flux = makeGaussian(pixels)
  
plt.imshow(flux) 

#creating the fits
hdu = fits.PrimaryHDU(flux)

hdulist = fits.HDUList([hdu])
hdulist.writeto('test2.fits')



