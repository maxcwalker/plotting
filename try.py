import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach2_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')

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
#mu = np.around(f['Laminar_Viscosity'], decimals=n)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

yg = int(len([x for x in x if x==0 ]))
xg = int(len(x)/yg)

plt.style.use('classic')
fig, ax = plt.subplots(1,1)
ax.scatter(x,y, marker ='.')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_title('scatter grap of {}x{} grid'.format(xg,yg))
#ax.set_ylim([0.004, 0.006])
ax.grid()
#ax.set_aspect(1)

plt.show()