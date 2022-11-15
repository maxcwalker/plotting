import numpy as np
import matplotlib.pyplot as plt


f = np.genfromtxt("./restart_flow.csv", names=True, delimiter = ',')
x = f['x']
y = f['y']
rho = f['Density']
rhou = f['Momentum_x']
rhov = f['Momentum_y']
E= f['Energy']
P = f['Pressure']
T = f['Temperature']
ma = f['Mach']
cp = f['Pressure_Coefficient']
mu = f['Laminar_Viscosity']

u = rhou/rho
v = rhov/rho
u_max = max(u)
max_i = str(int((np.where(x == max(x))[0][0])/65))
print("I must not exceed "+max_i)
i = input("Choose a value of i:")
i = int(i)

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