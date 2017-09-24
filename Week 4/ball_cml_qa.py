# Exercise 4.11

import sys

try:
    v0 = float(sys.argv[1])
except IndexError:
    v0 = float(input("Fart: "))

try:
    t = float(sys.argv[2])
except IndexError:
    t = float(input("Tid: "))


g = 9.81
y = v0*t - 0.5*g*t**2
print(y)


