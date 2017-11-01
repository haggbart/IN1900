import numpy as np
import matplotlib.pyplot as plt


def vel(k,x,s):
    return (x[k+1] - x[k]) / s


infile = open('pos.dat', 'r')
s = float(infile.readline())
lines = infile.readlines()
plots = len(lines)
x = np.zeros(plots)
y = np.zeros(plots)
vx = np.zeros(plots-1)
vy = np.zeros(plots-1)
t = np.linspace(0,plots*s,plots)

i = 0
for line in lines:
    words = line.split()
    x[i] = words[0]
    y[i] = words[1]
    i += 1
infile.close()


for i in range(plots-1):
    vx[i] = vel(i, x, s)
    vy[i] = vel(i, y, s)


plt.figure(1)
plt.subplots_adjust(hspace=1)
plt.subplot(3,1,1)
plt.title('Fart: x')
plt.xlabel('Tid: s')
plt.ylabel('Fart i x')
plt.plot(t[:-1], vx)


plt.subplot(3,1,2)
plt.title('Fart: y')
plt.xlabel('Tid: s')
plt.ylabel('Fart i y')
plt.plot(t[:-1], vy)


plt.subplot(3,1,3)
plt.title('Posisjon (x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)


plt.savefig('position2velocity.png')
plt.show()


'''
Terminal> position2velocity.py"

Process finished with exit code 0
'''