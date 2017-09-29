# Exercise 4.16

"""
Jeg forstår ikke poenget med oppgaven,
håper jeg har gjort det riktig.
"""

import sys

v0 = float(sys.argv[1])/3.6
u = float(sys.argv[2])
g = 9.81


def d(v0, u):
    return 1/2*v0**2/(u*g)


print("Bremselengde med fart %.2f km/t og friksjonskoeffisent %g: \n %.1f meter" %(v0*3.6, u, d(v0, u)))


"""
Terminal> stopping_length.py" 120 0.3
Bremselengde med fart 120.00 km/t og friksjonskoeffisent 0.3: 
 188.8 meter

Process finished with exit code 0
--------------------------------
Terminal> stopping_length.py" 50 0.3
Bremselengde med fart 50.00 km/t og friksjonskoeffisent 0.3: 
 32.8 meter

Process finished with exit code 0
"""