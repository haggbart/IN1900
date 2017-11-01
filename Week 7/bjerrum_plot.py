# Oppgave 5.5 fra kjemihefte
import numpy as np
import matplotlib.pyplot as plt

k1 = 5.01e-7
k2 = 4.79e-11

pH = np.linspace(4,12,200)
H = 10**-pH

co2 = H**2 / (H**2 + k1*H + k1*k2)
hco3 = (k1*H) / (H**2 + k1*H + k1*k2)
co3 = (k1*k2) / (H**2 + k1*H + k1*k2)

cross1 = np.argwhere(np.diff(np.sign(co2 - hco3)) != 0).reshape(-1) + 0
cross2 = np.argwhere(np.diff(np.sign(hco3 - co3)) != 0).reshape(-1) + 0
print(np.sign(hco3 - co3))
print(np.diff(np.sign(hco3 - co3)) != 0)


plt.plot(pH, co2, label = '[CO2(aq)]')
plt.plot(pH, hco3, label = '[HCO3-(aq)]')
plt.plot(pH, co3, label = '[CO32-(aq)]')
plt.plot(pH[cross1], co2[cross1], 'ro')
plt.plot(pH[cross2], hco3[cross2], 'ro')
plt.legend()
plt.title('Bjerrumplot')
plt.xlabel('pH')
plt.ylabel('Konsentrasjon')
plt.savefig('bjerrum_plot.png')
plt.show()

print('Kurvene til CO2 og HCO3- skjærer hverandre ved pH = %.2f' %(pH[cross1]))
print('Kurvene til HCO3 og CO32- skjærer hverandre ved pH = %.2f' %(pH[cross2]))


'''
Terminal> bjerrum_plot.py"
Kurvene til CO2 og HCO3- skjærer hverandre ved pH = 6.29
Kurvene til HCO3 og CO32- skjærer hverandre ved pH = 10.31

Process finished with exit code 0
'''