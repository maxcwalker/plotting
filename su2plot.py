#This plotting script is for a standard compressible flow

import numpy as np
import matplotlib.pyplot as plt
import math 

f = np.genfromtxt("../SU2/tutorials/compressible/lam_flatplate/restart_flow.csv", names=True, delimiter = ',')
n = 8 # number of decimals to round values to
x = np.around(f['x'], 5)
y = np.around(f['y'], 5)
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
print(rho)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)
print(u)

#working out the mesh dimensions
#for x
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

#telling you the mesh dimensions used
print("the mesh is a "+str(xg)+ "x" +str(yg)+" case")

i = len(x) - i
print("i is =" +str(i))

pos = (x[i])
pos = round(pos, 3)
pos = str(pos)

new_var = y_pos= y[i:i+63]
new_var
#y_pos = np.flip(y_pos)
u_x = u[i:i+63]
u_x = u_x/u_max
#u_x = np.flip(u_x)

#plotting the velocity profile
ax1 = plt.plot( u_x, y_pos)
plt.xlabel("u/$U_{inf}$")
plt.ylabel("normal position from the wall [m]")
plt.title("Velocity profile at point "+pos+"m along plate")
plt.xlim([0, 1])
plt.ylim([0,0.01])
plt.show()
exit()