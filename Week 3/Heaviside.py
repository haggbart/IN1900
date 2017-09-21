# 3.29 (Heaviside.py, side 139)

def test_Heaviside():
    """

    """
    x = 10
    expected = 1
    computed = Heaviside(x)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = ('computed area=%g != %g (expected)' % \
    (computed, expected))
    assert success, msg

def Heaviside(x):
    if x < 0:
        return 0
    else:
        return 1

print(Heaviside(-10))
print(Heaviside(-10**-15))
print(Heaviside(0))
print(Heaviside(10))
print(test_Heaviside())


"""
Terminal> Heaviside.py
0
0
1
1
None

Process finished with exit code 0
"""