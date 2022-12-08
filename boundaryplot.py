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
mu = np.around(f['Laminar_Viscosity'], decimals=n)
# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)

#calculating the mesh 
yg = len([x for x in x if x ==0])
xg = len(x)/yg 

plt.style.use('classic')

def boundarymult(x,yg,xg,u):
    f5 = 0.05
    f4 = 0.07
    f3 = 0.08
    f2 = 0.1
    f1 = 0.11
    #5th plot
    i5 = len(x) - yg*int(xg*f5)
    print('-----------------------------')
    print(i5)
    print(yg*int((xg*0.04)))
    print(len(x))
    pos5 = int((100*(x[i5]/max(x))))
    y_pos= y[i5:i5+yg]
    u_x = u[i5:i5+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i5 in range(len(u_x)):
        if u_x[i5] <= 0.99*u_max:
            u_x2.append(u_x[i5])
            y_pos2.append(y_pos[i5])
    ub5_nondim = u_x2/max(u_x2)
    yb5_nondim = y_pos2/max(y_pos2)

    #############################################################################
    #4th plot
    i4 = len(x) - yg*int(xg*f4)
    print('-----------------------------')
    print(i4)
    print(yg*int((xg*0.05)))
    print(len(x))

    pos4 = int((100*(x[i4]/max(x))))
    y_pos= y[i4:i4+yg]
    u_x = u[i4:i4+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i4 in range(len(u_x)):
        if u_x[i4] <= 0.99*u_max:
            u_x2.append(u_x[i4])
            y_pos2.append(y_pos[i4])
    ub4_nondim = u_x2/max(u_x2)
    yb4_nondim = y_pos2/max(y_pos2)

    ###################################################################
    #3th plot
    i3 = len(x) - yg*int(xg*f3)
    print('-----------------------------')
    print(i3)
    print(yg*int((xg*0.06)))
    print(len(x))
    pos3 = int((100*(x[i3]/max(x))))

    y_pos= y[i3:i3+yg]
    u_x = u[i3:i3+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i3 in range(len(u_x)):
        if u_x[i3] <= 0.99*u_max:
            u_x2.append(u_x[i3])
            y_pos2.append(y_pos[i3])
    ub3_nondim = u_x2/max(u_x2)
    yb3_nondim = y_pos2/max(y_pos2)

    ###############################################################
    #2nd plot
    i2 = len(x) - yg*int(xg*f2)
    print('-----------------------------')
    print(i2)
    print(yg*int((xg*0.07)))
    print(len(x))
    pos2 = int((100*(x[i2]/max(x))))

    y_pos= y[i2:i2+yg]
    u_x = u[i2:i2+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i2 in range(len(u_x)):
        if u_x[i2] <= 0.99*u_max:
            u_x2.append(u_x[i2])
            y_pos2.append(y_pos[i2])
    ub2_nondim = u_x2/max(u_x2)
    yb2_nondim = y_pos2/max(y_pos2)

    ####################################################################
    #1st plot

    i1 = len(x) - yg*int(xg*f1)
    print('-----------------------------')
    print(i1)
    print(yg*int((xg*0.08)))
    print(len(x))
    pos1 = int((100*(x[i1]/max(x))))
    y_pos= y[i1:i1+yg]
    u_x = u[i1:i1+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i1 in range(len(u_x)):
        if u_x[i1] <= 0.99*u_max:
            u_x2.append(u_x[i1])
            y_pos2.append(y_pos[i1])
    ub1_nondim = u_x2/max(u_x2)
    yb1_nondim = y_pos2/max(y_pos2)

    ######################################################################
    ######################################################################


    #plotting the velocity profile [non dimensional]
    fig, ax1 = plt.subplots(1,1)
    ax1.plot( ub5_nondim, yb5_nondim, marker='x', color = 'green', label = '{}{} along plate'.format(pos5,"%"))
    ax1.plot( ub4_nondim, yb4_nondim, marker='x', color = 'orange', label = '{}{}along plate'.format(pos4,"%"))
    ax1.plot( ub3_nondim, yb3_nondim, marker='x', color = 'purple', label = '{}{} along plate'.format(pos3,"%"))
    ax1.plot( ub2_nondim, yb2_nondim, marker='x', color = 'black', label = '{}{} along plate'.format(pos2,"%"))
    ax1.plot( ub1_nondim, yb1_nondim, marker='x', color = 'blue', label = '{}{} along plate'.format(pos1,"%"))
    ax1.legend()

    ax1.set_xlabel("u/$U_\infty$")
    ax1.set_ylabel("$y/\delta$")
    ax1.set_title("Laminar Boundary layer at several points along the plate")
    ax1.grid()

def boundary(x,yg,xg,u):
    i = len(x) - yg*int((xg*0.04))

    pos = (x[i])
    pos = str(round(pos, 3))
    y_pos= y[i:i+yg]
    u_x = u[i:i+yg]
    u_max = max(u_x)

    #u_x = [x for x in u_x if x <= 0.99*u_max]
    u_x2 =[]
    y_pos2 =[]
    for i in range(len(u_x)):
        if u_x[i] <= 0.99*u_max:
            u_x2.append(u_x[i])
            y_pos2.append(y_pos[i])
    ub_nondim = u_x2/max(u_x2)
    yb_nondim = y_pos2/max(y_pos2)

    fig, ax2 = plt.subplots(1,1)
    ax2.plot(ub_nondim,yb_nondim, color = 'green', marker='x')
    ax2.set_title("Laminar boundary layer at {}m along plate for a {}x{} mesh \n the boundary layer contains {} points".format(pos,int(xg),yg,len(yb_nondim)))
    ax2.set_xlabel("$u/U_\infty$")
    ax2.set_ylabel("$y/\delta$")
    ax2.grid()

#boundary(x,yg,xg,u)
boundarymult(x,yg,xg,u)

plt.show()