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
	# return 'Количество фокусивок, эксперимент: '+str(I1/(I2-I1))+', доверительный интервал: '+str([I1/(I2-I1)-dn,I1/(I2-I1)+dn])
	print('n:',I1/(I2-I1))
	print('delta_n:',dn)

# Переменные
def great(U_a,I,I2,L,d,vert):
	print(U_a,'вольт')
	delta_n(I,I2)
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
		return eta*E/omega*(cos(omega*t)-1)

	def v_x(t):
		return eta*E/omega*(sin(omega*t))

	def phi(t):
		if vert:
			return atan(abs(v_x(t))/abs(v_y(t)))
		else:
			return atan(abs(v_y(t))/v_x(t))

	# def y(t):
	# 	# if t<=tau:	
	# 	# 	return (eta*E/omega**2)*(np.sin(omega*t)-omega*t)
	# 	# if t>tau:
	# 	# 	return y(tau)+R_*np.sin(omega*t)
	# 	result=[]
	# 	for T in t:
	# 		if T<=tau:
	# 			temp=(eta*E/omega**2)*(np.sin(omega*T)-omega*T)
	# 			result.append(temp)
	# 		if T>tau:
	# 			temp=y([tau])-R_*np.sin(omega*T)
	# 			result.append(temp)
	# 	return np.array(result)		

	# def x(t):
	# 	result=[]
	# 	for T in t:
	# 		if T<=tau:
	# 			temp=(eta*E/omega**2)*(1-np.cos(omega*T))	
	# 			result.append(temp)
	# 		if T>tau:
	# 			temp=x([tau])+R_*np.cos(omega*T)-R_
	# 			result.append(temp)
	# 	return np.array(result)

	# def z(t):
	# 	return v0z*t

	# def y_(t):
	# 	return -R*np.sin(omega*t)

	# def x_(t):
	# 	return R*np.cos(omega*t)-R


	# time=10*tau
	# print(tau, 2*pi/omega)
	# t=np.linspace(0,2*tau,100)

	if vert:
		phi_0=pi/2-phi(tau)
	else:
		phi_0=pi-phi(tau)


	# print('Оборотов вне пластин, рад:',beta)
	# print('Оборотов в пластинах без скрещенных полей, рад:',omega*tau)
	# print('Оборотов в пластинах со скрещенными полями, рад:',phi_0)	
	# print(y(t))
	# print(R,R_)

	# ax.plot(x(t), y(t), z(t), label='parametric', alpha=0.3)
	# ax.plot(x_(t), y_(t), z(t), label='parametric', alpha=0.7, color='red')
	# 
	# print(phi_0)
	# print(x([tau]),y([tau]),v_x(tau),v_y(tau))
	# return (2*pi-phi_0)/(2*pi)
	# print(v_x(tau),v_y(tau))	
	# print(v0y*cos(omega*tau),v0y*sin(omega*tau))
	return(str((beta+phi_0)/(2*pi)))
	# plt.show()

print(great(1200,0.6, 1.14, 0.014,0.006,0))
# print(delta_n(0.6,1.14))
print('---------')
print(great(1000,0.54, 1.04, 0.014,0.006,0))
# print(delta_n(0.54,1.04))
print('---------')
print(great(1000,0.5, 1.09, 0.016,0.0055,1))
# print(delta_n(0.5,1.09))
print('---------')
print(great(1100,0.46, 1.08, 0.016,0.0055,1))
# print(delta_n(0.46,1.08))
print('---------')

# print('Данные группы 3.')

# print(great(1000,31*0.02,0.016,0.0055,1))
# print(delta_n(31*0.02,54*0.02))
# print('---------')

# print(great(850,31*0.02,0.016,0.0055,1))
# print(delta_n(29*0.02,50.5*0.02))
# print('---------')

# print(great(1300,31.5*0.02,0.014,0.006,0))
# print(delta_n(31.5*0.02,54*0.02))
# print('---------')

# print(great(1100,32*0.02,0.014,0.006,0))
# print(delta_n(32*0.02,54*0.02))
# print('---------')