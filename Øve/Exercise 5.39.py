# Exercise 5.39

from numpy import *
import matplotlib.pyplot as plt

from math import factorial

def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    x = linspace(xmin, xmax, n)
    y_exact = exact(x)
    s = zeros_like(x)

    plt.plot(x,y_exact)

    lines = plt.plot(x,s)

    plt.axes([xmin, xmax, ymin, ymax])


    for k in range(M,N+1):
        s = s + fk(x,k)
        lines[0].set_ydata(s)
        plt.draw()
        plt.pause(0.25)


def f_sin(x,k):
    return (-1)**k*x**(2*k+1)/factorial(2*k+1)


def exp_inv(x):
    return exp(-x)


def f_exp(x,k):
    return (-x)**k/factorial(k)

# animate_series(f_sin,0,40,0,13*pi,-2,2,100,sin)
animate_series(f_exp,0,30,0,15,-0.5,1.4,100,exp_inv)