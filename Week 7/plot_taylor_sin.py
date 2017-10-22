# Exercise 5.32
import math
import matplotlib.pyplot as plt
import numpy as np


def S(x,n):
    s = 0
    for j in range(n):
        s = s + (-1)**j * (x**(2*j+1)) / math.factorial(2*j+1)
    return s


x = np.linspace(0,np.pi*4,100)
y = np.sin(x)
Splot = [1,2,3,6,12]


for n in Splot:
    plt.plot(x, S(x, n), label = 'S(x, %g)' %(n))

plt.plot(x,y, label='sin(x')
plt.title('sin x on [0, 4pi]')
plt.ylim(1.1,-1.1)
plt.legend()
plt.savefig('plot_taylor_sin.png')
plt.show()


'''
Terminal> plot_taylor_sin.py"

Process finished with exit code 0
'''