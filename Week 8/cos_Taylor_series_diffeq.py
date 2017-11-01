import numpy as np
import matplotlib.pyplot as plt


def cos_Taylor2(x, n):
    s = 0
    a = 1
    for i in range(0, n+1):
        s = s+a
        a = -a*x**2 / ((2*i+1)*(2*i+2))
    return s, abs(a)
vcos = np.vectorize(cos_Taylor2)


def cos_two_terms(x):
    s = 0
    a = 1
    s = s+a
    a = -a*x**2 / ((2*0+1)*(2*0+2))
    s = s + a
    a = -a*x**2 / ((2*1+1)*(2*1+2))
    s = s + a
    a = -a*x**2 / ((2*2+1)*(2*2+2))
    return s, abs(a)


def test_cos_Taylor():
    x = 0.63
    tol = 1e-14
    s_expected, a_expected = cos_two_terms(x)
    s_computed, a_computed = cos_Taylor2(x,2)
    success1 = abs(s_computed - s_expected) < tol
    success2 = abs(a_computed - a_expected) < tol
    success = success1 and success2
    message = 'Output is different from expected!'
    assert success, message
test_cos_Taylor()


x = np.linspace(-5,5,100)
n = [0,2,4,6]
for i in n:
    y = vcos(x, i)
    plt.plot(x, y[0], label='n = %g' % i)
y = np.cos(x)
plt.plot(x, y, 'b-', label = 'expected')
plt.ylim(-1.1,1.1)
plt.legend()
plt.savefig('cos_Taylor_series_diffeq.png')
plt.show()


'''
Terminal> cos_Taylor_series_diffeq.py"

Process finished with exit code 0
'''