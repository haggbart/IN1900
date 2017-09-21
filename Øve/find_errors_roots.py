# 1.17 (find_errors_roots.py, side 48)

a = 2; b = 1; c = 2
from math import sqrt
from cmath import sqrt


q = b*b - 4*a*c
q_sr = sqrt(q)
print(q)
x1 = (-b + q_sr)/2*a
x2 = (-b - q_sr)/2*a

print(x1, x2)