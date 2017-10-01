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


def write(fileoutput, t, y):
    outfile = open(fileoutput, 'w')
    outfile.write('%6s %6s \n' % ('t(s)', 'y(m)'))
    for t, y in zip(t,y):
        outfile.write('%6.3f %6.3f\n' % (t,y))
    outfile.close()
    print("Wrote to %s" % fileoutput)


file = "ball.dat"
fileoutput = "ball_output.dat"
res = read(file)

#print(res)
#print(test_read())

#print(sorted(tlist))
g = 9.81    # m/s
v0 = res[0] # m/s
t = np.array(sorted(res[1]))     # Sorterer med økende tid
y = v0*t-0.5*g*t**2
write(fileoutput, t, y)



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
  t(s)   y(m) 
 0.042  0.117
 0.052  0.143
 0.103  0.256
 0.112  0.274
 0.156  0.349
 0.174  0.373
 0.209  0.413
 0.213  0.417
 0.214  0.417
 0.270  0.452
 0.281  0.456
 0.296  0.458
 0.346  0.451
 0.350  0.449
 0.368  0.440
 0.373  0.437
 0.393  0.421
 0.506  0.262
 0.528  0.217
 0.530  0.212
 0.577  0.098
 0.580  0.090
'''