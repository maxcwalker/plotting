import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile, plotoverx,contours,boundary,grid
import os

try:
    os.mkdir("./figures/")
except:
    print("A figures directory has already been found")

# read the file and extract varaibles
extract = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx =extract.variables("./restart_flow.csv")

# mesh
grid = grid()
grid.meshplolt(x,y)

#any plots over x
pltoverx = plotoverx()
pltoverx.varOverX(x,y,u,'Velocity')
pltoverx.varOverX(x,y,P,'Pressure')

#contour plots
conts = contours()
conts.varcontours(x,y,T,P,u,xg,yg)
conts.boundarycontours(x,y,T,P,u,xg,yg)

#boundary plots
bound = boundary()
bound.boundarymult(x,y,yg,xg,u)
bound.boundary(x,y,yg,xg,u)
bound.skinFrict(x,y,u,rho,mu)
bound.blasius(x,y,u,mu,xg,yg)
pltoverx.boundarythick(u,y,x,xg,yg)