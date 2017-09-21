# 1.3 (half_life.py, side 5) fra fysikkheftet
from math import log, exp


# a
t = 10*60 # s (10 minutter)
tau = 1760 # s
N0 = 4.5 # kg (karbon-11)
N = N0* exp(-t/tau)
print("a) %.2f kg karbol-11 igjen etter %g minutter" % (N, t/60))


# b
thalv = 1220 # s
tau = thalv/(log(2))
N = N0* exp(-t/tau) # N beregnet på nytt med utregnet tidskosntant

print("""
b) Tidskonstanten, tau = %g 
 %.2f kg karbol-11 igjen etter %g minutter""" % (tau, N, t/60))


"""
Terminal> half_life.py"
a) 3.20 kg karbol-11 igjen etter 10 minutter

b) Tidskonstanten, tau = 1760.09 
 3.20 kg karbol-11 igjen etter 10 minutter

Process finished with exit code 0
"""