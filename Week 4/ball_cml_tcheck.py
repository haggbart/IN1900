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
    raise SystemExit("t må være et tall mellom 0 og 2v0/g.")

y = v0*t - 0.5*g*t**2
print(y)


"""
Terminal> ball_cml_tcheck.py"
Fart: 20
Tid: 5
t må være et tall mellom 0 og 2v0/g.
20.0 5.0 4.077471967380224

Process finished with exit code 1
"""