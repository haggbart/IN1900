from math import sin,pi

def S(t,n, T):
    z = 0
    for i in range(1,n+1):
        z += 1 / (2 * i - 1) * sin((2 * (2 * i - 1) * pi * t) / T)
    z *= 4 / pi
    return z


def f(t, T):
    if 0 < t < T/2:
        res = 1
    elif abs(t - T/2) < 1e-14:
        res = 0
    elif T/2 < t < T:
        res = -1
    else:
        print('Error')
    return res

n = [1,3,5,10,30,100]
T = 2 * pi
a = [0.01,0.25,0.49]
t = [a*T for a in a]
print(t)
#t = a*T
for e in n:
    print('Testing %d' %(e))
    for i in t:
        #print(i,e,T)
        print('%15.9f %15.9f      Dif: %7.9f' %(S(i,e,T),f(i,T),abs(S(i,e,T)-f(i,T))))

n = 0
dt = (T-0)/(n+1)
print(dt)
t_list = []

plot(t_array,S_array)
show()