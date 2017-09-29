# Exercise 4.14
# -*- coding: utf-8 -*-
import numpy as np


def test_read():
    outfile = open("test_read.dat", 'w')
    outfile.write('v0: 6 \n')
    outfile.write('t:\n')
    outfile.write('0.1 10\n')
    outfile.write('0.5 5\n')
    outfile.close()
    exp1 = 6
    exp2 = [0.1, 10, 0.5, 5]
    computed = read('test_read.dat')
    success = exp1 == computed[0] and exp2 == computed[1]
    msg = 'Feil i funksjon read(file)'
    assert success, msg


def read(file):
    infile = open(file)
    v0 = float(infile.readline().split(':')[1])  # m/s
    infile.readline()
    tlist = []
    for line in infile:
        t = line.split()
        tlist += map(float, t)
    infile.close()
    return v0, tlist
print(test_read())  # Tester funksjonen read()


file = "ball.dat"
res = read(file)
#print(res)
#print(test_read())

#print(sorted(tlist))
g = 9.81    # m/s
v0 = res[0] # m/s
t = np.array(sorted(res[1]))     # Sorterer med økende tid

y = v0*t-0.5*g*t**2
#print(y)

outfile = open('ball_output.dat', 'w')
for t, y in zip(t,y):
    #print(t,y)
    outfile.write('%5.2f %5.2f\n' % (t,y))
outfile.close()

'''
a)
Terminal> python ball_file_read_write.py 
(3.0, [0.15592, 0.28075, 0.36807889, 0.35, 0.57681501876, 0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 0.21385894, 0.3464815, 0.57982969, 0.10262264, 0.29584013, 0.17383923])


b)
Terminal> python ball_file_read_write.py 
(6.0, [0.1, 10.0, 0.5, 5.0])
None


c)
Terminal> python ball_file_read_write.py 
None

fra ball_output.dat:
 0.04  0.12
 0.05  0.14
 0.10  0.26
 0.11  0.27
 0.16  0.35
 0.17  0.37
 0.21  0.41
 0.21  0.42
 0.21  0.42
 0.27  0.45
 0.28  0.46
 0.30  0.46
 0.35  0.45
 0.35  0.45
 0.37  0.44
 0.37  0.44
 0.39  0.42
 0.51  0.26
 0.53  0.22
 0.53  0.21
 0.58  0.10
 0.58  0.09
'''