import numpy as np

class Decay:
    def __init__(self, U0, T, n):
        self.U0, self.T, self.n = U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(self.n+1)
        self.t = np.zeros(self.n+1)

    def __call__(self, a):
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        self.a = a
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u, dt, f, k, t, f = self.u, self.dt, self.f, self.k, self.t, self.f
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

    def f(self, u, t):
        a = self.a
        return -a*u

def f(u, t):
    a = np.log(2)/5600 # 1/y
    return -a*u

solver = Decay(U0=1, T=20000, n=int(20000/500))
u,t = solver(np.log(2)/5600)

import matplotlib.pyplot as plt
plt.plot(t,u)
plt.xlabel('Year')
plt.ylabel('Fraction of particles left')
plt.title("Radioactive Decay")
plt.savefig('radioactive_decay.py.png')
plt.show()

print('Final u(T) value: %.4f' % u[-1])
print('Exact value: %.4f' % np.exp(-np.log(2)/5600*20000))


'''
Terminal> radioactive_decay.py"
Final u(T) value: 0.0777
Exact value: 0.0841

Process finished with exit code 0
'''