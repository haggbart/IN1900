from numpy import linspace
from matplotlib.pyplot import *
a = -2
b = 2


def f(x):
    res = abs(a*x+b)
    return res

x = linspace(0,4,100)
y = f(x)

plot(x,y)
show()