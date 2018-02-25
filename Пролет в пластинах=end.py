# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# import matplotlib.pyplot as plt
from math import * 

# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')

#################################################
#################################################

# Константы

n0=8400				# Плотность намотки
mu0=4*pi*(10**(-7)) # Магнитная постоянная
eta=1.74*(10**11)	# Известное e/m
dI=0.015

lg=0.122-0.014 
lv=0.144-0.016 

def delta_n(I1,I2):
	dn=I1/(I2-I1)*(dI/I1+2*dI/(I2-I1))
	return 'Количество фокусивок, эксперимент: '+str(I1/(I2-I1))+', доверительный интервал: '+str([I1/(I2-I1)-dn,I1/(I2-I1)+dn])
	# return I1/(I2-I1)

# Переменные
def great(U_a,I,L,d,vert):
# def __main():
	print(U_a,'вольт')
	# vert=0
	# L=0.016 	# Длина пластин
	# d=0.0055 	# Расстояние между пластинами
	D=0.07		# Диаметр соленоида

	# U_a=1000	# Напряжение второго анода
	# I=27*0.02	# Ток на соленоиде
	U=75		# Эффективное напряжение на пластинах

	B=mu0*n0*I 			# Индукция в соленоиде
	omega=eta*B			# Циклотронная частота
	v0z=sqrt(eta*2*U_a)	# Скорость по вылете из пластин
	tau=L/v0z 			# Время пролета в пластинах
	E=U/L				# Напряженность в пластинах


	v0y=eta*E*tau		# Однородное электрическое поле: скорость по вылете
	R=v0y/omega			# Радиус оборота в однородном магнитном поле
	if vert:
		l=lv
	if not vert:
		l=lg
	beta=(l/v0z*omega)


	#################################################
	#################################################

	# def v_perp(t):
	# 	vy=eta*E/omega*(cos(omega*t)-1)
	# 	vx=eta*E/omega*(sin(omega*t))
	# 	return sqrt(vx**2+vy**2)

	# R_=v_perp(tau)/omega

	def v_y(t):
		return (E/B)*(np.cos(omega*t)-1)

	def v_x(t):
		return (E/B)*(np.sin(omega*t))

	def y(t):
		return (eta*E/omega**2)*(np.sin(omega*t)-omega*t)

	def x(t):
		return (eta*E/omega**2)*(1-np.cos(omega*t))		

	def phi(t):
		if vert:
			return atan(abs(v_x(t))/abs(v_y(t)))
		else:
			return atan(abs(v_y(t))/v_x(t))

	def alpha2(t):
		if vert:
			return (omega*t/2)
		else:
			return (pi/2-omega*t/2)

	# tt=np.linspace(0,10*tau,20)

	# print(alpha(tt))
	# print(alpha2(tt))
	if vert:
		phi_0=pi/2-phi(tau)
	else:
		phi_0=pi-phi(tau)

	# print(atan(abs(v_x(tau))/abs(v_y(tau))))

	# print('Оборотов вне пластин, рад:',beta)
	# print('Оборотов в пластинах без скрещенных полей, рад:',omega*tau)
	# print('Оборотов в пластинах со скрещенными полями, рад:',phi_0)	
	# print(alpha(tau))
	# print(alpha2(tau))
	# print(x(tau))
	print('vert',vert)
	# print(y(tau))
	# print(v_x(tau))
	# print(v_y(tau))	
	print('Количество фокусировок, теория`: '+str((beta+alpha2(tau))/(2*pi)))
	# return('Количество фокусировок, теория: '+str((beta+phi_0)/(2*pi)))

# print('Данные группы 2.')
# __main()
print(great(1200,0.6,0.014,0.006,0))
print(delta_n(0.6,1.14))
print('---------')
print(great(1000,0.54,0.014,0.006,0))
print(delta_n(0.54,1.04))
print('---------')
print(great(1000,0.5,0.016,0.0055,1))
print(delta_n(0.5,1.09))
print('---------')
print(great(1100,0.46,0.016,0.0055,1))
print(delta_n(0.46,1.08))
print('---------')

print('Данные группы 3.')

print(great(1000,31*0.02,0.016,0.0055,1))
print(delta_n(31*0.02,54*0.02))
print('---------')

print(great(850,29*0.02,0.016,0.0055,1))
print(delta_n(29*0.02,50.5*0.02))
print('---------')

print(great(1300,31.5*0.02,0.014,0.006,0))
print(delta_n(31.5*0.02,54*0.02))
print('---------')

print(great(1100,32*0.02,0.014,0.006,0))
print(delta_n(32*0.02,54*0.02))
print('---------')
