import numpy as np
import matplotlib.pyplot as plt
#a tester printer function
def add_limit(axis_to_alter, file_name,plot_parameters,label_to_use):
    x,y = np.loadtxt(file_name,
                     unpack = True,
                    delimiter = ',')
    axis_to_alter.plot(x,y,plot_parameters,label=label_to_use)