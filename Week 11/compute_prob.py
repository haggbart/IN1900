# Exercise 8.2

from random import random


i = [1,2,3,6]

for i in i:
    M = 0
    N = 10**i
    for j in range(N):
        if 0.5 <= random() <= 0.6:
            M += 1
    print('10^%d: %.4f or %d percent' % (i,M/N, M/N*100))


'''
Terminal> compute_prob.py"
10^1: 0.3000 or 30 percent
10^2: 0.0800 or 8 percent
10^3: 0.0800 or 8 percent
10^6: 0.1001 or 10 percent

Process finished with exit code 0
'''