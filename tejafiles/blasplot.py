import numpy as np

def integrate_boundary_layer(self, n):
        """ Integrates the boundary-layer and calculates the scale factor from displacement thickness.
        :arg int n: Iteration number from the iterative solver.
        :returns: ndarray: y: Wall normal coordinates.
        :returns: ndarray: u: Streamwise velocity component profile.
        :returns: ndarray: T: Temperature profile.
        :returns: float: scale: Scale factor of the boundary-layer."""

        sumd, record_z = 0, 0
        ythic = 0.0001712   

        z = np.zeros(n+1)
        d_eta = self.eta[1]*0.5

        # self.soln[1,:] is the u velocity, should be 1 in free stream

        for i in range(1, n+1):
            z[i] = z[i-1] + d_eta*(self.soln[3, i] + self.soln[3, i-1])
            dm = self.soln[3, i-1] - self.soln[1, i-1]
            dd = self.soln[3, i] - self.soln[1, i]
            sumd += d_eta*(dd+dm)

            if(self.soln[1, i] > 0.999 and record_z < 1.0):
                # print "recording at iteration: ", i
                # dlta = z[i]
                record_z = 2.0
            scale = sumd

        # print("delta is :", dlta)
        # print("conversion factor is: ", scale)
        # print("scaled delta is: ", dlta/scale)
        # Rescale with displacement thickness and convert to FLOWER variable normalisation

        y, u, T = z/(scale), self.soln[1, :], self.soln[3, :]
        # Calculate du/dy at the wall
        dy = y[1]
        # self.dudy = (-3*u[0]+4*u[1]-u[2])/(2.0*dy)

        self.dudy = (-1.83333333333334*u[0]+3.00000000000002*u[1]-1.50000000000003*u[2]+0.333333333333356*u[3]-8.34657956545823e-15*u[4]+1.06910315192207e-15*u[5])/dy
        self.dTdy = (-1.83333333333334*T[0]+3.00000000000002*T[1]-1.50000000000003*T[2]+0.333333333333356*T[3]-8.34657956545823e-15*T[4]+1.06910315192207e-15*T[5])/dy

        # uref, ydomain, blthickness = 680.3481462, 0.01712, 0.0000264*1.
        # self.dydy = self.dudy* (uref/blthickness)
        # self.dTdy = self.dTdy* (uref/blthickness)

        return y, u, T, scale

y, u, T, scale = integrate_boundary_layer(100)