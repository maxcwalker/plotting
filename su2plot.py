#This plotting script is for a standard compressible flow

import numpy as np
import matplotlib.pyplot as plt
import math


f = np.genfromtxt("../SU2/mach6_comp_lam_plate/restart_flow.csv", names=True, delimiter = ',')
x = np.around(f['x'], 5)
y = f['y']

n = 8 # number of decimals to round values to
rho = np.around(f['Density'], decimals=n)
rhou = np.around(f['Momentum_x'], decimals=n)
rhov = np.around(f['Momentum_y'], decimals=n)
E= np.around(f['Energy'], decimals=n)
P = np.around(f['Pressure'], decimals=n)
T = np.around(f['Temperature'], decimals=n)
ma = np.around(f['Mach'], decimals=n)
cp = np.around(f['Pressure_Coefficient'], decimals=n)
mu = np.around(f['Laminar_Viscosity'], decimals=n)

# velocity from the momentum
u = rhou/rho
v = rhov/rho
u_max = max(u)
max_i = str(int((np.where(x == max(x))[0][0])/65))
#first attempt
#print("I must not exceed "+max_i)
#i = input("Choose a value of i:")
#i = int(i)

i = 0
while x[i+1] == x[i]:
    print(i)
    if x[i+1] != x[i]:
        break
    i += 1

j = 0
if y[j] == 0:
    j += 1
print("the mesh is a {i} x {y} case")

print({i})


try:
    if i>1:
        i = (i-1)*65+2
    else:
        i = 1

    print(" x ="+str(x[i]))
    if x[i]<0:
        print("This position is before the plate")

    pos = (x[i])
    pos = round(pos, 3)
    pos = str(pos)

    new_var = y_pos= y[i:i+63]
    new_var
    #y_pos = np.flip(y_pos)
    u_x = u[i:i+63]
    u_x = u_x/u_max
    #u_x = np.flip(u_x)

    ax1 = plt.plot( u_x, y_pos)
    plt.xlabel("u/$U_{inf}$")
    plt.ylabel("normal position from the wall [m]")
    plt.title("Velocity profile at point "+pos+"m along plate")
    plt.xlim([0, 1])
    plt.ylim([0,0.01])
    plt.show()

except:
    print("A point has been chosen outside of the case domain")
    print("Please choose a smaller value of i")