#This plotting script is for a standard compressible flow

import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile

###--------------------------###
exvar = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx = exvar.variables("../SU2/mach2_comp_lam_plate/restart_flow.csv")
### -------------- ###

col_begin = []

for i in range(len(y)):
    if y[i] == max(y):
        col_begin.append(i)

i1 = col_begin[63]
i2 = col_begin[63]+yg

x, y, u = x[i1:i2], y[i1:i2], u[i1:i2]
u_norm = u/u[0]

eta = y* np.sqrt(u[0]/(mu[0]*x))

fig, ax = plt.subplots(1,1)
ax.plot(u_norm, eta, marker='.',color='purple')
ax.set_title('Velocity profile comparison for a Laminar Flat Plate')
ax.set_xlabel('$u/U_e$')
ax.set_ylabel('$\eta$')
ax.set_ylim([0,10])

plt.show()









