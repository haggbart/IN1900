# Exercise 5.40

from numpy import linspace
from matplotlib.pyplot import *
#from scitools.std import movie


def v(r,n):
    res = ((B/(2*u0))**(1/n) * n/(n+1) * (R**(1+1/n)-r**(1+1/n)))
    return res

R = 1
B = 0.02
u0 = 0.02
#n = 0.1

r = linspace(0, R, 100)
y = v(r, 0.1)
counter = 0
hold(0)
for n in linspace(1, 0.01, 100):
    plot(r,v(r, n) / v(0, n))
    xlabel("Radial")
    ylabel("Velocity")
    savefig("tmp_%03d.png" % counter)
    counter += 1

movie('tmp_*.png', encoder='convert', fps=24)
print(v(4))
print(r)
print(y)

import glob
import os
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)