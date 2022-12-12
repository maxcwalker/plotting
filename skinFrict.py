#This plotting script is for a standard compressible flow

import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile

extr = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx = extr.variables("../SU2/mach2_comp_lam_plate/restart_flow.csv")

y_wall = []
u_wall = []
x_wall = []

for i in range(len(y)):
    if y[i] ==  0:
        y_wall.append(y[i-1])
        u_wall.append(u[i-1])
        x_wall.append(x[i-1])

dudy = np.array(u_wall) / np.array(y_wall)
t_wall = mu[0]*dudy
Cf = t_wall/(0.5*rho[0]*u[0])
x_wall = np.array(x_wall)/0.3
fig, ax = plt.subplots(1,1)
plt.style.use('classic')
ax.plot(x_wall,Cf)
ax.set_xlim([0,1])
ax.set_xlabel('$x/L$')
ax.set_ylabel('$C_f$')
ax.set_title('Coefficient of Friction')
ax.grid()
plt.savefig("skinFrictGraph.pdf")
plt.show()