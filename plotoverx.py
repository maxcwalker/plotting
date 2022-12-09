import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach2_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')
x = f['x']
y = f['y']
try:
    rho = f['Density']
except:
    rho1 = f['Density_0']
    rho2 = f['Density_1']
    rho3 = f['Density_2']
    rho4 = f['Density_3']
    rho5 = f['Density_4']
    rhon = [rho1,rho2,rho3,rho4,rho5]
    rho = sum(rhon)

rhou = f['Momentum_x']
rhov = f['Momentum_y']
E= f['Energy']
P = f['Pressure']
try:    
    T = f['Temperature']
except:
    T = np.around(f['Temperature_tr'], decimals=n)
ma = f['Mach']
cp = f['Pressure_Coefficient']
mu = f['Laminar_Viscosity']
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

### -----mesh----- ###
xg = len([y for y in y if y == 0])
yg = int(len(y)/xg)
print("The mesh is {}x{}".format(xg,yg))
### -------------- ###
plt.style.use('classic')

def varOverX(x,y,variable,varname):

    y_pos = 0.01  # choose what point above the wall
    y = np.around(y, 3)
    x_pos = []
    variable1 = []

    for i in range(len(y)):
        if y[i] == y_pos:
            x_pos.append(x[i])
            variable1.append(variable[i])

    fig,ax = plt.subplots(1,1)
    fig.set_size_inches(20,5)
    ax.plot(x_pos,variable1, label = 'y position {}m'.format(y_pos))
    ax.set_xlabel('X position [m]')

    if varname == 'Pressure':
        units = 'Pa'
    else:
        units = 'ms$^{-1}$'
    
    ax.set_ylabel('{} [{}]'.format(varname, units))
    ax.set_xlabel('x [m]')
    ax.set_title('Plot of {} over domain at y = {}m'.format(varname,str(y_pos)))
    ax.legend()
    ax.grid()
    ax.set_xlim([-0.05, 0.3])
    plt.savefig('plot{}over.pdf'.format(varname))

def boundarythick(u,y,x,xg,yg):
    newU = u.reshape(xg,yg)
    newY = y.reshape(xg,yg).T
    newX = x.reshape(xg,yg).T
    x_boundary = newX[0, :]
    #max_u = np.max(u)
    #print(max_u)

    y_boundary = []
    for i in range(xg):
        for j in range(yg):
            if newU[j,i] <= 0.99*686 or j==64:
                y_boundary.append(newY[j,i])
                break

    fig, ax1 = plt.subplots(1,1)
    ax1.plot(x_boundary,y_boundary, color='green', marker = 'x')
    ax1.set_aspect(5)
    #ax1.set_autoscale_on
    ax1.set_title('Boundary layer thickenss along the plate (99{} of $U_\infty$)'.format('%'))
    ax1.set_xlabel('x [m]')
    ax1.set_ylabel('$\delta$ [m]')
    ax1.set_ylim(0)
    ax1.set_xlim([min(x), 0.3])
    ax1.grid()

   

varOverX(x,y,u,'Velocity')
#varOverX(x,y,P,'Pressure')
boundarythick(u,y,x,xg,yg)
plt.show()