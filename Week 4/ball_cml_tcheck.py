# Exercise 4.12

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
print(v0,t,2*v0/g)

if t < 0 or t > 2*v0/g:
    raise SystemExit("v0 must be a number between 0 and 2v0/g.")

y = v0*t - 0.5*g*t**2
print(y)


