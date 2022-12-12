import numpy as np

class readfile:
    def __init__(self):
        #print('initialised')
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
        # velocity from the momentum
        u = rhou/rho
        v = rhov/rho
        ### -----mesh----- ###
        xg = len([y for y in y if y == 0])
        yg = int(len(y)/xg)
        print("---------------------------------------------")
        print("The mesh is {}x{}".format(xg,yg))
        print("---------------------------------------------")

        return x,y,E,P,T,cp,mu,u,v,xg,yg

