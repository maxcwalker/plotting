import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach2_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')
n = 10 # number of decimals to round values to
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

### -----mesh----- ###
xg = len([y for y in y if y ==0])
yg = int(len(y)/xg)
print("The mesh is {}x{}".format(xg,yg))
### -------------- ###
variable = P
y_pos = 0.01 #choose what point above the wall
y = np.around(y, 3 )
x_pos =[]
variable1 = []

for i in range(len(y)):
    if y[i] == y_pos:
        x_pos.append(x[i])
        variable1.append(variable[i])

print(len(x_pos))
plt.plot(x_pos,variable1)
plt.xlabel('X position [m]')
plt.ylabel('Pressure [Pa]')

plt.show()

