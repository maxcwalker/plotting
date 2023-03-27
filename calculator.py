import numpy as np
from matplotlib import pyplot as plt
from sympy import sin, pi, sqrt

y = 1.4
Ma = 10

# Q1i

#stagnation pressure calculation
print(" ")
print("Question 1(i)")
Cpmax = (2/(y*Ma**2)) * (((1-y+(2*y)*(Ma**2))/(y+1)) * ((((y+1)**2)*(Ma**2)) / (4*y*(Ma**2)-2*(y-1)))**3.5-1)
print("Pressure coefficient at the stagnation point is %.5f" %  Cpmax)

# Modified Newtonian theory, the pressure coeff at a point is
# Cp = Cpmax * sin^theta

theta = 15*pi/180
Cp = Cpmax * (sin(theta))**2
print("Cp = %.3f at a point with %.0f degrees inclination" % (Cp,theta)) 
print(" ")

#1ii

print("Question 1(ii)")
M1 = 15
M2 = 6.19
th1 = 5
th1 = th1*pi/180
L = 0.35
th2 = 3 
th2 = th2*pi/180
th2r = 2 # From horizontal 5 - 3
l1 = 0.15
l2 = 0.2
H = 10e3
P1 = 26.5e3

#For the first segment of the plate
#Newtonian theory
print("For the first segment of the plate")
Cpi = 2 * (sin(th1))**2
print("Using the Newtonian theory, Cp is %.4f" % Cpi)
# The tangent wedge method
Cpi = (2*(th1**2))*(((y+1)/4) + sqrt((((y+1)/4)**2) + (1/((M1*th1)**2)))) 
print("Using the Tangent-wedge method, Cp is %.4f" % Cpi)
P2 = P1 * ((1+(2.4 / 2)*M1**2) / (1+(2.4 / 2)*M2**2))**(1.4/0.4)
Cpi = (2 / (y * M1**2)) * (P2 /P1 -1)
print("Using the shock expansion method, Cp is %.4f" % Cpi)

print('----------------------------------------------------')

print("For the second segment of the plate")
Cpi2 = 2 * (sin(th2))**2
print("Using the Newtonian theory, Cp is %.4f" % Cpi2)
# The tangent wedge method
Cpi = (2*(th2**2))*(((y+1)/4) + sqrt((((y+1)/4)**2) + (1/((M2*th2)**2)))) 
print("Using the Tangent-wedge method, Cp is %.4f" % Cpi)

P3 = P2 * ((1+(2.4 / 2)*M2**2) / (1+(2.4 / 2)*M3**2))
Cpi = (2 / (y * M1**2)) * (P2 /P1 -1)
print("Using the shock expansion method, Cp is %.4f" % Cpi)



print(" ")
