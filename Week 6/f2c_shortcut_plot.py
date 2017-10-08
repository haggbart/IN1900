# Exercise 5.12

import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(-20,120,100)

C_inexact = (F-30)/2
C_exact = (F-32)*5/9


print(C_inexact)
print(C_exact)

plt.plot(F,C_inexact,'y-',label = 'inexact')
plt.plot(F,C_exact,'b-',label = 'exact')
plt.legend()
plt.title('inexact vs exact')
plt.xlabel('F')
plt.ylabel('C')
plt.savefig('inexact_vs_exact.png')
plt.show()