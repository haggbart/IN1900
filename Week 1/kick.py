# Compute the air resistance on a football
from math import pi


q = 1.2     # kgm^-3 (density of air)
a = 11/100      # m (radius of football)
A = pi*a**2
m = 0.43    # kg (mass of football)
g = 9.81    # ms^-2 (tyngdeakselerasjon)
Fg = m*g    # gravity force on football
CD = 0.4    # drag coefficient
V = [120/3.6, 70/3.6]     # m/s (velocity)
print("Gravitasjonskraften virker på fotballen med %g N" % round(Fg, 1))
for item in V:
    Fd = 1 / 2 * CD * q * A * item ** 2
    ratio = Fd/Fg
    print("""Blir ballen sparket med en fart på %g m/s, virker luftmotstanden på fotballen med en kraft på %g N.
     Forholdet Fd/Fg er %g.""" % (round(item,1), round(Fd,1), round(ratio,1)))

"""
Terminal> kick.py
Gravitasjonskraften virker på fotballen med 4.2 N
Blir ballen sparket med en fart på 33.3 m/s, virker luftmotstanden på fotballen med en kraft på 10.1 N.
     Forholdet Fd/Fg er 2.4.
Blir ballen sparket med en fart på 19.4 m/s, virker luftmotstanden på fotballen med en kraft på 3.4 N.
     Forholdet Fd/Fg er 0.8.

Process finished with exit code 0
"""