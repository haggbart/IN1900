# 3.4 (f2c.py, side 128)

"""
Write a function C(F) that implements this formula. Also write the inverse function
F(C) for going from Celsius to Fahrenheit degrees. How can you test that the two
functions work?
Hint C(F(c)) should result in c and F(C(f)) should result in f.
"""
# C = []
# C = list(range(0,45,5))
# dC = 10
# # for i in range(10):
# #     C.append(i*dC)
# print(C)

def C(f):
    C = 5/9*(f-32)
    return C
def F(c):
    F = (9*c+160)/5
    return F



for c in range(-50,50+10,10):
    print("C: %3g   F:%6.2f   C(calc): %6.2f" % (c, F(c), C(F(c))))
print("---------")

for f in range(-58,128+10,10):
    print("F: %3g   C:%6.2f   F(calc): %6.2f" % (f, C(f), F(C(f))))