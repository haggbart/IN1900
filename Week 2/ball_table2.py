v0 = 5  # m/s
g = 9.81  # m/s^2

t_stop = 2*v0/g
dt = t_stop/10

n = 10
tlist = []
ylist = []
for i in range(n+1):
    tlist.append(i*dt)
    ylist.append(v0 * tlist[i] - 1 / 2 * g * tlist[i] ** 2)  # meter
for t, y in zip(tlist, ylist):
    print("Tid: %5.2fs Høyde: %5.2f meter" % (t, y))


"""
Terminal> ball_table2.py"
Tid:  0.00s Høyde:  0.00 meter
Tid:  0.10s Høyde:  0.46 meter
Tid:  0.20s Høyde:  0.82 meter
Tid:  0.31s Høyde:  1.07 meter
Tid:  0.41s Høyde:  1.22 meter
Tid:  0.51s Høyde:  1.27 meter
Tid:  0.61s Høyde:  1.22 meter
Tid:  0.71s Høyde:  1.07 meter
Tid:  0.82s Høyde:  0.82 meter
Tid:  0.92s Høyde:  0.46 meter
Tid:  1.02s Høyde:  0.00 meter

Process finished with exit code 0
"""