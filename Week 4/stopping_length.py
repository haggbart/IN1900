# Exercise 4.16

v0 = [120/3.6, 50/3.6]
u = 0.3
g = 9.81

def d(v0, u=0.3):
    return 1/2*v0**2/(u*g)

print(d(10))
