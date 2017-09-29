# Exercise 5.2

import numpy as np

#xlist = np.linspace(-4,4,41)
#print(xlist)

def h(x):
    x = 1/(np.sqrt(2*np.pi))*np.exp(-1/2*x**2)
    return x
n = 41
start = -4
end = 4
dx = abs((end-start)/(n-1))
print(dx)
xlist = [start + i*dx for i in range(n)]
ylist = [h(x) for x in xlist]
#for i in range(n):
#    xlist.append(start+i*dx)
#    print(i)

print(xlist)
print(ylist)