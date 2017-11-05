import numpy as np
from math import sqrt

class Quadratic(object):
    def __init__(self, a, b, c):
         self.a, self.b, self.c = a, b, c

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c

    @staticmethod
    def table(L, R, n=10):
        x = np.linspace(L, R, n)
        y = q.value(x)
        return zip(x, y)

    def root(self):
        a, b, c = self.a, self.b, self.c
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        return x1, x2


q = Quadratic(2, 10, 5)
print(q.value(2))
print(q.table(0,2,5))
print(q.root())
print(list(q.table(0,5)))
for e in list(q.table(0,5)):
    print('x: %-10.2f y: %-10.2f' % (e[0], e[1]))