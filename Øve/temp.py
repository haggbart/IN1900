# Exercise 3.7

def sum_1k(M):
    s = 0
    for k in range(1, M+1):
        s += 1.0/k
    return s

def test_sum_1k():
    M = 3
    expected = 1 + 1.0/2 + 1.0/3
    computed = sum_1k(M)
    success = abs(expected-computed) < 1E-14
    message = 'Error detected'
    assert success, message

    M = 4
    expected = 1 + 1.0/2 + 1.0/3 + 1.0/4
    computed = sum_1k(M)
    success = abs(expected-computed) < 1E-14
    message = 'Error detected'
    assert success, message
test_sum_1k()