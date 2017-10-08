# Exercise 5.41

import numpy as np
import matplotlib.pyplot as plt


def S(t,n, T):
    z = 0
    for i in range(1,n+1):
        z += 1 / (2 * i - 1) * np.sin((2 * (2 * i - 1) * np.pi * t) / T)
    z *= 4 / np.pi
    return z


# def f(t, T):
#     if 0 < t < T/2:
#         res = 1
#     elif abs(t - T/2) < 1e-14:
#         res = 0
#     elif T/2 < t < T:
#         res = -1
#     else:
#         print('Error')
#     return res


n_list = [1,3,20,200]
T = np.pi*2
t = np.linspace(0,T,100)

for n in n_list:
    y = S(t,n,T)
    plt.plot(t,y)
plt.plot([0,T/2,T/2,T],[1,1,-1,-1])
plt.savefig('sinesum.png')
plt.show()


'''
Terminal> sinesum1_plot.py"

Process finished with exit code 0
'''