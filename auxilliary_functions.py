#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 18:37:58 2018

@author: tkemner
"""

# ------------------------------------------------------------------------------   
# imports
# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# ------------------------------------------------------------------------------   
# calculate interpolation polynomial
# ------------------------------------------------------------------------------
def calc_int_poly(x_array, y_array, grade):
    return np.poly1d(np.polyfit(x_array, y_array, grade))

# ------------------------------------------------------------------------------   
# calculate bi-cubic splines
# ------------------------------------------------------------------------------
def calc_int_spline(x_array, y_array):
    tck = interpolate.splrep(x_array, y_array, s=0)
    x_values = np.arange(x_array.min(), x_array.max())
    y_values = interpolate.splev(x_values, tck, der=0)
    return x_values, y_values

# ------------------------------------------------------------------------------   
# configure plot
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------   
# calculate and show polynomial plots
# ------------------------------------------------------------------------------
def show_polynomial_plots(x_array, y_array):
    # axis min and max values
    x_min, x_max = int(np.amin(x_array)) - 10, int(np.amax(x_array)) + 30
    y_min, y_max = int(np.amin(y_array)) - 10, int(np.amax(y_array)) + 30
    # calculate polynomials
    poly_3 = calc_int_poly(x_array, y_array, 3)
    poly_final = calc_int_poly(x_array, y_array, y_array.size - 1)
    # create plots
    xp = config_plot(x_min, x_max, y_min, y_max, 1.5)
    plt.plot(x_array, y_array, 'o', xp, poly_3(xp), '--', xp, poly_final(xp), '-')
    plt.legend(['Stützpunkte', 'Polynom Grad 3', 'Polynom Grad n-1'])
    plt.show()
    return poly_3, poly_final

# ------------------------------------------------------------------------------   
# calculate and show spline plots
# ------------------------------------------------------------------------------
def show_spline_plots(x_array, y_array):
    # axis min and max values
    x_min, x_max = int(np.amin(x_array)) - 10, int(np.amax(x_array)) + 30
    y_min, y_max = int(np.amin(y_array)) - 10, int(np.amax(y_array)) + 30
    spln_x_values, spln_y_values = calc_int_spline(x_array, y_array)
    # create plots
    xp = config_plot(x_min, x_max, y_min, y_max, 1.5)
    plt.plot(x_array, y_array, 'o', x_array, y_array, '--', spln_x_values, spln_y_values, '-')
    plt.legend(['Stützpunkte', 'Linear', 'Bikubische Splines'])
    plt.show()
    return
    