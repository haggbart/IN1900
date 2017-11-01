import math
def S(x,n):
    ajm1 = x
    s = ajm1
    for j in range(1,n+1):
        aj = -x**2 / ((2*j+1)*2*j) * ajm1
        s += aj
        ajm1 = aj
    aj = -x**2 / ((2*j+1)*2*j) * ajm1
    return s, aj
print(S(2,10))
print(math.sin(2))