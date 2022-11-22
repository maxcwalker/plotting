import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("/home/maxwalker/git/SU2/tutorials/compressible/lam_flatplate/restart_flow.csv", names=True, delimiter = ',')
n = 10
x = np.around(f['x'],n )
y = np.around(f['y'], n)
rho = np.around(f['Density'], decimals=n)
rhou = np.around(f['Momentum_x'], decimals=n)
rhov = np.around(f['Momentum_y'], decimals=n)

u = rhou/rho
v = rhov/rho
u_max = max(u)

if x[0] == x[1]:
    i = 0
    xg = 1 #x grid points
    while x[i+1] == x[i]:
        if x[i+1] != x[i]:
            break
        i += 1
        xg += 1

    #for y
    j = 0
    yg = 0 #y grid points
    n = len(y)
    for j in range(n):
        if y[j] == 0:
            yg += 1

i = len(x) - i

pos = (x[i])
pos = str(round(pos, 3))
y_pos= y[i:i+yg]
u_x = u[i:i+yg]
u_max = max(u_x)

#u_x = [x for x in u_x if x <= 0.99*u_max]
u_x2 =[]
y_pos2 =[]
for i in range(len(u_x)):
    if u_x[i] <= 0.99*u_max:
        u_x2.append(u_x[i])
        y_pos2.append(y_pos[i])
ub_nondim = u_x2/max(u_x2)
yb_nondim = y_pos2/max(y_pos2)

#plotting the velocity profile [dimensional]
#plt.plot( u_x2, y_pos2)
#plt.xlabel("u") #/$U_{inf}$
#plt.ylabel("normal position from the wall [m]")
#plt.title("Velocity profile at point "+pos+"m along plate")

#plotting the velocity profile [non dimensional]
plt.plot( ub_nondim, yb_nondim)
plt.xlabel("u/$U_\infty$")
plt.ylabel("$y/\delta$")
plt.title("Laminar boundary layer at "+pos+"m along plate for a {}x{} mesh".format(xg,yg))

plt.show()