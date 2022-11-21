import numpy
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import h5py
import os.path
import matplotlib.cm as cm # latex module
import os

from ode_equation_flat import eq_flat
from fn_newton_root import newton_main
from scipy.integrate import solve_ivp
import numpy as np


plt.style.use('classic')

class plotFunctions(object):
    def __init__(self):
        return

    def contour_local(self, fig, levels0, label, variable):
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_xlabel(r"$x_0$", fontsize=20)
        ax1.set_ylabel(r"$x_1$", fontsize=20)
        ax1.set_xlim([0, 400])
        ax1.set_ylim([0, 10])

        CS = ax1.contourf(self.x, self.y, variable, levels=levels0, cmap=cm.jet)
        divider = make_axes_locatable(ax1)
        cax1 = divider.append_axes("right", size="5%", pad=0.05)
        ticks_at = numpy.linspace(levels0[0], levels0[-1], 10)
        cbar = plt.colorbar(CS, cax=cax1, ticks=ticks_at, format='%.3f')
        cbar.ax.set_ylabel(r"$%s$" % label, fontsize=20)
        ax1.set_title('Feiereisen')

        return

    def read_file(self, fname):
        f = h5py.File(fname, 'r')
        group = f["opensbliblock00"]
        return f, group

    def read_dataset(self, group, dataset):
        d_m = group["%s" % (dataset)].attrs['d_m']
        size = group["%s" % (dataset)].shape
        read_start = [abs(d) for d in d_m]
        read_end = [s-abs(d) for d, s in zip(d_m, size)]
        if len(read_end) == 2:
            read_data = group["%s" % (dataset)].value[read_start[0]:read_end[0], read_start[1]:read_end[1]]
        elif len(read_end) == 3:
            read_data = group["%s" % (dataset)].value[read_start[0]:read_end[0], read_start[1]:read_end[1], read_start[2]:read_end[2]]
        else:
            raise NotImplementedError("")
        return read_data


class KatzerPlot(plotFunctions):
    def __init__(self):
        self.Minf = 2.0
        self.Re = 950
        self.RefT = 288.0
        self.SuthT = 110.4
        self.Ly = 115.0
        self.Lx = 400.0
        self.scale = 2.31669259
        self.D11 = self.extract_metrics()
        return

    def load_reference_data(self):
        reference = numpy.loadtxt('./reference_data.txt')
        x, cf, p = reference[:, 0], reference[:, 1], reference[:, 2]
        return x, cf, p

    def extract_coordinates(self):
        f, group1 = self.read_file(fname)
        x = self.read_dataset(group1, "x0_B0")
        y = self.read_dataset(group1, "x1_B0")
        dx, dy = x[0, 1], y[1, 0]
        print("Grid size (x,y)  is: (%f, %f)" % (x.shape[1], x.shape[0]))
        print("First grid point dx: %f, dy: %f" % (dx, dy))
        dx, dy = x[0, -1]-x[0, -2], y[-1, 0]-y[-2, 0]
        print("Last grid point dx: %f, dy: %f" % (dx, dy))

        # grid plot

        return x, y

    def extract_metrics(self):
        fname = 'opensbli_output_1000000.h5'
        f, group1 = self.read_file(fname)
        D11 = self.read_dataset(group1, "D11_B0")
        return D11

    def extract_flow_variables(self, group):
        rho = self.read_dataset(group, "rho_B0")
        rhou = self.read_dataset(group, "rhou0_B0")
        rhov = self.read_dataset(group, "rhou1_B0")
        rhoE = self.read_dataset(group, "rhoE_B0")
        u = rhou/rho
        v = rhov/rho
        p = (0.4)*(rhoE - 0.5*(u**2+v**2)*rho)
        a = numpy.sqrt(1.4*p/rho)
        M = numpy.sqrt(u**2 + v**2)/a
        T = 1.4*(self.Minf**2)*p/rho
        print('---------------------------------------------------------------------------------------------')
        print('Temperature')
        print(T)
        print('---------------------------------------------------------------------------------------------')
        mu = self.compute_viscosity(T)
        return rho, u, v, rhoE, p, T, M, mu

    def compute_wall_derivative(self, variable):
        ny = numpy.size(self.y[:, 0])
        Ly = self.Ly
        delta = Ly/(ny-1.0)
        D11 = self.D11[0:6, :]
        var = variable[0:6, :]
        coeffs = numpy.array([-1.83333333333334, 3.00000000000002, -1.50000000000003, 0.333333333333356, -8.34617916606957e-15, 1.06910884386911e-15])
        coeffs = coeffs.reshape([6, 1])
        dudy = sum(D11*var*coeffs)/delta
        return dudy

    def compute_viscosity(self, T):
        mu = (T**(1.5)*(1.0+self.SuthT/self.RefT)/(T+self.SuthT/self.RefT))
        return mu

    def compute_skin_friction(self, u, mu):
        # Wall viscosity all x points
        mu_wall = mu[0, :]
        dudy = self.compute_wall_derivative(u)
        tau_wall = dudy*mu_wall
        Cf = tau_wall/(0.5*self.Re)
        return Cf

    def SBLI_comparison(self, Cf, P):
        # Skin friction plot
        x, ref_cf, ref_p = self.load_reference_data()
        # Rex0 = 0.5*(self.Re/self.scale)**2
        # x0 = 0.5*self.Re/self.scale**2
        # delta = 0.1
        # # Calculate local Reynolds number for all x
        # Rex = Rex0 + self.Re*self.x[1, :]

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # ax.plot(x, ref_cf, color='r', linestyle='--', marker='o', markevery=15, markersize=5, label='Reference')

        ax.plot(self.x[1, :], Cf, color='k', label='OpenSBLI')
        ax.axhline(y=0.0, linestyle='--', color='k')

        ax.set_xlabel(r'$x_0$', fontsize=20)
        ax.set_ylabel(r'$C_f$', fontsize=20)
        # ax.set_title('Skin friction')
        plt.legend(loc="best")
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        fig.savefig(directory + 'skin_friction.pdf', bbox_inches='tight')
        fig.clf()

        # plt.plot(x, ref_p, color='r', linestyle='--', marker='o', markevery=15, markersize=5, label='Reference')
        plt.plot(self.x[1, :], P[0, :]/P[0, 0], color='k', label="OpenSBLI")
        # linestyle='', marker='o',markevery=10)
        plt.xlabel(r'$x_0$', fontsize=20)
        plt.ylabel(r'$\frac{P_w}{P_1}$', fontsize=22)
        plt.title('Normalized wall pressure, Feiereisen')
        plt.legend(loc="best")
        plt.savefig(directory + "wall_pressure.pdf", bbox_inches='tight')
        plt.clf()

        x01, y01 = self.extract_coordinates()

        plt.scatter(x01, y01, color='k', marker='.', label="OpenSBLI")
        # linestyle='', marker='o',markevery=10)
        plt.xlabel(r'$x_0$', fontsize=20)
        plt.ylabel(r'$x_1$', fontsize=22)
        plt.title('Normalized wall pressure, Feiereisen')
        plt.legend(loc="best")
        plt.savefig(directory + "grid.pdf", bbox_inches='tight')
        plt.clf()

        f, group1 = self.read_file(fname)

        # self.x, self.y = self.extract_coordinates()
        rho, u, v, rhoE, p, T, M, mu = self.extract_flow_variables()
        variables = [rho, u, v, rhoE, p, M, T, mu]
        names = ["rho", "u", "v", "rho E", "P", "M", "T", "mu"]

        be = 100
        delta = next(x[0] for x in enumerate(u[0:be,10]) if x[1] > 0.99)
        # print(delta)
        # print(y01[55,10])

        # constants
        eta_max = 7.0
        eta_points = 1041
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

        be = 100
        delta0 = [i for i,v in enumerate(u[0:be,0]) if v > 0.999]
        delta200 = [i for i,v in enumerate(u[0:be,200]) if v > 0.999]
        delta300 = [i for i,v in enumerate(u[0:be,300]) if v > 0.999]
        delta400 = [i for i,v in enumerate(u[0:be,400]) if v > 0.999]

        plt.scatter(u[0:be,0], y01[0:be,0]/y01[delta0[0],0]*3.4, color='r', marker='.', label=" at 0")
        plt.scatter(u[0:be,200], y01[0:be,200]/y01[delta200[0],200]*3.4, color='g', marker='.', label=" at 200")
        plt.scatter(u[0:be,300], y01[0:be,300]/y01[delta300[0],300]*3.4, color='b', marker='.', label=" at 300")
        plt.scatter(u[0:be,400], y01[0:be,400]/y01[delta400[0],400]*3.4, color='magenta', marker='.', label=" at 400")
        plt.scatter(df, eta, color='k', marker='.', label=" Compressible Blas")

        # linestyle='', marker='o',markevery=10)
        plt.xlabel(r'$u$', fontsize=20)
        plt.ylabel(r'$x_1$', fontsize=22)
        plt.title('Boundary layer velocity profile, Feiereisen')
        # plt.xlim([0,1.2])
        # plt.ylim([0,6])
        plt.legend(loc="best")
        plt.savefig(directory + "boundary_layer_velocity.pdf", bbox_inches='tight')
        plt.clf()

        return

    def main_plot(self, fname, n_levels):
        f, group1 = self.read_file(fname)

        self.x, self.y = self.extract_coordinates()
        rho, u, v, rhoE, p, T, M, mu = self.extract_flow_variables(group1)
        variables = [rho, u, v, rhoE, p, M, T, mu]
        names = ["rho", "u", "v", "rho E", "P", "M", "T", "mu"]

        # Contour plots
        for var, name in zip(variables, names):
            min_val = numpy.min(var)
            max_val = numpy.max(var)
            levels = numpy.linspace(min_val, max_val, n_levels)
            print("%s" % name)
            print(levels)
            fig = plt.figure()
            self.contour_local(fig, levels, "%s" % name, var)
            plt.savefig(directory + "flatplate_%s.pdf" % name, bbox_inches='tight')
            plt.clf()
        # Compare to SBLI
        Cf = self.compute_skin_friction(u, mu)
        self.SBLI_comparison(Cf, p)
        f.close()

fname = "opensbli_output_1000000.h5"
n_contour_levels = 25
directory = './'

if not os.path.exists(directory):
    os.makedirs(directory)

KP = KatzerPlot()
KP.main_plot(fname, n_contour_levels)