#-*- coding: utf-8 -*-

import pylab
import numpy as np
import math
from numpy import arctan

pylab.rc('text', usetex=True)
pylab.rc('font', family='serif')

omega=np.logspace(0, 7, num=4000)

C=5e-8
R=13000
O=omega*R*C

# phi=abs((1-4*O**2)/np.sqrt((1-4*O**2)**2+64*O**2))
phi=arctan(8*O/(1-4*O**2))
# fi = np.loadtxt('data/chem6.tsv', skiprows=1, delimiter='\t', usecols=(0, 6))
# print(fi)

# Результаты эксперимента
# om=fi.T[0]*2*np.pi
# fi=fi.T[1]

pylab.semilogx(omega, phi, "r-")
# pylab.semilogx(om, fi, "bo", markersize=5)

pylab.xlabel(r"$\omega$")
pylab.ylabel(r"$\phi$")

pylab.grid(True)
pylab.show()


# O2=omega2*R*C
# w=nu*(2*np.pi)
# omega2=np.logspace(3.6, 7, num=100)
# phi = np.arctan(w*R2*R2*C/(R1+R2+R1*(w*R2*C)**2))
# data=np.hstack([w,phi])
# np.savetxt('phi', phi)
# np.savetxt('w', w)
# phi2=np.arcsin(fi.T[1])
# pylab.semilogx(omega2, phi2, "b-")