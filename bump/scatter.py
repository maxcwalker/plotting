import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("/home/maxwalker/git/SU2/bump_meshes/inv_bump_mach1_256x128/restart_flow.csv", names=True, delimiter = ',')

n = 3 # number of decimals to round values to
x = np.around(f['x'],n )
y = np.around(f['y'], n)
rho = np.around(f['Density'], decimals=n)
rhou = np.around(f['Momentum_x'], decimals=n)
rhov = np.around(f['Momentum_y'], decimals=n)
E= np.around(f['Energy'], decimals=n)
P = np.around(f['Pressure'], decimals=n) 
T = np.around(f['Temperature'], decimals=n)
ma = np.around(f['Mach'], decimals=n)
cp = np.around(f['Pressure_Coefficient'], decimals=n)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

ax = plt.scatter(x,y, color = 'blue', s=0.2)
#plt.figure(facecolor='yellow')
plt.title("The grid points at the top of the bump")
plt.xlabel("x")
plt.ylabel("y")
ax.set_facecolor("blue")
#plt.ylim([0.08,0.2])
#plt.xlim([1.4,1.6])
plt.show()