# 5.10: Plot a formula

from numpy import *
from matplotlib.pyplot import *
import sys

#v_list = sys.argv[1:]
v_list = [3, 5, 10]
print(v_list)
#v0 = 10

g = 9.81

t_max = 0
y_max = 0

for v0 in v_list:
    t_stop = 2*v0/g
    t = linspace(0,t_stop, 100)
    y = v0*t-0.5*g*t**2
    plot(t,y, label = 'v0 = %g' %(v0))
    if t_stop >t_max:
        t_max = t_stop

    if max(y) > y_max:
        y_max = max(y)

print(t_max, y_max)


xlabel("time (s)")
ylabel("height (m)")
axis([-1, t_max, 0, y_max*1.1])

legend()
show()

