import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module

f = np.genfromtxt("../SU2/mach6_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')
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


####################################################################
####################################################################
#5th plot
i = len(x) - yg*int((xg*0.05))
pos5 = int((100*(x[i]/max(x))))
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
ub5_nondim = u_x2/max(u_x2)
yb5_nondim = y_pos2/max(y_pos2)

#############################################################################
#4th plot
i = len(x) - int(yg*(xg*0.1))
print(i)

pos4 = int((100*(x[i]/max(x))))
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
ub4_nondim = u_x2/max(u_x2)
yb4_nondim = y_pos2/max(y_pos2)

###################################################################
#3th plot
i = len(x) - yg*int((xg*0.15))
print(i)
pos3 = int((100*(x[i]/max(x))))

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
ub3_nondim = u_x2/max(u_x2)
yb3_nondim = y_pos2/max(y_pos2)

###############################################################
#2nd plot
print(i)
i = len(x) - yg*int((xg*0.20))

pos2 = int((100*(x[i]/max(x))))
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
ub2_nondim = u_x2/max(u_x2)
yb2_nondim = y_pos2/max(y_pos2)

####################################################################
#1st plot

i = len(x) - yg*int((xg*0.25))
print(i)
pos1 = int((100*(x[i]/max(x))))
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
ub1_nondim = u_x2/max(u_x2)
yb1_nondim = y_pos2/max(y_pos2)

######################################################################
######################################################################


#plotting the velocity profile [non dimensional]
plt.plot( ub5_nondim, yb5_nondim, color = 'green', label = '{}{} along plate'.format(pos5,"%"))
plt.plot( ub4_nondim, yb4_nondim, color = 'orange', label = '{}{}along plate'.format(pos4,"%"))
plt.plot( ub3_nondim, yb3_nondim, color = 'purple', label = '{}{} along plate'.format(pos3,"%"))
plt.plot( ub2_nondim, yb2_nondim, color = 'black', label = '{}{} along plate'.format(pos2,"%"))
plt.plot( ub1_nondim, yb1_nondim, color = 'blue', label = '{}{} along plate'.format(pos1,"%"))
plt.legend()

plt.xlabel("u/$U_\infty$")
plt.ylabel("$y/\delta$")
plt.title("Laminar Boundary layer at several points along the plate")
print("---------------------------------------")
print(len(u_x))
print("---------------------------------------")
plt.show()