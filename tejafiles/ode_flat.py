#!/bin/python3
# --------------------------------------------------------------------------------------------------------------------------------------------
# ode_stagpoint.py
#   White, section 7-3.5, High Speed Plane Stagnation Flow
#
# version. I - stagnation point equation.
# author. gnsa1e21, 2022
# university of southampton
# --------------------------------------------------------------------------------------------------------------------------------------------

from ode_equation_flat import eq_flat
from fn_newton_root import newton_main
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# constants
eta_max = 10.0
eta_points = 1001
time_array = np.linspace(0, eta_max, eta_points)

sigma = 0.72
gw = 1.67619431
fwall = 0

# newton method to get initial conditions
fn_newton = newton_main(1e-9, 1e-10, 1e-3)
fn_newton.constants(eta_max, eta_points, sigma, gw, fwall)
fn_newton.define_inputs(eq_flat, [0, 0, 0, gw, 0], [0.2, 0.2], [2, 4], [1, 1], [1, 3])
fn_newton.solve_newton()

# solve ode
print(fn_newton.new_ini())
# fn_newton.show()  # show all the used tolerences

initial_conditions_newton = fn_newton.new_ini()
# perform ode
ode_mtd1 = solve_ivp(eq_flat, [time_array[0], time_array[-1]], initial_conditions_newton, \
    t_eval = time_array, dense_output = 'true', rtol = 1e-8, atol = 1e-8, max_step = 0.02)

# extract variables from ode solution. 
eta = ode_mtd1.t
f = ode_mtd1.y[0]; df = ode_mtd1.y[1]; ddf = ode_mtd1.y[2]
g = ode_mtd1.y[3]; dg = ode_mtd1.y[4]



# # plot all values. ------------------------------------------------------------------ potential plot presentation template
# # plt.plot(eta, f, label='f',linewidth=2.0)
# plt.plot(df, eta, label='f`',linewidth=2.0)
# # plt.plot(eta, ddf, label='f``',linewidth=2.0)
# # plt.plot(eta,  g, label='g',linewidth=2.0)
# # plt.plot(eta, dg, label='g`',linewidth=2.0)

# plt.legend(prop={'size': 18}); plt.xlabel('$\eta$', fontsize=18); plt.ylabel('  ')
# plt.ylim([0, 5.0]); plt.xlim([0, 1.2])
# plt.grid(which='major', color='#000000', linewidth=1, alpha=0.2)
# plt.grid(which='minor', color='#000000', linestyle=':', linewidth=1, alpha=0.3)
# plt.minorticks_on()

# plt.show()