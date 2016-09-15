import numpy as np
import matplotlib.pyplot as pl

convert_m2s_to_km2yr=1.E4*86400.*365.24;


def brianPlot(axis):
    data = np.genfromtxt('brian_flux.csv', delimiter=',', skip_header=1, names=['energy', 'flux'])
    axis.plot(data['energy'],data['flux'],'ro-',label = 'brians flux')

def AhlersPlot(axis):
        
    #do things for the lower limit
    datalow = np.genfromtxt('ahlers_2010_low.csv', delimiter=',', skip_header=1, names=['lowerx', 'lowery'])
    AhlersLowerEnergy = datalow['lowerx']
    AhlersLowerFlux = datalow['lowery']     
    for i in xrange(AhlersLowerEnergy.shape[0]):
        temporary = AhlersLowerEnergy[i]        
        temporary+=9
        AhlersLowerEnergy[i]=pow(10,temporary)
        temporary = AhlersLowerFlux[i]
        temporary2 = pow(10,temporary)
        temporary2*=(1e9 * 1e4 * convert_m2s_to_km2yr / AhlersLowerEnergy[i])
        AhlersLowerFlux[i]=temporary2
    
    #do things for the upper limit
    datahigh = np.genfromtxt('ahlers_2010_high.csv', delimiter=',', skip_header=1, names=['upperx', 'uppery'])
    AhlersUpperEnergy = datahigh['upperx']
    AhlersUpperFlux = datahigh['uppery'] 
    for i in xrange(AhlersUpperEnergy.shape[0]):
        temporary = AhlersUpperEnergy[i]        
        temporary+=9
        AhlersUpperEnergy[i]=pow(10,temporary)
        temporary = AhlersUpperFlux[i]
        temporary2 = pow(10,temporary)
        temporary2*=(1e9 * 1e4 * convert_m2s_to_km2yr / AhlersUpperEnergy[i])
        AhlersUpperFlux[i]=temporary2

    axis.plot(AhlersLowerEnergy,AhlersLowerFlux,'grey',label = 'Ahlers 2010')
    axis.plot(AhlersUpperEnergy,AhlersUpperFlux,'grey')
    #axis.fill_between(AhlersUpperEnergy,AhlersLowerFlux,AhlersUpperFlux,facecolor='grey', interpolate=True) //need to get this to work to make a band...
