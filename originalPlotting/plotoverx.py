import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module
from readfile import readfile

###--------------------------###
#exvar = readfile()
#x,y,E,P,T,cp,mu,u,v,xg,yg = exvar.variables("../SU2/mach2_comp_lam_plate/restart_flow.csv")
### -------------- ###

plt.style.use('classic')
class plotoverx:
    def __init__(self):
        return
    def varOverX(self,x,y,variable,varname):
        self.x = x
        self.y = y
        self.variable = variable
        self.varname = varname

        y_pos = 0.01  # choose what point above the wall
        y = np.around(y, 3)
        x_pos = []
        variable1 = []

        for i in range(len(y)):
            if y[i] == y_pos:
                x_pos.append(x[i])
                variable1.append(variable[i])

        fig,ax = plt.subplots(1,1)
        fig.set_size_inches(20,5)
        ax.plot(x_pos,variable1, label = 'y position {}m'.format(y_pos))
        ax.set_xlabel('X position [m]')

        if varname == 'Pressure':
            units = 'Pa'
        else:
            units = 'ms$^{-1}$'
        
        ax.set_ylabel('{} [{}]'.format(varname, units))
        ax.set_xlabel('x [m]')
        ax.set_title('Plot of {} over domain at y = {}m'.format(varname,str(y_pos)))
        ax.legend()
        ax.grid()
        ax.set_xlim([-0.05, 0.3])
        plt.savefig('plots/plot{}over.pdf'.format(varname))

    def boundarythick(self,u,y,x,xg,yg):
        self.u = u
        self.y = y
        self.x = x
        self.xg = xg
        self.yg = yg

        newU = u.reshape(xg,yg)
        newY = y.reshape(xg,yg).T
        newX = x.reshape(xg,yg).T
        x_boundary = newX[0, :]
        #max_u = np.max(u)
        #print(max_u)

        y_boundary = []
        for i in range(xg):
            for j in range(yg):
                if newU[j,i] <= 0.99*686 or j==64:
                    y_boundary.append(newY[j,i])
                    break

        fig, ax1 = plt.subplots(1,1)
        ax1.plot(x_boundary,y_boundary, color='green', marker = 'x')
        ax1.set_aspect(5)
        #ax1.set_autoscale_on
        ax1.set_title('Boundary layer thickenss along the plate (99{} of $U_\infty$)'.format('%'))
        ax1.set_xlabel('x [m]')
        ax1.set_ylabel('$\delta$ [m]')
        ax1.set_ylim(0)
        ax1.set_xlim([min(x), 0.3])
        ax1.grid()
        plt.savefig("plots/boundarythickness.pdf")


#pltoverx = plotoverx()
#pltoverx.varOverX(x,y,u,'Velocity')
#varOverX(x,y,P,'Pressure')
#boundarythick(u,y,x,xg,yg)
#plt.show()