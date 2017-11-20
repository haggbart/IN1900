class Sum:
    def __init__(self, fk, M, N):
        self.fk = fk
        self.M = M
        self.N = N

    def __call__(self, x):
        S = 0
        for k in range(self.M, self.N+1):
            S += self.fk(k, x)
        return S

    def term(self, k, x):
        return self.fk(k,x)


def test_Sum():
    def fk(k,x):
        return x**k
    M = 0
    N = 2
    x = 0.5
    expected = 1.0 + x + x**2
    tol = 1e-14
    S = Sum(fk,M,N)
    computed = S(x)
    success = abs(expected - computed) < tol
    assert success


print("a:")
def term(k, x):
    return (-x)**k

S = Sum(term, M=0, N=3)
x = 0.5
print(S(x))
print(S.term(k=4, x=x))

print("b:")
test_Sum()

print("c:")
from math import factorial, pi

def f_sin(k,x):
    return (-1)**k*(x**(2*k+1))/factorial(2*k+1)

Taylor_sin = Sum(f_sin,0,14)
print(Taylor_sin(pi), Taylor_sin(pi/2), Taylor_sin(pi/4))