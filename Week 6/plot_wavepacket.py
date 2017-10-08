# Exercise 5.28

import numpy as np
import matplotlib.pyplot as plt

t = 0

x = np.linspace(-4,4,400)

y = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))


#print(y)


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x,t)')
plt.savefig('wavepacket.png')
plt.show()


