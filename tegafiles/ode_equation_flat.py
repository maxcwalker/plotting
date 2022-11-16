#!/bin/python3
# --------------------------------------------------------------------------------------------------------------------------------------------
# ode_equation_stagpoint.py
#   White, section 7-3.5, High Speed Plane Stagnation Flow
#
# version. I - stagnation point equation.
# author. gnsa1e21, 2022
# university of southampton
# --------------------------------------------------------------------------------------------------------------------------------------------

import math
import numpy as np

def eq_flat(t, y):

    pr = 0.72
    # suthcon = 110.4/61.15

    xmach = 2.0
    gama = 1.4
    # theta = 0.505

    Te=288.0
    c2=110.4
    a = c2/Te

    f, df, ddf = y[0], y[1], y[2]
    g, dg = y[3], y[4]
    
    suth = 110.4/288.0
    c = np.sqrt(y[3])*(1.0+suth)/(y[3]+suth)
    dcdg = 1.0/(2.0*np.sqrt(y[3])) - np.sqrt(y[3])/(y[3]+suth)
    dcdg *= (1.0+suth) / (y[3]+suth)
    cp = dcdg*y[4]

    c = np.sqrt(y[3])*(1.0+suth)/(y[3]+suth)
    dcdg = 1.0/(2.0*np.sqrt(y[3])) - np.sqrt(y[3])/(y[3]+suth)
    dcdg *= (1.0+suth) / (y[3]+suth)
    cp = dcdg*y[4]
    return [y[1], y[2], -y[2]*(cp+y[0])/c, y[4], -y[4]*(cp+pr*y[0])/c - pr*(gama-1)*xmach**2 * y[2]**2]

