# 5.10: Plot a formula

from numpy import *
from matplotlib.pyplot import *
import sys

#v_list = sys.argv[1:]
v_list = [5, 10, 15]
print(v_list)
#v0 = 10

g = 9.81

for v0 in v_list:
    t = linspace(0,2*v0/g, 100)
    y = v0*t-0.5*g*t**2
    plot(t,y, label = 'v0 = %g' %(v0))

xlabel("time (s)")
ylabel("height (m)")
legend()
show()

"""
Terminal> python Exercise 5.10.py 5 10 15
(output is a plot)
"""