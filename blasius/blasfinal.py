import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile
from plots import plotoverx
from plots import contours
from plots import boundary
import os

extract = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx =extract.variables("./restart_flow.csv")


col_begin = []
for i in range(len(y)):
    if y[i] == min(y):
        col_begin.append(i)

pos = int(10)#(len(x)/yg)*0.9
xg = int(len(x) / yg)
i1 = col_begin[pos*yg]
i2 = col_begin[pos*yg]+yg

x, y_su2, u = x[i1:i2], y[i1:i2], u[i1:i2]
u_norm_su2 = u/u[0]

eta_su2 = y_su2* np.sqrt(u[yg-1]/(mu[yg-1]*x))



#####################################################################################
#####################################################################################

# -------------------------------------------------------------------------
#
# -1- Equation de Blasius f''' + f f'' = 0
#
#           dudt(t) = v(t)
#           dvdt(t) = w(t)
#           dwdt(t) = -u(t)*w(t) 
# 
#

def f(u):
    dudt =   u[1]
    dvdt =   u[2] 
    dwdt = - u[0] * u[2]  
    return np.array([dudt,dvdt,dwdt])
    
# -------------------------------------------------------------------------    
#
# -2- Schema de Runge-Kutta classique d'ordre 4
# 

def rungekutta(a,h):
    imax = int(5/h)
    X = np.arange(imax+1)*h
    U = np.zeros((imax+1,3)); U[0,:] = [0,0,a]
    for i in range(imax):  
        K1 = f(U[i,:]       )
        K2 = f(U[i,:]+K1*h/2)
        K3 = f(U[i,:]+K2*h/2)
        K4 = f(U[i,:]+K3*h  )
        U[i+1,:] = U[i,:] + h*(K1+2*K2+2*K3+K4)/6     
    return X,U

# -------------------------------------------------------------------------    
#
# -3- Methode de bissection 
# 

def shoot(a,h):
    X,U = rungekutta(a,h)
    return (1.0-U[-1,1])

def blasius(h,tol):
    n = 1; nmax = 40
    a = 0; fa = shoot(a,h)
    b = 1; fb = shoot(b,h)
    n = 0; delta = (b-a)/2
    if (fa*fb > 0) :
        raise RuntimeError('Bad initial interval') 
    while (abs(delta) >= tol and n <= nmax) :
        delta = (b-a)/2; n = n + 1;
        x = a + delta; fx = shoot(x,h)
        #print(" x = %14.7e (Estimated error %13.7e at iteration %d)" % (x,abs(delta),n))
        if (fx*fa > 0) :
            a = x;  fa = fx
        else :
            b = x;  fb = fx
    if (n > nmax):
        raise RuntimeError('Too much iterations') 
    return x
    
h   = 0.1
tol = 1e-7
a = blasius(h,tol)
X,U = rungekutta(a,h)

print(" ============ Final value for f''(0) = %.4f " % U[0,2])

#######################################################################################
#######################################################################################

fig, ax = plt.subplots(1,1)
ax.plot(U[:,1],X,'-r',label='blasius')
ax.plot(u_norm_su2, eta_su2, marker='.',color='purple', label = 'SU2')
ax.set_title('Velocity profile comparison for a Laminar Flat Plate')
ax.set_xlabel('$u/U_e$')
ax.set_ylabel('$\eta$')
ax.legend()
ax.set_ylim([0,10])
#ax.set_xlim([0,1])


plt.show()