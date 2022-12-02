#This plotting script is for a standard compressible flow

import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach6_comp_lam_plateNemo/restart_flow.csv", names=True, delimiter = ',')
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

#working out the mesh dimensions
#for x
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

else:
    i = 0
    yg = 1 #x grid points
    while y[i+1] == y[i]:
        if y[i+1] != y[i]:
            break
        i += 1
        yg += 1

    #for y
    j = 0
    xg = 0 #y grid points
    n = len(x)
    for j in range(n):
        if x[j] == 0:
            xg += 1
    j = i

#telling you the mesh dimensions used
print("------------------------------------------------------------------")
print("the mesh is a "+str(xg)+ "x" +str(yg)+" case")
print("------------------------------------------------------------------")

i = len(x) - i

pos = (x[i])
pos = str(round(pos, 3))

y_pos= y[i:i+yg]
u_x = u[i:i+yg]

#plotting the velocity profile
#ax1 = plt.plot( u_x, y_pos, marker='x')
#plt.xlabel("u") #/$U_{inf}$
#plt.ylabel("normal position from the wall [m]")
#plt.title("Velocity profile at point "+pos+"m along plate")
#plt.xlim([0, 1])
#plt.ylim([0,0.01])

newx = x.reshape((xg,int(len(x)/xg)))
newy = y.reshape(xg,int(len(x)/xg))
newT = T.reshape(xg,int(len(x)/xg))
newP = P.reshape(xg,int(len(x)/xg))
newU = u.reshape(xg,int(len(x)/xg))

fig, (ax1,ax2, ax3) = plt.subplots(3,1)
fig.set_size_inches(18.5, 10.5)
T = ax1.contourf( newx, newy, newT, levels = 1000, cmap=cm.jet ) 
ax1.set_title("Temperature Contours for a {}x{} grid".format(xg, yg))
ax1.set_ylabel("y")
ax1.set_ylim([0, 0.001])
#ax1.set_aspect(1)
tbar = plt.colorbar(T, ax=ax1)
tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

P = ax2.contourf(newx, newy, newP, levels = 1000)
ax2.set_title("Pressure Contours for a {}x{} grid".format(xg, yg))
ax2.set_ylabel("y")
ax2.set_ylim([0, 0.001])
#ax2.set_aspect(1)
Pbar = plt.colorbar(P, ax=ax2)
Pbar.set_label("Pressure [Pa]" ) #rotation= 270
plt.legend

U = ax3.contourf(newx, newy, newU, levels = 1000)
ax3.set_title("X_Velocity Contours for a {}x{} grid".format(xg, yg))
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_ylim([0, 0.001])
#ax3.set_aspect(1)
ubar = plt.colorbar(U, ax=ax3)
ubar.set_label("X_Velocity [ms$^{-1}$]" ) #rotation= 270
plt.legend

plt.show()