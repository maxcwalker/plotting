# This plotting scheme is for restart flies that logging horizontally up

import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("/home/maxwalker/git/SU2/tutorials/compressible/inviscid_bump/restart_flow.csv", names=True, delimiter = ',')

n = 3 # number of decimals to round values to
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
#mu = np.around(f['Laminar_Viscosity'], decimals=n)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

########################################################
#working out the mesh dimensions
y2 = []

#for i in range(len(y)):
#    if y[i] == max(y):
#        y2.append(y[i])
#    print(str(i)+" out of "+str(len(x)))

yg = 256#len(y2)

xg = len([x for x in x if x == 0])

#telling you the mesh dimensions used
print("------------------------------------------------------------------")
print("the mesh is a "+str(xg)+ "x" +str(yg)+" case")
print("------------------------------------------------------------------")
##########################################################
pos = "not sure"

y_pos = []
u_x = []
n = 120
for i in range(xg):
    y_pos.append(y[(i*yg)+n])
    u_x.append(u[(i*yg)+n])
 

#plotting the velocity profile
ax1 = plt.plot( u_x, y_pos, marker ='x' )
plt.xlabel("u") #/$U_{inf}$
plt.ylabel("normal position from the wall [m]")
plt.title("Velocity profile at point "+pos+"m along plate")

print("------------------------------------------------------------------")
print(len(x))
print(xg)
print("------------------------------------------------------------------")

newx = x.reshape((xg,int(len(x)/xg)))
newy = y.reshape(xg,int(len(x)/xg))
newT = T.reshape(xg,int(len(x)/xg))
newP = P.reshape(xg,int(len(x)/xg))
newU = u.reshape(xg,int(len(x)/xg))

fig, (ax1,ax2, ax3) = plt.subplots(3,1)
fig.set_size_inches(18.5, 10.5)
T = ax1.contourf(newx, newy, newT, levels = 1000, cmap=cm.jet ) 
ax1.set_title("Temperature Contours for a {}x{} grid".format(xg, yg))
ax1.set_ylabel("y")
ax1.set_ylim([0, 0.001])
tbar = plt.colorbar(T, ax=ax1)
tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

P = ax2.contourf(newx, newy, newP, levels = 1000)
ax2.set_title("Pressure Contours for a {}x{} grid".format(xg, yg))
ax2.set_ylabel("y")
#ax2.set_ylim([0, 0.001])
Pbar = plt.colorbar(P, ax=ax2)
Pbar.set_label("Pressure [Pa]" ) #rotation= 270
plt.legend

U = ax3.contourf(newx, newy, newU, levels = 1000)
ax3.set_title("X_Velocity Contours for a {}x{} grid".format(xg, yg))
ax3.set_xlabel("x")
ax3.set_ylabel("y")
#ax3.set_ylim([0, 0.001])
ubar = plt.colorbar(U, ax=ax3)
ubar.set_label("X_Velocity [ms$^{-1}$]" ) #rotation= 270
plt.legend

plt.show()