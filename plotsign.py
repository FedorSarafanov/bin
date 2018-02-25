import numpy as np
from numpy.fft import fft as fft
from numpy import sign, sin,pi
import matplotlib.pyplot as plt

t = np.linspace(0,10,100)
x = sign(sin(t))
plt.plot(t, x)
plt.show()
