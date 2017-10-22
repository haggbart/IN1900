# Exercise A.5

import matplotlib.pyplot as plt

F = 10000
x0 = F

p = 5
q = 30
I = 1
c0 = (p*q)/10**4*F
N = 10
xnm1 = x0
cnm1 = c0

x_list = [x for x in range(N+1)]
y_list = [x0]
n = 0
while n < N:
    xn = xnm1 + (p/100)*xnm1-cnm1
    y_list.append(xn)
    xnm1 = xn
    cn = cnm1 + I/100*cnm1
    cnm1 = cn
    n += 1
print(round(xn,2))
plt.plot(x_list, y_list)
plt.ylabel('Fortune')
plt.xlabel('Year')
plt.savefig('fortune_and_inflation1.png')
plt.show()


'''
Terminal> fortune_and_inflation1.py"
14322.92

Process finished with exit code 0
'''