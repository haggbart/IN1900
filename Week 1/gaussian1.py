from math import exp, pi, sqrt


m = 0.0
s = 2.0
x = 1.0

print(1/(sqrt(2*pi)*s)*exp(-1/2*((x-m)/s)**2))


"""
Terminal> gaussian1.py
0.17603266338214976

Process finished with exit code 0
"""