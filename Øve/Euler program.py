
def ForwardEuler(f, U0, T, n):
    '''Solve u'=f(u,t), u(0)=U0, with n steps until t=T.'''
    import numpy as np
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]

    t[0] = 0
    u[0] = U0

    dt = T/float(n)

    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

def f(u, t):
    return u

U0 = 1
T = 3
n = 100
u, t = ForwardEuler(f, U0, T, n)

#print(u)
#print(t)


import matplotlib.pyplot as ppl
from numpy import exp
u_exact = exp(t)
ppl.plot(t, u, 'r-', label='numerical')
ppl.plot(t, u_exact, 'b-', label='exact')
ppl.title("Solution of the ODE u'=u, u(0)=1")
ppl.xlabel('t'), \
ppl.ylabel('u')
ppl.legend()
ppl.show()