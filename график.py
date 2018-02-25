import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import * 

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

#################################################
#################################################

# Константы

n0=8400				# Плотность намотки
mu0=4*pi*(10**(-7)) # Магнитная постоянная
eta=1.74*(10**11)	# Известное e/m
D=0.07				# Диаметр соленоида
U=75				# Эффективное напряжение на пластинах

lg=0.122-0.014 
lv=0.144-0.016 
L=lg

# Переменные

L=0.016 	# Длина пластин
d=0.0055 	# Расстояние между пластинами


U_a=1000	# Напряжение второго анода
I=27*0.02	# Ток на соленоиде


B=mu0*n0*I 			# Индукция в соленоиде
omega=eta*B			# Циклотронная частота
v0z=sqrt(eta*2*U_a)	# Скорость по вылете из пластин
tau=L/v0z 			# Время пролета в пластинах
E=U/L				# Напряженность в пластинах


v0y=eta*E*tau		# Однородное электрическое поле: скорость по вылете
R=v0y/omega			# Радиус оборота в однородном магнитном поле
# if vert:
# 	l=lv
# if not vert:
# 	l=lg
# beta=(l/v0z*omega)


#################################################
#################################################

def v_perp(t):
	vy=eta*E/omega*(cos(omega*t)-1)
	vx=eta*E/omega*(sin(omega*t))
	return sqrt(vx**2+vy**2)

_R=v_perp(tau)/omega


def y(t):
	return	(eta*E/omega**2)*(np.sin(omega*t)-omega*t)
		
def x(t):
	return	-(eta*E/omega**2)*(1-np.cos(omega*t))	
	 

def z(t):
	return v0z*t

def y_(t):
	return R*np.sin(omega*t)

def x_(t):
	return R*np.cos(omega*t)-R

def y_leq(t):
	return	-(_R*np.sin(omega*t))+y_(tau)
		
def x_leq(t):
	return	-(_R*np.cos(omega*t)-_R)+x_(tau)


t=np.linspace(0,10*tau,100)
# T=np.linspace(tau,2*tau,100)

plt.xlabel('xlabel')
plt.ylabel('ylabel')
print(x(tau),y(tau),z(tau))

ax.plot(x(t), y(t), z(t), label='parametric', alpha=0.7,color='blue')
ax.plot([x(tau)], [y(tau)], [z(tau)], marker='o', label='parametric', alpha=0.7,color='black')
ax.plot([x_(tau)], [y_(tau)], [z(tau)], marker='o', label='parametric', alpha=0.7,color='black')
ax.plot(x_(t), y_(t), z(t), label='parametric', alpha=0.7, color='red')
# ax.plot(x_(T), y_(T), z(T), label='parametric', alpha=0.7, color='red')
# ax.plot(x_leq(T), y_leq(T), z(T), label='parametric', alpha=0.7, color='blue')
plt.show()
