# Oppgave 5.5 fra kjemihefte
import numpy as np
import matplotlib.pyplot as plt

k1 = 5.01e-7
k2 = 4.79e-11

pH = np.linspace(4,12,100)
H = 10**-pH

co2 = H**2 / (H**2 + k1*H + k1*k2)
hco3 = (k1*H) / (H**2 + k1*H + k1*k2)
co3 = (k1*k2) / (H**2 + k1*H + k1*k2)

plt.plot(pH, co2, label = '[CO2(aq)]')
plt.plot(pH, hco3, label = '[HCO3-(aq)]')
plt.plot(pH, co3, label = '[CO32-(aq)]')
plt.legend()
plt.title('Bjerrumplot')
plt.xlabel('pH')
plt.ylabel('Konsentrasjon')
plt.savefig('bjerrum_plot.png')
plt.show()


'''
Terminal> bjerrum_plot.py"

Process finished with exit code 0
'''