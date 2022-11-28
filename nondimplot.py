#This script will calculate non dimensional plots
import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/tutorials/compressible/lam_flatplate/restart_flow.csv", names=True, delimiter = ',')

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

#---------------------------------------#
xg = 0
while x[xg]== x[xg+1]:
    xg +=1
xg = xg +1
yg = len([y for y in y if y==0])

#--------------------------------------#1
#position of wall at any given x position
n =  2 # - 2 just so its not at the outlet
pos_w = n*yg - 1
pos_w2 = pos_w -1 # first cell from wall

print(y[pos_w])
#wall shear stress
dudy = (u[pos_w-64:pos_w])/(y[pos_w-64:pos_w])
t_wall = mu[pos_w-64:pos_w]*(dudy)
print(t_wall)

u_tau = np.sqrt(t_wall/rho[pos_w-64:pos_w])
u_plus = u[pos_w-64:pos_w]/u_tau
nu = rho[pos_w-64:pos_w]/mu[pos_w-64:pos_w]
y_plus = (u_tau*y[pos_w-64:pos_w])/nu

plt.plot(u_plus,y_plus,marker='o')
plt.show()
