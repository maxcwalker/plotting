# This plotting scheme is for restart flies that logging horizontally up

import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../../SU2/inv_bump_mach2/restart_flow.csv", names=True, delimiter = ',')

n = 5 # number of decimals to round values to
x = np.around(f['x'], n )
y = np.around(f['y'], n )
rho = np.around(f['Density'], decimals=n)
rhou = np.around(f['Momentum_x'], decimals=n)
rhov = np.around(f['Momentum_y'], decimals=n)
E= np.around(f['Energy'], decimals=n)
P = np.around(f['Pressure'], decimals=n)
T = np.around(f['Temperature'], decimals=n)
cp = np.around(f['Pressure_Coefficient'], decimals=n)
#mu = np.around(f['Laminar_Viscosity'], decimals=n)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

########################################################
#working out the mesh dimensions
xg = 0
x_max = max(x)
while x[xg] != x_max:
    xg+=1
xg = xg +1 
yg = int(len(x)/xg)
#telling you the mesh dimensions used
print("------------------------------------------------------------------")
print("the mesh is a "+str(xg)+ "x" +str(yg)+" case")
print("------------------------------------------------------------------")
##########################################################

y_pos = []
u_x = []
x_pos = 2
i = 0
for i in range(len(x)):
    if x[i] == x_pos:
        y_pos.append(y[i])
        u_x.append(u[i])
        print(i)
u_x = u_x/u_max


#plotting the velocity profile
ax1 = plt.plot( u_x, y_pos )
plt.xlabel("u") #/$U_{inf}$
plt.ylabel("normal position from the wall [m]")
plt.title("Velocity profile in wall normal direction at point {}m".format(x_pos))

newx = x.reshape(yg,xg)
newy = y.reshape(yg,xg)
newT = T.reshape(yg,xg)
newP = P.reshape(yg,xg)
newU = u.reshape(yg,xg)
levels1 = 100

fig, (ax1,ax2, ax3) = plt.subplots(3,1)
fig.set_size_inches(10, 10.5)
T = ax1.contourf(newx, newy, newT, levels = levels1 ) 
ax1.set_title("Temperature Contours for a {}x{} grid".format(xg, yg))
ax1.set_ylabel("y")
ax1.set_aspect(1)
tbar = plt.colorbar(T, ax=ax1)
tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

P = ax2.contourf(newx, newy, newP, levels = levels1)
ax2.set_title("Pressure Contours for a {}x{} grid".format(xg, yg))
ax2.set_ylabel("y")
ax2.set_aspect(1)
Pbar = plt.colorbar(P, ax=ax2)
Pbar.set_label("Pressure [Pa]" ) #rotation= 270
plt.legend

U = ax3.contourf(newx, newy, newU, levels = levels1 )
ax3.set_title("X_Velocity Contours for a {}x{} grid".format(xg, yg))
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_aspect(1)
#ax3.set_ylim([0,0.1])
#ax3.set_xlim([0.8,1.1])
ubar = plt.colorbar(U, ax=ax3)
ubar.set_label("X_Velocity [ms$^{-1}$]" ) #rotation= 270
plt.legend

plt.show()