# Exercise 5.16

import sys
import matplotlib.pyplot as plt
import numpy as np


fname = 'density_air.dat'
temp = []; dens = []
infile = open(fname, 'r')
for line in infile:
    words = line.split()
    if len(words) >= 2 and words[0] != '#':
        temp.append(float(words[0]))
        dens.append(float(words[1]))
infile.close()
plt.plot(temp, dens, 'bo')
plt.show()
print(np.polyfit(temp, dens, 1))