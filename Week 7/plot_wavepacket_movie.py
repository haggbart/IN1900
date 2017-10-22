# Exercise 5.33
# Slik jeg forstod det i følge piazza og forelesninger holder det å lage en animasjon.
import numpy as np
import matplotlib.pyplot as plt

t = 0
x = np.linspace(-6, 6, 1001)

def wave(x, t):
    return np.exp(-(x-3*t)**2) * np.sin(3*np.pi*(x-t))


for t in np.linspace(-1,1,61):
    plt.ylim(-1.1,1.1)
    y = wave(x, t)
    plt.plot(x,y)
    plt.pause(1/6)           # Ser at animasjonen ender opp med å være lenger enn forventet
    plt.cla()                # Finnes det et bedre alternativ for å fjerne plot, men beholde aksene? Skulle gjerne hatt ylim utenfor loopen.

plt.show()


'''
Terminal> plot_wavepacket_movie.py"

Process finished with exit code 0
'''