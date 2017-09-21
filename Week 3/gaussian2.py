# 3.22 (gaussian2.py, side 137)

from math import exp, sqrt, pi

def gauss(x, m=0, s=1):
    return 1 / (sqrt(2 * pi) * s) * exp(-1 / 2 * ((x - m) / s) ** 2)

dx = 1      # intervallet
sett = 20   # utgangspunkt x +/- 5
xlist = []
glist = []
for x in range(sett-5, sett+6):
    xlist.append(x*dx)
    glist.append(gauss(x*dx))
r = list(zip(xlist, glist))
for i in range(len(r)):
    print("x: %2.f Gauss: %10.3g" % (r[i][0], r[i][1]))

"""
Terminal> gaussian2.py"
x: 15 Gauss:   5.53e-50
x: 16 Gauss:   1.03e-56
x: 17 Gauss:      7e-64
x: 18 Gauss:   1.76e-71
x: 19 Gauss:   1.62e-79
x: 20 Gauss:   5.52e-88
x: 21 Gauss:    6.9e-97
x: 22 Gauss:  3.17e-106
x: 23 Gauss:  5.37e-116
x: 24 Gauss:  3.34e-126
x: 25 Gauss:  7.65e-137

Process finished with exit code 0
"""