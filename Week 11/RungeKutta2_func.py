

import matplotlib.pyplot as ppl
import numpy as np


def RungeKutta2(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)

    t[0] = 0
    u[0] = U0

    dt = T/float(n)

    for k in range(n):
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 1/2*K1, t[k]+ 1/2*dt)
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + K2

    return u, t

def f(u, t):
    return u*2

U0 = 1
T = 3
n = 100

i = [2, 4, 8, 16, 64]

for i in i:
    n = i
    u, t = RungeKutta2(f, U0, T, n)
    ppl.plot(t, u, '-', label='numerical: n=%d' %n)

4
u_exact = np.exp(t*2)
ppl.plot(t, u_exact, 'b-', label='exact')
ppl.title("Solution of the ODE u'=u, u(0)=1")
ppl.xlabel('t'), \
ppl.ylabel('u')
ppl.legend()
ppl.savefig('RungeKutta2_func.png')
ppl.show()


''' Demonsterer ved hjelp av figur at nummerisk løsning nærmer seg analytisk løsning når dt minkes.
Terminal> RungeKutta2_func.py"

Process finished with exit code 0
'''