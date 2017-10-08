# Exercise 5.31

import numpy as np
import matplotlib.pyplot as plt

g = 9.81        # m/s^2
s = 7.9e-2      # N/m
p = 1000        # kg/m^3
h = 50          # meter

def c(L, h=50):
    return np.sqrt((g*L)/(2*np.pi) * (1+s*(4*np.pi**2)/(p*g*L**2)) * np.tanh((2*np.pi*h)/L))



l = np.linspace(0.001,0.1,100)
L = np.linspace(1,2e3,100)
#print(c(l))


plt.plot(l,c(l))
plt.title('small lambda')
plt.xlabel('lambda')
plt.ylabel('velocity')
plt.show()
plt.plot(L,c(L))
plt.title('larger lambda')
plt.xlabel('lambda')
plt.ylabel('velocity')
plt.show()