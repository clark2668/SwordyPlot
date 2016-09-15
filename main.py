import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib
from matplotlib import rcParams
rcParams['mathtext.default'] = 'regular'
from functions import *

plotBrian = False
plotAhlers = True

def main():
   

    #set up the final plot
    xlow = 1e6 #the lower x limit
    xup = 1.001e21 #the uppper x limit
    ylow = 1e-8 #the lower y limit
    yup = 1.001E20 #the upper y limit
    fig = plt.figure(figsize=(6,8))
    ax1 = fig.add_subplot(1,1,1)

    if plotBrian:
        brianPlot(ax1)
    if plotAhlers:
        AhlersPlot(ax1)

    #prepare the labels and save the figure
    ax1.set_xlabel('Energy (eV)') #give it a title
    ax1.set_ylabel(r'E dN / dE dA d$\Omega$ dt ($km^{2}$ sr yr)$^{-1}$')
    ax1.set_title("Swordy Plot")
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_xlim([xlow,xup]) #set the x limits of the plot
    ax1.set_ylim([ylow,yup]) #set the y limits of the plot
    ax1.set_xticks([1e6,1e8,1e10,1e12,1e14,1e16,1e18,1e20])
    ax1.legend()
    fig.savefig('test.jpg',edgecolor='none') #save the figure
    
    
    






#actually execute the main function
main()