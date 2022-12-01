#This script will calculate non dimensional plots
import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach6_comp_lam_plateNemo/restart_flow.csv", names=True, delimiter = ',')

n = 8 # number of decimals to round values to
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
#if x[0] == x[1]:
p = 0
while x[p] == x[p+1]:
    p += 1
yg = p +1
xg = len([y for y in y if y==0])
#else:
#    yg = len([x for x in x if x==0])
#    lg = 0
#    while y[lg] == y[lg+1]:
#        lg +=1
#    xg = lg +1

print("The mesh is {}x{}".format(xg,yg))
#--------------------------------------#
#position of wall at any given x position
n =  yg-2# - 2 just so its not at the outlet
pos_w = n*yg +yg -1 
pos_w2 = pos_w -1 # first cell from wall

print(y[pos_w])
#wall shear stress
dudy = (u[pos_w2])/(y[pos_w2])
t_wall = mu[(pos_w-yg+1):pos_w]*(dudy)

u_tau = np.sqrt(t_wall/rho[(pos_w-yg+1):pos_w])
u_plus = u[(pos_w-yg+1):pos_w]/u_tau
nu = rho[(pos_w-yg+1):pos_w]/mu[(pos_w-yg+1):pos_w]
y_plus = (u_tau*y[(pos_w-yg+1):pos_w])/nu

plt.plot(u_plus,y_plus)
#plt.scatter(x,y)

plt.show()
