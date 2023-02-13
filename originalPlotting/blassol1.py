import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
import scipy.optimize as optimize
from plots import readfile

##########SU2 data#########################
exvar = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx = exvar.variables("./restart_flow.csv")
u_inf = u[0]
col_begin = []

for i in range(len(y)):
    if y[i] == max(y):
        col_begin.append(i)

pos = int((len(x)/yg)*0.95)
i1 = col_begin[pos]
i2 = col_begin[pos]+yg
x, y_su2, u = x[i1:i2], y[i1:i2], u[i1:i2]
u_norm_su2 = u/u[0]

eta_su2 = y_su2* np.sqrt(u_inf/(mu[0]*x))

#####################################################################################
#####################################################################################

# 2f''' + ff'' = 0
# f(0) = 0, f'(0) = 0, f'(inf) = 1
# introducing variables g and h for the shooting method
# g = f' and h = f''
# so g' = f'' = h
# h' = f'' = -(f''f)/2 = -(hf) / 2

def blasEq(eta,y):
    f, g, h = y
    return g, h, -h*f/2

# we now need to integrate this ode and we know the initial values of g and f but
# not that of h. So we need to guess an initial value for h
# after we can then check the value of g at infinity and see how close it is to the
# expected value of 1.

def findh0(h0):
    f0, g0 = 0, 0
    y0 = np.asarray([f0,g0,h0],dtype=object)
    res = integrate.RK45(blasEq, 0, y0, 100)
    for i in range(100):
        res.step()

    # we subtract 0 to the output so that it returns 0 when the correct value 
    # for h0 is used
    return 1 - res.y[1]

for i in range(1, 10):
    print(i/10, findh0(i/10))

#as we see the sign change from 0.3 to 0.4, the initial guess value will be 0.3
def blasius():
    h0 = optimize.fsolve(findh0, 0.3)

    N= 50
    f0, g0 = 0, 0
    f = np.zeros(N)
    eta = np.zeros(N)

    y0 = np.asarray([f0,g0,h0],dtype=object)
    res = integrate.RK45(blasEq, 0, y0, 100)
    for i in range(N):
        res.step()
        f[i] = res.y[1]
        eta[i] = res.t
    return f, eta

f, eta = blasius()
fif, ax = plt.subplots(1,1)
ax.plot(f,eta, color = 'blue', label = 'Blasius Solution')
ax. plot(u_norm_su2, eta_su2, color = 'green', label = 'SU2')
ax.set_ylim([0,8])
ax.set_xlim([0,1])
ax.set_title('Velocity profile comparison for a Laminar Flat Plate')
ax.set_xlabel('$u/U_e$')
ax.set_ylabel('$\eta$')
ax.legend()
plt.show()
