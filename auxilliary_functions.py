#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 18:37:58 2018

@author: tkemner
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# calculate interpolation polynomial
def calc_int_poly(x_array, y_array, grade):
    return np.poly1d(np.polyfit(x_array, y_array, grade))

# calculate bi-cubic splines
def calc_int_spline(x_array, y_array):
    tck = interpolate.splrep(x_array, y_array, s=0)
    x_values = np.arange(x_array.min(), x_array.max())
    y_values = interpolate.splev(x_values, tck, der=0)
    return x_values, y_values

# configure plot
def config_plot(x_min, x_max, y_min = 0, y_max = 0, size_factor = 1):
    # get present size and multiply by size factor
    plt_size = plt.rcParams.get('figure.figsize')
    plt.figure(figsize=(plt_size[0]*size_factor, plt_size[1]*size_factor))
    #set labels
    plt.xlabel('Raw value (kg)')
    plt.ylabel('Final value (kg)')
    plt.title('Interpolation durch die nominal und actual Werte')
    plt.grid(True)
    # set y limits if given, else auto scale
    if y_min != 0 | y_max != 0:
        plt.ylim(y_min, y_max)
    # create array of x-values between x_min and x_max
    x_values = np.linspace(x_min, x_max, 200)   
    return x_values
