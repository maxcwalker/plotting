import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from plots import readfile
from plots import plotoverx
from plots import contours
from plots import boundary
import os

plt.style.use('classic')

try:
    os.mkdir("./figures/")
except:
    print("A plots directory is already created")

# read the file and extract varaibles
extract = readfile()
x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx =extract.variables("./restart_flow.csv")

bound = boundary()
bound.blasius(x,y,u,mu,yg)