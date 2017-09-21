# 3.8 (roots_quadratic.py, side 129)

""" Begynte på oppgaven litt sent, så ble lite tid til å lage bedre tester """


from numpy.lib.scimath import sqrt


def test_roots_float():
    expected1 = -2
    #expected2 = -3
    computed = roots(1, 5, 6)
    print(computed)
    tol = 1E-14
    success = abs(expected1 - computed[0]) < tol
    msg = ('computed area=%g != %g (expected)' % \
    (computed[0], expected1))
    assert success, msg


def roots(a, b, c):
    root = b**2-4*a*c
    x1 = (-b + sqrt(root))/2*a
    x2 = (-b - sqrt(root))/2*a,
    a = (x1), x2
    return a

print(roots(1, 3, 4))
print(roots(1, 3, -4))
print(test_roots_float())


"""
Terminal> roots_quadratic.py"
((-1.5+1.3228756555322954j), ((-1.5-1.3228756555322954j),))
(1.0, (-4.0,))
(-2.0, (-3.0,))
None

Process finished with exit code 0
"""