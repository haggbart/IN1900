# Exercise 7.1
from math import exp, sin

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        return exp(-self.a*x)*sin(self.w*x)

f1 = F(1.0, 0.1)

f2 = F(2.0, 0.1)

print(f1.w,f2.w)
print(f1.value(3.14))
print(f2.value(3.14))
