# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pylab import * 
from math import *

t=np.linspace(0,1,100)
a=t+2*e**(-t/2)-2

plot(a, t, linestyle = '--', color='black', label='$S(t)$')
plot(a, np.sqrt(t), linestyle = '-', color='black', label='$S(t^2)$')

# # for counter in delta_m:
# #     gca().add_patch(Rectangle((delta_m[i]-dm,a[i]-get_A_err(t[i])), 2*dm, 2*get_A_err(t[i]), color="black",fill="black"))
# #     i+=1


# Вывод графика

grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')
legend()

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('font', size=15)
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

ylabel(r'$S$')
xlabel(r'$t$ or $t^2$ . Formule: a=t+2*e**(-t/2)-2')

# savefig( "img/ex4.eps")
show()

