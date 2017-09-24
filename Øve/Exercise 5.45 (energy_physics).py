# Exercise 5.45

from numpy import linspace
from matplotlib.pyplot import *
import sys
m = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81 # m/s
print(m,v0)


t = linspace(0, 2*v0/g)
y = v0*t-1/2*g*t**2
v = v0 - g*t
P = m * g * y
K = 1/2 * m * v ** 2

plot(t, P, label = "Potential energy")
plot(t, K, label = "Kinetic energy")
plot(t, P+K, label = "P + K")

xlabel("Time (s)")
ylabel("Energy (J)")
legend()
show()