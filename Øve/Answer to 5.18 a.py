import matplotlib.pyplot as plt
import numpy as np


def fit(x,y,deg):
    plt.plot(x, y, 'bo')
    x1 = np.linspace(np.min(x), np.max(x), 100)
    for d in deg:
        coef = np.polyfit(x, y, d)
        p = np.poly1d(coef)
        y1 = p(x1)
        plt.plot(x1, y1, 'r-')


fnames = ['density_air.dat', 'density_water.dat']


for i in range(len(fnames)):
    plt.subplot(1,2,i+1)
    temp = []; dens = []
    infile = open(fnames[i], 'r')
    for line in infile:
        words = line.split();
        if len(words) >= 2 and words[0] != '#':
            temp.append(float(words[0]))
            dens.append(float(words[1]))
    infile.close()
    fit(temp, dens, deg=[1,2])
    plt.title(fnames[i])

plt.show()


