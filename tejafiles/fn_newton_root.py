#!/bin/python3
# --------------------------------------------------------------------------------------------------------------------------------------------
# fn_newton_root
#   Numerical solution for self-similar fay-riddell method 1 boundary layer 
#           equations multiple shooting method. 
#
# version. I - newton method solution
# author. gnsa1e21, 2022
# university of southampton
# --------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
from scipy.integrate import solve_ivp

class newton_main():

    # init method or constructor
    def __init__(self, req_tol, tol, delta):
        self.req_tol = req_tol
        self.tol = tol
        self.delta = delta

    def constants(self, eta_max, eta_points, sigma, gw, fwall):
        self.eta_max = eta_max
        self.eta_points = eta_points
        self.time_array = np.linspace(0, eta_max, eta_points)

        self.sigma = sigma
        self.gw = gw
        self.fwall = fwall


    # define inputs for the ode
    #       ode = 'equation_in_question'
    #       ini_con = initial conditions for the ode
    #       guess = initial guess for the shooting method
    #       pos_ini = position of initial guesses
    #       boundary = boundary conditions
    #       pos_bd = position of boundary conditions

    def define_inputs(self, ode, ini_con, guess, pos_ini, boundary, pos_bd):
        self.ode = ode
        self.ini_con = ini_con
        self.guess = guess
        self.pos_ini = pos_ini
        self.boundary = boundary
        self.pos_bd = pos_bd

    # solve with newton method
    def solve_newton(self):
        print('Solving for initial solutions')
        tolerance_stop = 1

        while tolerance_stop > self.req_tol: 
            # create a p matrix
            p_mat_size = (len(self.pos_bd),len(self.pos_bd))
            p_matrix = np.zeros(p_mat_size)

            boundary_array = []

            r_array = np.zeros(len(self.pos_bd))

            # assign variables
            for i in range(0, len(self.pos_ini)):
                self.ini_con[self.pos_ini[i]] = self.guess[i]
                # print(self.ini_con)

            # create delta matrix
            del_mat_size = (len(self.pos_ini)+1,len(self.ini_con))
            delta_matrix = np.zeros(del_mat_size)

            for g in range(0,len(self.pos_ini)):
                delta_matrix[g+1, self.pos_ini[g]] = self.delta
            
            y_initial = self.ini_con + delta_matrix

            for yi in range(0, len(y_initial)):
                # print(y_initial[yi, :])
                extract_cond = y_initial[yi, :]
                ini_conditions = extract_cond.tolist()
                print(ini_conditions)


                ode_solution = solve_ivp(self.ode, [self.time_array[0], self.time_array[-1]], ini_conditions, \
                    t_eval = self.time_array, dense_output = 'true', rtol = 1e-8, atol = 1e-8, max_step = 0.02)

                boundary_array.append(ode_solution.y[:, -1])

            for p in range(0, len(self.pos_bd)):
                for  o in range(0, len(self.pos_bd)):
                    p_matrix[p, o] = (boundary_array[o+1][self.pos_bd[p]] - boundary_array[0][self.pos_bd[p]])/self.delta
                
                r_array[p] = self.boundary[p] - boundary_array[0][self.pos_bd[p]]

            resolve = np.linalg.solve(p_matrix, r_array.T)
            self.guess = self.guess + resolve.T

            # monitor tolerance
            tolerance_stop = abs(r_array[0])



    def new_ini(self):
        print('------------------------------------ Returing calculated initial conditions in their respective positions')
        return self.ini_con 
        

    def show(self):
        print('------------------------------------ required tolerance set::', self.req_tol)
        print('------------------------------------   actual tolerance set::', self.tol)
        print('------------------------------------             step delta::', self.delta)