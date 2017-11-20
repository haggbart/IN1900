# Exercise 8.6


from random import randint


def dice(n,N):
    M = 0
    for i in range(N):
        for j in range(n):
            if randint(1,6) == 6:
                M += 1
                break
    return M/N


N = [2,4,6,10,1000,100000]
n = 2
for N in N:
    print('%6d throws: %.3f' % (N, dice(n, N)))
print('------------')
print('Monte Carlo simulation exact: 11/36 or %.3f' % (11/36))


'''
Terminal> one6_ndice.py"
     2 throws: 0.000
     4 throws: 0.250
     6 throws: 0.000
    10 throws: 0.200
  1000 throws: 0.291
100000 throws: 0.306
------------
Monte Carlo simulation exact: 11/36 or 0.306
'''