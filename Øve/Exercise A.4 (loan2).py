# Exercise A.4

# N: number of months
# L: initional size of the loan
# P: annual interest rate (in percent)
import numpy as np


def loan(N,L,p):
    x = np.zeros(N)
    y = np.zeros_like(x)
    L = float(L)
    p = float(p)
    x[0] = L
    for n in range(1,N):
        y[n] = (p/(12*100))*x[n-1] + L/N
        x[n] = x[n-1] + (p/(12*100))*x[n-1] + y[n]
    return x,y

print(loan(100,400,5))