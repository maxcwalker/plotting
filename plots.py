import numpy as np
from matplotlib import pyplot as plt
import math 
import matplotlib.cm as cm # latex module



class readfile:
    plt.style.use('classic')
    def __init__(self):
        return
 
    def variables(self,fname):
        self.fname = fname
        
        f = np.genfromtxt(fname, names=True, delimiter = ',')
        x = f['x']
        y = f['y']
        try:
            rho = f['Density']
        except:
            rho1 = f['Density_0']
            rho2 = f['Density_1']
            rho3 = f['Density_2']
            rho4 = f['Density_3']
            rho5 = f['Density_4']
            rhon = [rho1,rho2,rho3,rho4,rho5]
            rho = sum(rhon)

        rhou = f['Momentum_x']
        rhov = f['Momentum_y']
        E= f['Energy']
        P = f['Pressure']
        try:    
            T = f['Temperature']
        except:
            T = np.around(f['Temperature_tr'], decimals=n)
        ma = f['Mach']
        cp = f['Pressure_Coefficient']
        mu = f['Laminar_Viscosity']
        Csfx = f['Skin_Friction_Coefficient_x']
        # velocity from the momentum
        u = rhou/rho
        v = rhov/rho
        ### -----mesh----- ###
        xg = len([y for y in y if y == 0])
        yg = int(len(y)/xg)
        print("---------------------------------------------")
        print("The mesh is {}x{}".format(xg,yg))
        print("---------------------------------------------")

        return x,y,rho,E,P,T,cp,mu,u,v,xg,yg,Csfx

class plotoverx:
    def __init__(self):
        print("initialise")
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

class contours:
    def __init__(self):
        return

    def varcontours(self,x,y,T,P,u,xg,yg):
        self.x = x
        self.y = y
        self.T = T
        self.P = P
        self.u = u
        self.xg = xg
        self.yg = yg

        newx = x.reshape((xg,int(len(x)/xg)))
        newy = y.reshape(xg,int(len(x)/xg))
        newT = T.reshape(xg,int(len(x)/xg))
        newP = P.reshape(xg,int(len(x)/xg))
        newU = u.reshape(xg,int(len(x)/xg))

        levelsT = np.linspace(min(T),max(T),1000)
        levelsP = np.linspace(min(P),max(P),1000)
        levelsU = np.linspace(0,max(u),1000)

        fig, (ax1,ax2, ax3) = plt.subplots(3,1)
        fig.set_size_inches(18.5, 10.5)
        T = ax1.contourf( newx, newy, newT, levels = levelsT, cmap=cm.jet ) 
        ax1.set_title("Temperature Contours for a {}x{} grid".format(xg, yg))
        ax1.set_ylabel("y")
        tbar = plt.colorbar(T, ax=ax1)
        tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

        P = ax2.contourf(newx, newy, newP, levels = levelsP)
        ax2.set_title("Pressure Contours for a {}x{} grid".format(xg, yg))
        ax2.set_ylabel("y")
        Pbar = plt.colorbar(P, ax=ax2)
        Pbar.set_label("Pressure [Pa]" ) #rotation= 270
        plt.legend

        U = ax3.contourf(newx, newy, newU, levels = levelsU)
        ax3.set_title("X_Velocity Contours for a {}x{} grid".format(xg, yg))
        ax3.set_xlabel("x")
        ax3.set_ylabel("y")
        ubar = plt.colorbar(U, ax=ax3)
        ubar.set_label("X_Velocity [ms$^{-1}$]" ) #rotation= 270
        plt.legend

        ax1.set_aspect(1)
        ax2.set_aspect(1)
        ax3.set_aspect(1)
        plt.savefig("plots/contours.pdf")

    def boundarycontours(self, x,y,T,P,u,xg,yg):
        self.x = x
        self.y = y
        self.T = T
        self.P = P
        self.u = u
        self.xg = xg
        self.yg = yg

        newx = x.reshape((xg,int(len(x)/xg)))
        newy = y.reshape(xg,int(len(x)/xg))
        newT = T.reshape(xg,int(len(x)/xg))
        newP = P.reshape(xg,int(len(x)/xg))
        newU = u.reshape(xg,int(len(x)/xg))

        levelsT = np.linspace(200,550,1000)
        levelsP = np.linspace(95000,122000,1000)
        levelsU = np.linspace(0,800,1000)

        fig, (ax1,ax2, ax3) = plt.subplots(3,1)
        fig.set_size_inches(18.5, 10.5)
        T = ax1.contourf( newx, newy, newT, levels = levelsT, cmap=cm.jet ) 
        ax1.set_title("Temperature Contours for a {}x{} grid".format(xg, yg))
        ax1.set_ylabel("y")
        tbar = plt.colorbar(T, ax=ax1)
        tbar.set_label("Temperature [$^{\circ}$C]" ) #rotation= 270

        P = ax2.contourf(newx, newy, newP, levels = levelsP)
        ax2.set_title("Pressure Contours for a {}x{} grid".format(xg, yg))
        ax2.set_ylabel("y")
        Pbar = plt.colorbar(P, ax=ax2)
        Pbar.set_label("Pressure [Pa]" ) #rotation= 270
        plt.legend

        U = ax3.contourf(newx, newy, newU, levels = levelsU)
        ax3.set_title("X_Velocity Contours for a {}x{} grid".format(xg, yg))
        ax3.set_xlabel("x")
        ax3.set_ylabel("y")
        ubar = plt.colorbar(U, ax=ax3)
        ubar.set_label("X_Velocity [ms$^{-1}$]" ) #rotation= 270
        plt.legend
        plt.style.use('classic')

        ax1.set_ylim([0, 0.001])
        ax2.set_ylim([0, 0.001])
        ax3.set_ylim([0, 0.001])
        plt.savefig("plots/boundarycontours.pdf")

class boundary:
    def __init__(self):
        return
    
    def boundarymult(self,x,y,yg,xg,u):
        self.x = x
        self.y = y
        self.yg = yg
        self.xg = xg
        self.u = u

        f5 = 0.05
        f4 = 0.07
        f3 = 0.08
        f2 = 0.1
        f1 = 0.11
        #5th plot
        i5 = len(x) - yg*int(xg*f5)
        print('-----------------------------')
        print(i5)
        print(yg*int((xg*0.04)))
        print(len(x))
        pos5 = int((100*(x[i5]/max(x))))
        y_pos= y[i5:i5+yg]
        u_x = u[i5:i5+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i5 in range(len(u_x)):
            if u_x[i5] <= 0.99*u_max:
                u_x2.append(u_x[i5])
                y_pos2.append(y_pos[i5])
        ub5_nondim = u_x2/max(u_x2)
        yb5_nondim = y_pos2/max(y_pos2)

        #############################################################################
        #4th plot
        i4 = len(x) - yg*int(xg*f4)
        print('-----------------------------')
        print(i4)
        print(yg*int((xg*0.05)))
        print(len(x))

        pos4 = int((100*(x[i4]/max(x))))
        y_pos= y[i4:i4+yg]
        u_x = u[i4:i4+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i4 in range(len(u_x)):
            if u_x[i4] <= 0.99*u_max:
                u_x2.append(u_x[i4])
                y_pos2.append(y_pos[i4])
        ub4_nondim = u_x2/max(u_x2)
        yb4_nondim = y_pos2/max(y_pos2)

        ###################################################################
        #3th plot
        i3 = len(x) - yg*int(xg*f3)
        print('-----------------------------')
        print(i3)
        print(yg*int((xg*0.06)))
        print(len(x))
        pos3 = int((100*(x[i3]/max(x))))

        y_pos= y[i3:i3+yg]
        u_x = u[i3:i3+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i3 in range(len(u_x)):
            if u_x[i3] <= 0.99*u_max:
                u_x2.append(u_x[i3])
                y_pos2.append(y_pos[i3])
        ub3_nondim = u_x2/max(u_x2)
        yb3_nondim = y_pos2/max(y_pos2)

        ###############################################################
        #2nd plot
        i2 = len(x) - yg*int(xg*f2)
        print('-----------------------------')
        print(i2)
        print(yg*int((xg*0.07)))
        print(len(x))
        pos2 = int((100*(x[i2]/max(x))))

        y_pos= y[i2:i2+yg]
        u_x = u[i2:i2+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i2 in range(len(u_x)):
            if u_x[i2] <= 0.99*u_max:
                u_x2.append(u_x[i2])
                y_pos2.append(y_pos[i2])
        ub2_nondim = u_x2/max(u_x2)
        yb2_nondim = y_pos2/max(y_pos2)

        ####################################################################
        #1st plot

        i1 = len(x) - yg*int(xg*f1)
        print('-----------------------------')
        print(i1)
        print(yg*int((xg*0.08)))
        print(len(x))
        pos1 = int((100*(x[i1]/max(x))))
        y_pos= y[i1:i1+yg]
        u_x = u[i1:i1+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i1 in range(len(u_x)):
            if u_x[i1] <= 0.99*u_max:
                u_x2.append(u_x[i1])
                y_pos2.append(y_pos[i1])
        ub1_nondim = u_x2/max(u_x2)
        yb1_nondim = y_pos2/max(y_pos2)

        ######################################################################
        ######################################################################


        #plotting the velocity profile [non dimensional]
        fig, ax1 = plt.subplots(1,1)
        ax1.plot( ub5_nondim, yb5_nondim, marker='x', color = 'green', label = '{}{} along plate'.format(pos5,"%"))
        ax1.plot( ub4_nondim, yb4_nondim, marker='x', color = 'orange', label = '{}{}along plate'.format(pos4,"%"))
        ax1.plot( ub3_nondim, yb3_nondim, marker='x', color = 'purple', label = '{}{} along plate'.format(pos3,"%"))
        ax1.plot( ub2_nondim, yb2_nondim, marker='x', color = 'black', label = '{}{} along plate'.format(pos2,"%"))
        ax1.plot( ub1_nondim, yb1_nondim, marker='x', color = 'blue', label = '{}{} along plate'.format(pos1,"%"))
        ax1.legend()

        ax1.set_xlabel("u/$U_\infty$")
        ax1.set_ylabel("$y/\delta$")
        ax1.set_title("Laminar Boundary layer at several points along the plate")
        ax1.grid()
        plt.savefig("plots/nondimboundarymultiple.pdf")

    def boundary(self,x,y,yg,xg,u):
        self.x = x
        self.y = y
        self.yg = yg
        self.xg = xg
        self.u = u
        i = len(x) - yg*int((xg*0.04))

        pos = (x[i])
        pos = str(round(pos, 3))
        y_pos= y[i:i+yg]
        u_x = u[i:i+yg]
        u_max = max(u_x)

        #u_x = [x for x in u_x if x <= 0.99*u_max]
        u_x2 =[]
        y_pos2 =[]
        for i in range(len(u_x)):
            if u_x[i] <= 0.99*u_max:
                u_x2.append(u_x[i])
                y_pos2.append(y_pos[i])
        ub_nondim = u_x2/max(u_x2)
        yb_nondim = y_pos2/max(y_pos2)

        fig, ax2 = plt.subplots(1,1)
        ax2.plot(ub_nondim,yb_nondim, color = 'green', marker='x')
        ax2.set_title("Laminar boundary layer at {}m along plate for a {}x{} mesh \n the boundary layer contains {} points".format(pos,int(xg),yg,len(yb_nondim)))
        ax2.set_xlabel("$u/U_\infty$")
        ax2.set_ylabel("$y/\delta$")
        ax2.grid()
        plt.savefig("plots/nondimboundary.pdf")