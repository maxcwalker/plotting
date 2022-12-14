from matplotlib import pyplot as plt
import matplotlib
import matplotlib.cm as cm # latex module
import numpy as np
import math
from plots import readfile

##########SU2 data#########################
exvar = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx = exvar.variables("../SU2/mach2_comp_lam_plateNemo/restart_flow.csv")
u_inf = u[0]
col_begin = []

for i in range(len(y)):
    if y[i] == max(y):
        col_begin.append(i)

pos = 60
i1 = col_begin[pos]
i2 = col_begin[pos]+yg
x, y_su2, u = x[i1:i2], y[i1:i2], u[i1:i2]
u_norm_su2 = u/u[0]

eta_su2 = y_su2* np.sqrt(u_inf/(mu[0]*x))

#####################################################################################
#####################################################################################
#
# -------------------------------------------------------------------------
#
# -1- Equation de Blasius f''' + f f'' = 0
#
#           dudt(t) = v(t)
#           dvdt(t) = w(t)
#           dwdt(t) = -u(t)*w(t) 
#
 
def f(u):
  dudt =   u[1]
  dvdt =   u[2] 
  dwdt = - u[0] * u[2]  
  return np.array([dudt,dvdt,dwdt])
 
# -------------------------------------------------------------------------    
# 4th Order Runge-Kutta numerical ODE solving method

def rungekutta(a,h):
  imax = int(10/h)
  # using np.arrange(val) sets linspace of integers from 0 to that value
  X = np.arange(imax+1)*h # This gets 0 and the last by adding 1
  U = np.zeros((imax+1,3)) # 1000 x 3 matrix
  U[0,:] = [0,0,a]
  for i in range(imax):  
    K1 = f(U[i,:])
    K2 = f(U[i,:]+K1*h/2)
    K3 = f(U[i,:]+K2*h/2)
    K4 = f(U[i,:]+K3*h  )
    U[i+1,:] = U[i,:] + h*(K1+2*K2+2*K3+K4)/6     
  return X,U

# -------------------------------------------------------------------------    
#
# -3- Bissection Method? Not too sure

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
    print(" x = %14.7e (Estimated error %13.7e at iteration %d)" % (x,abs(delta),n))
    if (fx*fa > 0) :
      a = x;  fa = fx
    else :
      b = x;  fb = fx
  if (n > nmax) :
    raise RuntimeError('Too many iterations') 
  return x

h   = 0.1 # This is the steps
tol = 1e-10
a = blasius(h,tol)
X,U = rungekutta(a,h)




# print(" ============ Final value for f''(0) = %.4f " % U[0,2])

# ####################################################################################
# ####################################################################################

# plt.xlabel('$\eta$')
# plt.ylabel('$f(\eta)$')

# #plt.plot(X,U[:,1]*X - U[:,0],'-b',X,U[:,1],'-r')
# plt.plot(U[:,1],X*2,'-r',label='blasius') # U[:,1]*X - U[:,0],X,'-b'
# plt.plot(u_norm_su2, eta_su2, marker='.',color='purple', label = 'SU2')
# plt.title('Velocity profile comparison for a Laminar Flat Plate')
# plt.xlabel('$u/U_e$')
# plt.ylabel('$\eta$')
# plt.legend()
# plt.ylim([0,10])

# plt.show()