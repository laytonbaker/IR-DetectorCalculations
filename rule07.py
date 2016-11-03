# -*- coding: utf-8 -*-
"""
Created on Thu Sep 04 12:07:43 2014

@author: laytonba
"""
from __future__ import division, print_function
import numpy as np
import scipy.constants as const

def rule07(wl, T):
    '''
    function to compute dark current density using Rule 07 TIS empirical model
    ARGS: wl = cutoff wave length in microns, T = temperature in Kelvin
    RETURN: J = dark current density in A/cm^2
    '''
    Jo = 8367.000019    
    Pwr = 0.544071282
    C = -1.162972237
    ws = 0.200847413
    wt = 4.635136423
    q = const.e
    k = const.k
    wl = float(wl)
    T = float(T)
    
    if wl >= wt:
        we = wl
    else:
        we = wl / (1-((ws/wl)-(ws/wt))**Pwr)
    
    #print(type(we))    
    #assert we is type(float)
    #assert we > 0.0
    
    A = C*1.24*q/(k*we*T)
    
    return Jo*np.exp(A)


def rule07_wlplot(wlarray, Tarray):
    '''
    Plot dark current versus wavelength
    '''
   
    colormap = plt.cm.jet
    cycle = [colormap(i) for i in np.linspace(0.0, 1.0, len(Tarray))]

    plt.figure(figsize=(5, 4), dpi=150)
    plt.subplots_adjust(left=0.20, right=0.95,bottom=0.15, 
                        top=0.92, hspace=0.3, wspace=0.3)
    ax = plt.subplot2grid((1,1),(0,0))    
    
    for i,T in enumerate(Tarray):
        Jarray = []        
        for wl in wlarray:
            Jarray.append(rule07(wl,T))
    
        plt.semilogy(wlarray, 
                     Jarray, 
                     color=cycle[i], alpha=0.8,
                     label=r'{0}K'.format(T) )
                 
    plt.xlim(5, 20)
    plt.ylim(1e-10, 10)    
    
    plt.title('Rule07 Dark Current Density',
              fontsize = 14)

    plt.xlabel(r'$\mathbf{cutoff wavelength\hspace{0.5}}  \mathrm{(\mu m)}$',
               fontsize = 16)

    plt.ylabel(r'$\mathbf{J_{dark}\hspace{0.5}}  \mathrm{(A/cm^{2})}$',
               fontsize=16)

    plt.grid(b=None, which='major', axis='both', color='gray')
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(11)

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = collections.OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),
               fontsize = 8,
               ncol=2, loc='upper left', 
               labelspacing=0.0,
               handletextpad=0.0, handlelength=1.5,
               fancybox=True, shadow=True)

#    plt.text(17.5, 5e-11, 
#             r'{0}K'.format(40),
#             fontsize = 8 )               
#    plt.text(10.8, 1e-5, 
#             r'{0}K'.format(77),
#             fontsize = 8 )  
    
    plt.show()


def rule07_Tplot(wlarray, Tarray):
    '''
    Plot dark current versus wavelength
    '''
   
    colormap = plt.cm.rainbow
    cycle = [colormap(i) for i in np.linspace(0.0, 1.0, len(wlarray))]

    plt.figure(figsize=(5, 4), dpi=150)
    plt.subplots_adjust(left=0.20, right=0.95,bottom=0.15, 
                        top=0.92, hspace=0.3, wspace=0.3)
    ax = plt.subplot2grid((1,1),(0,0))    
    
    for i,wl in enumerate(wlarray):
        Jarray = []        
        for T in Tarray:
            Jarray.append(rule07(wl,T))
    
        plt.semilogy(Tarray, 
                     Jarray, 
                     color=cycle[i], alpha=0.8,
                     label=r'{0}um'.format(wl) )
                 
    plt.xlim(Tarray[0], Tarray[-1])
    plt.ylim(1e-10, 10)    
    
    plt.title('Rule07 Dark Current Density',
              fontsize = 14)

    plt.xlabel(r'$\mathbf{temperature\hspace{0.5}}  \mathrm{(K)}$',
               fontsize = 16)

    plt.ylabel(r'$\mathbf{J_{dark}\hspace{0.5}}  \mathrm{(A/cm^{2})}$',
               fontsize=16)

    plt.grid(b=None, which='major', axis='both', color='gray')
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(11)

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = collections.OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),
               fontsize = 8,
               ncol=2, loc='upper left', 
               labelspacing=0.0,
               handletextpad=0.0, handlelength=1.0,
               fancybox=True, shadow=True)

#    plt.text(17.5, 5e-11, 
#             r'{0}K'.format(40),
#             fontsize = 8 )               
#    plt.text(10.8, 1e-5, 
#             r'{0}K'.format(77),
#             fontsize = 8 )  
    
    plt.show()

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import collections
 
#    Tarray_A = (50, 60, 70, 77, 80, 90, 100, 110, 120)
#    wlarray_A = np.linspace(5, 20, 100)
#    
#    rule07_wlplot(wlarray_A, Tarray_A)
    
    Tarray_B = np.linspace(40, 160, 120)
    wlarray_B = range(5,16)
    
    rule07_Tplot(wlarray_B, Tarray_B)