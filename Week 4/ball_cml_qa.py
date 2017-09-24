# Exercise 4.11

import sys

try:
    v0 = float(sys.argv[1])
except IndexError:
    print("Fart og tid er ikke definert fra command line.")
    v0 = float(input("Fart: "))

try:
    t = float(sys.argv[2])
except IndexError:
    t = float(input("Tid: "))


g = 9.81
y = v0*t - 0.5*g*t**2
print(y)


"""
Terminal> ball_cml_qa.py" 
Fart og tid er ikke definert fra command line.
Fart: 20
Tid: 1
15.094999999999999

Process finished with exit code 0
"""