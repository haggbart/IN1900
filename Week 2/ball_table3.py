# 2.17 ball_table3.py, side 86


v0 = 5  # m/s
g = 9.81  # m/s^2

t_stop = 2*v0/g
dt = t_stop/5

n = 5
tlist = []  # definerer lister
ylist = []


for i in range(n+1):  # lager listene
    tlist.append(i*dt)
    ylist.append(v0 * tlist[i] - 1 / 2 * g * tlist[i] ** 2)  # meter
ty1 = [tlist, ylist]  # lager tabel, 2 lister i en liste
print("--[ty1]---->")
for i in range(len(ty1[0])):
    print("Tid: %5.2fs Høyde: %5.2f meter" % (ty1[0][i], ty1[1][i]))


ty2 = [[t, y] for t, y in zip(tlist, ylist)] # lager tabel2, en liste med lister
print("--[ty2]---->")
for i in range(len(ty2)):
    print("Tid: %5.2fs Høyde: %5.2f meter" % (ty2[i][0], ty2[i][1]))

"""
Terminal> ball_table3.py"
--[ty1]---->
Tid:  0.00s Høyde:  0.00 meter
Tid:  0.20s Høyde:  0.82 meter
Tid:  0.41s Høyde:  1.22 meter
Tid:  0.61s Høyde:  1.22 meter
Tid:  0.82s Høyde:  0.82 meter
Tid:  1.02s Høyde:  0.00 meter
--[ty2]---->
Tid:  0.00s Høyde:  0.00 meter
Tid:  0.20s Høyde:  0.82 meter
Tid:  0.41s Høyde:  1.22 meter
Tid:  0.61s Høyde:  1.22 meter
Tid:  0.82s Høyde:  0.82 meter
Tid:  1.02s Høyde:  0.00 meter

Process finished with exit code 0
"""