'''
Q2 i)

spatial steps j=1 to j=N
time steps from t=1 to t=T

boundary conditions J=1 and j=N

initial condistions for Qj

for time steps t=1 to t=T
    for j=1 to j=N
        f(q) = (rho * u, rho * u^2 + p, rho * u H)^T

        if u<-a then
            f- = f(q), f+ = f(q)
        
        elif u>a then
            f-=0, f+=f(q)
        
        else


Q2 ii)
'''

import numpy as np
import pylab as py
import time
import math as m
import matplotlib.pyplot as plt
import tabulate
#latex
import matplotlib as mpl
import matplotlib.animation as animation
import tabulate


print("Start CPU time = {} s".format(time.time()))

# Define all arrays
Nx = 102
U = np.zeros((Nx,3))
F, Ftil, Fp, Fn = np.zeros((Nx,3)), np.zeros((Nx,3)), np.zeros((Nx,3)), np.zeros((Nx,3))
Fint = np.zeros(3)
x, p, V, a, H = np.zeros(Nx), np.zeros(Nx), np.zeros(Nx), np.zeros(Nx), np.zeros(Nx)

# Duct geometry
Lx=15.0
dx=Lx/(Nx-2)

# Set no. of steps, time step - adjust dt to satisfy CFL condition when
# increasing Nx
dt = 0.0001
nstep = int(0.01/dt) # i.e. run to time t=0.01s

# For output
noutput = 5  # Output each noutput step
nanim = int(nstep/noutput)
rhoa, Va, pa = np.zeros((nanim+2,Nx)), np.zeros((nanim+2,Nx)), np.zeros((nanim+2,Nx))
ni = 0

# Initial condition
gamma = 1.4
R = 287.
Vi = 240
for i in range(0, Nx):
    x[i] = -dx/2. + i*dx
    if i<Nx/3:
        rhoi = 1.1
        pi = 110.e3
    else:
        rhoi = 0.25
        pi = 25.e3

    U[i][0] = rhoi
    U[i][1] = U[i][0]*Vi
    U[i][2] = U[i][0]*(pi/(rhoi*(gamma - 1.0)) + 0.5*Vi**2)

    # Save data for animation output
    rhoa[ni][i] = rhoi
    Va[ni][i] = Vi
    pa[ni][i] = pi

# Main loop
for n in range(1,nstep):

    for i in range(0, Nx):
        p[i] = (gamma-1.0)*(U[i][2]-0.5*U[i][1]**2./U[i][0])
        V[i] = U[i][1]/U[i][0]
        a[i] = m.sqrt(gamma*p[i]/U[i][0])
        H[i] = (U[i][2]+p[i])/U[i][0]
        F[i][0] = U[i][1]
        F[i][1] = U[i][1]**2./U[i][0] + p[i]
        F[i][2] = H[i]*U[i][1]          
    
        if V[i] < -a[i]: 
           Fp[i] = 0.
           Fn[i] = F[i]
        elif V[i] > a[i]:
           Fp[i] = F[i]
           Fn[i] = 0.
        else:
            Fp[i][0] = 1.0
            Fp[i][1] = ((gamma-1.0)*V[i] + 2*a[i]) / gamma
            Fp[i][2] = ((gamma-1.0)*V[i] + 2*a[i])**2 / (2*(gamma**2 -1))
            Fp[i] *= U[i][0] / (4*a[i]) * (V[i]+a[i])**2

            Fn[i][0] = 1.0
            Fn[i][1] = ((gamma-1.0)*V[i] + 2*a[i]) / gamma
            Fn[i][2] = ((gamma-1.0)*V[i] + 2*a[i])**2 / (2*(gamma**2 -1))
            Fn[i] *= U[i][0] / (4*a[i]) * (V[i]+a[i])**2

    for i in range(0,Nx-1):
        Ftil[i] = Fp[i] + Fn[i+1]
        
    for i in range(1, Nx-1):
        U[i] = U[i] + (-(Ftil[i] - Ftil[i-1])/dx)*dt 

    # Left and right boundary condition: extrapolation 
    U[0] = 2*U[1] - U[2]
    U[Nx-1] = 2*U[Nx-2] - U[Nx-3]

    # Estimate CFL number
    emax = np.zeros(Nx)
    if (n%noutput==0) | (n==1):
        # emax = max(abs(V)+a)
        for i in range(Nx):
            if abs(V[i]) < a[i]:
                operator = (gamma + 3) / (2*gamma + abs(V[i])*(3-gamma)/a[i])
            else:
                operator = 1
            emax[i] = (abs(V[i])+a[i]) * operator           
        emax = max(emax)

        print("Step %6d, time=%12.8f, CFL=%8.6f" % (n,n*dt,emax*dt/dx))
    
    # Save data for animation output
    if (n%noutput==0) | (n==nstep):
        ni += 1
        for i in range(0, Nx):
            rhoa[ni][i] = U[i][0]
            Va[ni][i] = U[i][1]/U[i][0]
            pa[ni][i] = (gamma - 1.0) * (U[i][2] - 0.5 * Va[ni][i]*Va[ni][i]*U[i][0])

# Table output
Ta, Ma = np.zeros(Nx), np.zeros(Nx)
for i in range(0, Nx):
    Ta[i] = pa[ni][i]/rhoa[ni][i]/R;
    Ma[i] = Va[ni][i]/m.sqrt(gamma*R*Ta[i])

# Two Rieman problems
# print(tabulate(['rho [kg/m3]', U[0][0], U[-1][0]], \
#     ['u [m/s]', V[0], V[-1]], \
#         ['p [kpa]',p[0]/1e3, p[-1]/1e3], headers = ['', 'left', 'right']))
print("end CPU time = {} s".format(time.clock()))

# Graphic output
plt.figure(1)
plt.subplot(211)
plt.ylabel('rho')
plt.xlabel('x')
plt.plot(x, rhoa[ni])
plt.xlim(0,Lx)

plt.subplot(212)
plt.xlabel('x')
plt.ylabel('V')
plt.plot(x, Va[ni])
plt.xlim(0,Lx)

plt.figure(2)
plt.subplot(311)
plt.ylabel('T')
plt.xlabel('x')
plt.plot(x, Ta)
plt.xlim(0,Lx)

plt.subplot(312)
plt.ylabel('p')
plt.xlabel('x')
plt.plot(x, pa[ni])
plt.xlim(0,Lx)

plt.subplot(313)
plt.xlabel('x')
plt.ylabel('M')
plt.plot(x, Ma)
plt.xlim(0,Lx)

figanim, (axrho, axp) = plt.subplots(2, 1)
axrho.set_ylabel('rho')
plt.xlabel('x')
axrho.set_xlim(0,Lx)
axp.set_ylabel('p')
axp.set_xlim(0,Lx)
linerho, = axrho.plot(x, rhoa[0])
linep, = axp.plot(x, pa[0])
def animate(i):
    linerho.set_ydata(rhoa[i])  # update the data
    linep.set_ydata(pa[i])  # update the data
    return linerho, linep,
ani = animation.FuncAnimation(figanim, animate, np.arange(0, nanim), interval=100)

plt.show()


