# Exercise 5.13

import sys
import numpy as np
from matplotlib.pyplot import *
from math import tan, cos, sqrt


def f(x, y0, theta, v0, g):
    return x * tan(theta) - (1/(2*v0**2))*((g*x**2)/(cos(theta)**2)) + y0


y0 = float(sys.argv[1])
theta = float(sys.argv[2])
v0 = float(sys.argv[3])
g = 9.81


a = -(1/(2*v0**2))*((g)/(cos(theta)**2))
b = tan(theta)
c = y0
x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
print(x1,x2)

x_max = max(x1,x2)
x = np.linspace(0,x_max,100)
y = f(x,y0,theta,v0,g)
plot(x,y)
show()