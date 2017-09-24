# Exercise 4.10

import sys

v0 = float(sys.argv[1])
t = float(sys.argv[2])
#t = float(input("Tid: "))
#v0 = float(input("Fart: "))
g = 9.81
y = v0*t - 0.5*g*t**2
print(y)

