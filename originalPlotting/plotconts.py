import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm # latex module
#import pandas as pd # may not need

f = np.genfromtxt("restart_flow.csv", names = True, delimiter=',')

#extracting the variables
n = 15 # number of decimals to round to
x = np.around(f['x'], decimals=n)
y = np.around(f['y'], decimals=n)
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

# ######################## #
# ######################## #

newx = x.reshape((65,65))
newy = y.reshape((65,65))
newT = T.reshape((65,65))
newP = P.reshape((65,65))


fig, (ax1,ax2) = plt.subplots(2,1)
fig.set_size_inches(18.5, 10.5)
T = ax1.contourf(newx, newy, newT, levels = 100, cmap=cm.jet ) 
ax1.set_title("Temperature Contours")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
tbar = plt.colorbar(T, ax=ax1)
tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

P = ax2.contourf(newx, newy, newP, levels = 100)
ax2.set_title("Pressure Contours")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
Pbar = plt.colorbar(P, ax=ax2)
Pbar.set_label("Pressure [Pa]" ) #rotation= 270

plt.show()
