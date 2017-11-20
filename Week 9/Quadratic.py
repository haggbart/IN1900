import numpy as np
from math import sqrt

class Quadratic(object):
    def __init__(self, a, b, c):
         self.a, self.b, self.c = a, b, c

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c

    def table(self, L, R, n=5):
        x = np.linspace(L, R, n)
        y = self.value(x)
        return zip(x, y)

    def root(self):
        a, b, c = self.a, self.b, self.c
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        return x1, x2

def test_value():
    q = Quadratic(2, 4, 2)
    computed = q.value(2)
    expected = 18
    tol = 1e-14
    success = abs(computed - expected) < tol
    msg = 'test value error'
    assert success, msg
test_value()

def test_root():
    q = Quadratic(2, 4, 2)
    computed1, computed2 = q.root()[0], q.root()[1]
    expected1, expected2 = -1.0, -1.0
    tol = 1e-14
    success1 = abs(computed1 - expected1) < tol
    success2 = abs(computed2 - expected2) < tol
    success = success1 and success2
    msg = 'test root error'
    assert success, msg
test_root()

q = Quadratic(1, 4, 4)
print('f(2) = %g' %q.value(2))
print('Roots: %g, %g' % (q.root()[0],q.root()[1]))
print('----------------------')
for e in list(q.table(0,2)):
    print('x: %-10.2f y: %-10.2f' % (e[0], e[1]))


'''
Terminal> Quadratic.py"
f(2) = 16
Roots: -2, -2
----------------------
x: 0.00       y: 4.00      
x: 0.50       y: 6.25      
x: 1.00       y: 9.00      
x: 1.50       y: 12.25     
x: 2.00       y: 16.00     

Process finished with exit code 0
'''