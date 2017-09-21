

v0 = 5  # m/s
g = 9.81  # m/s^2

t_stop = 2*v0/g
dt = t_stop/10


#y = v0*t-1/2*g*t**2
n = 10

for i in range(n+1):
    t = i*dt
    y = v0 * t - 1 / 2 * g * t ** 2  # meter
    print("Tid: %5.2fs Høyde: %5.2f meter" % (t, y))
t = 0
print("--[while loop]---->")
while t <= t_stop:
    y = v0 * t - 1 / 2 * g * t ** 2  # meter
    print("Tid: %5.2fs Høyde: %5.2f meter" % (t, y))
    t = t + dt