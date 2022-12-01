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

#working out the mesh dimensions
#for x

i = 0
yg = 1 #x grid points
while x[i+1] == x[i]:
    if x[i+1] != x[i]:
        break
    i += 1
    yg += 1 

xg = len([y for y in y if y == 0])
print("This is a {}x{} mesh".format(xg,yg))
n = 2
y_xloc1 = xg*yg - n*yg  # array pf y at a cetain x location
y_xloc2 = xg*yg - (n-1)*yg

U = np.full((y_xloc2-y_xloc1),max(u))
print(U.shape)
y = y[y_xloc1:y_xloc2]
print(y.shape)
x = x[y_xloc1:y_xloc2]
u = u[y_xloc1:y_xloc2]
nu = rho[y_xloc1:y_xloc2]/mu[y_xloc1:y_xloc2]
print(nu.shape)

eta = y*np.sqrt(U/(nu*x))
print(eta.shape)
u_max = max(u)
ub =[]
etab =[]
for i in range(len(u)):
    if u[i] <= 0.99*u_max:
        ub.append(u[i])
        etab.append(eta[i])
ub_ndim = ub/u_max

#blasius f''' + ff'' = 0
def f(x):
    dxdt = u[1]
    dvdt = u[2]
    dwdt = -u[0]*u[2]
    return np.array([dxdt,dvdt,dwdt])







#plt.plot(ub_ndim,etab)
#plt.xlabel("$u/U$")
#plt.ylabel("$\eta$")
#plt.show()

