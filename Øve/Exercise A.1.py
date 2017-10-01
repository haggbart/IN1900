from numpy import *

def sequence_a(N):
    index_set = range(N+1)
    a = zeros(len(index_set))
    for n in index_set:
        a[n] = (7+1.0/(n+1))/(3-1.0/(n+1)**2)
    return a

#print(sequence_a(100))
#print(7/3)


def sequence_b(N):
    index_set = range(N+1)
    D = zeros(len(index_set))
    for n in index_set:
        D[n] = sin(2**(-n))/2**(-n)
    return D

print(sequence_b(1000))


def D(f,x,N):
    index_set = range(N+1)
    D = zeros(len(index_set))
    for n in index_set:
        h = 2**-n
        D[n] = (f(x+h)-f(x))/h
        print(h)
    return D

import matplotlib.pyplot as plt


D1 = D(sin,pi,53)
plt.plot(range(53+1),D1,'o')
plt.show()

