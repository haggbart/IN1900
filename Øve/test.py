import numpy as np
x = np.array([1,2,3,4,5])
y = x[0:3]
y += 1
print(x)
print(y)

import numpy as np
x = np.array([1,2,3])
y = np.array([2,2,2])
z = y * x ** x
print(z)

import numpy as np
x = np.linspace(0,1,11)
y = x + x
print(y)