import numpy as np
import matplotlib.pyplot as plt


infile = open('lnsum.dat', 'r')
data = infile.readlines()
lines = len(data)
epsi = np.zeros(lines)
error = np.zeros(lines)
n = np.zeros(lines)


i = 0
for l in data:
    words = l.split(',')
    epsi[i] = words[0].split()[1]
    error[i] = words[1].split()[2]
    n[i] = words[2].split('=')[1]
    i += 1

plt.semilogy(n, epsi, label = 'epsilon')
plt.semilogy(n, error, label = 'exact error')
plt.xlabel('n')
plt.legend()
plt.savefig('read_error.png')
plt.show()


'''
Terminal> read_error.py"

Process finished with exit code 0
'''