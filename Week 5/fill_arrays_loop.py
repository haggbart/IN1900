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
x = np.zeros(n)
y = np.zeros(len(x))
for i in range(len(x)):
    x[i] = start + i*dx
    y[i] = h(x[i])


for x,y in zip(x,y):
    print('h(%5.2f) = %4.4f' % (x, y))

'''
Terminal> fill_arrays_loop.py"
h(-4.00) = 0.0001
h(-3.80) = 0.0003
h(-3.60) = 0.0006
h(-3.40) = 0.0012
h(-3.20) = 0.0024
h(-3.00) = 0.0044
h(-2.80) = 0.0079
h(-2.60) = 0.0136
h(-2.40) = 0.0224
h(-2.20) = 0.0355
h(-2.00) = 0.0540
h(-1.80) = 0.0790
h(-1.60) = 0.1109
h(-1.40) = 0.1497
h(-1.20) = 0.1942
h(-1.00) = 0.2420
h(-0.80) = 0.2897
h(-0.60) = 0.3332
h(-0.40) = 0.3683
h(-0.20) = 0.3910
h( 0.00) = 0.3989
h( 0.20) = 0.3910
h( 0.40) = 0.3683
h( 0.60) = 0.3332
h( 0.80) = 0.2897
h( 1.00) = 0.2420
h( 1.20) = 0.1942
h( 1.40) = 0.1497
h( 1.60) = 0.1109
h( 1.80) = 0.0790
h( 2.00) = 0.0540
h( 2.20) = 0.0355
h( 2.40) = 0.0224
h( 2.60) = 0.0136
h( 2.80) = 0.0079
h( 3.00) = 0.0044
h( 3.20) = 0.0024
h( 3.40) = 0.0012
h( 3.60) = 0.0006
h( 3.80) = 0.0003
h( 4.00) = 0.0001

Process finished with exit code 0
'''