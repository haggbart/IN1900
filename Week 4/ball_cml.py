# Exercise 4.10

import sys

v0 = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81
y = v0*t - 0.5*g*t**2
print(y)


"""
Terminal> ball_cml.py" 20 1
15.094999999999999

Process finished with exit code 0
"""