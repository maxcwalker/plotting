
#plotting the velocity profile [non dimensional]
import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach1_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')
n = 15 # number of decimals to round values to
x = np.around(f['x'],n )
y = np.around(f['y'], n)
try:
    rho = np.around(f['Density'], decimals=n)
except:
    rho1 = np.around(f['Density_0'], decimals=n)
    rho2 = np.around(f['Density_1'], decimals=n)
    rho3 = np.around(f['Density_2'], decimals=n)
    rho4 = np.around(f['Density_3'], decimals=n)
    rho5 = np.around(f['Density_4'], decimals=n)
    rhon = [rho1,rho2,rho3,rho4,rho5]
    rho = sum(rhon)

rhou = np.around(f['Momentum_x'], decimals=n)
rhov = np.around(f['Momentum_y'], decimals=n)
E= np.around(f['Energy'], decimals=n)
P = np.around(f['Pressure'], decimals=n)
try:    
    T = np.around(f['Temperature'], decimals=n)
except:
    T = np.around(f['Temperature_tr'], decimals=n)
ma = np.around(f['Mach'], decimals=n)
cp = np.around(f['Pressure_Coefficient'], decimals=n)
mu = np.around(f['Laminar_Viscosity'], decimals=n)
# velocity from the momentum
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

i = len(x) - yg*int((xg*0.04))

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

plt.plot(ub_nondim,yb_nondim, color = 'green', marker='x')
plt.title("Laminar boundary layer at {}m along plate for a {}x{} mesh \n the boundary layer contains {} points".format(pos,xg,yg,len(yb_nondim)))
plt.xlabel("$u/U_\infty$")
plt.ylabel("$y/\delta$")
plt.show()