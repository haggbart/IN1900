# Oppgave 5.5 - Oscillerende fjær

import numpy as np
from matplotlib.pyplot import plot, xlabel, ylabel, show


def y(t):
    return A*np.exp(-gamma*t)*np.cos(np.sqrt(k/m)*t)


A = 0.3  # m
k = 4  # kg/s^2
gamma = 0.15  # s^-1
m = 9  # kg

start = 0
stop = 25
n = 101
dt = (stop-start)/(n - 1)


# Oppgave a)

t_array_old = np.zeros(n)
y_array_old = np.zeros(len(t_array_old))
for i in range(len(t_array_old)):
    t_array_old[i] = i*dt
    y_array_old[i] = y(t_array_old[i])


t_array = np.linspace(start,stop,n)
y_array = y(t_array)
plot(t_array, y_array)
plot(t_array_old, y_array_old)
xlabel('Tid (s)')
ylabel('Høyde (m)')
show()


'''
Terminal> oscilating_spring.py"

Process finished with exit code 0

oscilating_spring.png (se vedlegg)
Plots fra oppgave a og b er like og gjør at grafene ligger oppå hverandre.
'''