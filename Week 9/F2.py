from math import exp, sin

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        return exp(-self.a*x)*sin(self.w*x)

    def __call__(self, x):
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self):
        return 'exp(-a*x)*sin(w*x)'


# from F import F
#f = F(1.0, 0.1)
from math import pi
#print(f(x=pi))
#f.a = 2
#print(f(pi))
#print(f)


'''
Fra Python Console: 

from F import F
f = F(1.0, 0.1)
from math import pi
print(f(x=pi))
0.01335383513703555
f.a = 2
print(f(pi))
0.0005770715401197441
print(f)
exp(-a*x)*sin(w*x)

'''