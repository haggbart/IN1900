def sin_Taylor(x,n):
    s = [0.0]*(n+2)
    a = [0.0]*(n+2); a[0] = x
    for i in range(1, n+2):
        s[i] = s[i-1] + a[i-1]
        a[i] = -a[i-1]*x**2 / (2*i*(2*i+1))

    return s[n+1], abs(a[n+1])


def sin_Taylor2(x, n):
    s = 0
    a = x
    for i in range(1, n+2):
        s = s+a
        a = -a*x**2 / (2*i*(2*i+1))
    return s, abs(a)


def sin_two_terms(x):
    s = [0]*4
    a = [0]*4
    a[0] = x

    s[1] = s[0] + a[0]
    a[1] = -a[0]*x**2 / (2*1*(2*1+1))

    s[2] = s[1] + a[1]
    a[2] = -a[1]*x**2 / (2*2*(2*2+1))

    s[3] = s[2] + a[2]
    a[3] = -a[2]*x**2 / (2*3*(2*3+1))

    return s[3], abs(a[3])


def test_sin_Taylor():
    x = 0.63
    tol = 1e-14
    s_expected, a_expected = sin_two_terms(x)
    s_computed, a_computed = sin_Taylor(x,2)
    success1 = abs(s_computed - s_expected) < tol
    success2 = abs(a_computed - a_expected) < tol
    success = success1 and success2
    message = 'Output is different from expected!'
    assert success, message


def make_table(M,N):
    import numpy as np
    x = np.linspace(0, 1, M)
    n = np.arange(1, N+1)
    S = np.zeros((M,N))
    print(S)
    for i in range(M):
        for j in range(N):
            S[i,j] = sin_Taylor(x[i], n[j])[0]
    return S, x, n
#print(make_table(10,10))

#print(sin_two_terms(0.63))
#print(sin_Taylor(0.63, 2))
#print(test_sin_Taylor())

#print(sin_Taylor(2,10))
#print(sin_Taylor2(2,10))

