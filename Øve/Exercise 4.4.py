# Exercise 4.4, Filename: f2c_file_read_write



infile = open('Fdeg.dat', 'r')

infile.readline()
infile.readline()
infile.readline()

Fdegrees = []
Cdegrees = []


for line in infile:
    words = line.split()
    #print(words)
    F = float(words[-1])
    Fdegrees.append(F)
    C = (F-32)*(5.0/9)
    Cdegrees.append(C)

infile.close()

#print(Fdegrees, '\n', Cdegrees)
outfile = open('FCdeg.dat', 'w')

for F,C in zip(Fdegrees, Cdegrees):
    print(F,C)
    outfile.write('%5.1f %5.1f\n' %(F,C))
outfile.close()