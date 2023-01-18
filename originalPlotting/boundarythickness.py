import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile, plotoverx,contours,boundary,grid
import os

extract = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx =extract.variables("../../SU2/transitionalGrid/mach1_comp_lam_plate/restart_flow.csv")



newU = u.reshape(xg,yg).T
print(len(newU[:,119]))
print(newU[:,119])
newY = y.reshape([xg,yg]).T
print(np.shape(newY))
newX = x.reshape([xg,yg]).T
print(np.shape(newX))
x_boundary = newX[0, :]

# plt.contourf(newX,newY,newU, levels= 1000)
# plt.ylim([0, 0.01])
# plt.show()

y_boundary = []
print(xg)
print(yg)
for i in range(xg):
    for j in range(yg):
        if newU[j,i] <= 0.99*max(newU[:,i]) or j==(yg-1):
            y_boundary.append(newY[j,i])
            break

fig, ax1 = plt.subplots(1,1)
ax1.plot(x_boundary,y_boundary, color='green', marker = 'x')
ax1.set_aspect(5)
ax1.set_title('Boundary layer thickenss along the plate (99{} of $U_\infty$)'.format('%'))
ax1.set_xlabel('x [m]')
ax1.set_ylabel('$\delta$ [m]')
ax1.set_ylim(0)
ax1.set_xlim([min(x), max(x)])
ax1.set_aspect(1)
ax1.grid()
plt.show()