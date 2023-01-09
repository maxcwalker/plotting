import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate


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
    f0, g0 = 0,0
    res = integrate.RK45(blasEq, 0, (f0, g0, h0), 100)
    for i in range(100):
        res.step()

    # we subtract 0 to the output so that it returns 0 when the correct value 
    # for h0 is used
    return 1 - res.y[1]

for i in range(1, 10):
    print(i/10, findh0(i/10))
