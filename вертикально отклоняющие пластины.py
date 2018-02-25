import numpy as np
from math import * 
import matplotlib.pyplot as plt

# Константы

n0=8400				# Плотность намотки
mu0=4*pi*(10**(-7)) # Магнитная постоянная
eta=1.74*(10**11)	# Известное e/m
D=0.07				# Диаметр соленоида
U=75				# Эффективное напряжение на пластинах


l=0.144-0.016 		# Расстояние от горизонтально отклоняющих пластин до экрана
L=0.016 			# Длина пластин

d=0.006 			# Расстояние между пластинами


U_a=1000			# Напряжение второго анода
I=54*0.02			# Ток на соленоиде
# I=25*0.02			# Ток на соленоиде

# U_a=1100			# Напряжение второго анода
# I=23*0.02			# Ток на соленоиде

B=mu0*n0*I 			# Индукция в соленоиде
omega=eta*B			# Циклотронная частота

ex_g=[[1200,30,57],[1000,27,52]]

for el in ex_g:
	v0z=sqrt(eta*2*el[0])	# Скорость по вылете из пластин
	tau=L/v0z 			# Время пролета в пластинах
	E=U/d				# Напряженность в пластинах
	T=l/v0z
	tt=T
	Omega=eta*el[1]*0.02*mu0*n0
	print("Закручено всего",el[1]/(el[2]-el[1]))
	print("Пролетело вне пластин",Omega*tt/2/pi)
	print("Практический пролет в пластинах",el[1]/(el[2]-el[1])-Omega*tt/2/pi)
	print("Теоретический пролет",Omega*tau/2/pi)
	print("Поворот",atan(((1-cos(Omega*tau))/sin(Omega*tau))**(1))/2/pi)
	print('------------------------')
	pass

l=0.122-0.014 		# Расстояние от вертикально отклоняющих пластин до экрана
L=0.014 			# Длина пластин


ex_v=[[1000,25,54],[1100,23,54]]

for el in ex_v:
	v0z=sqrt(eta*2*el[0])	# Скорость по вылете из пластин
	tau=L/v0z 			# Время пролета в пластинах
	E=U/d				# Напряженность в пластинах
	T=l/v0z
	tt=T
	Omega=eta*el[1]*0.02*mu0*n0
	print("Закручено всего",el[1]/(el[2]-el[1]))
	print("Пролетело вне пластин",Omega*tt/2/pi)
	print("Практический пролет в пластинах",el[1]/(el[2]-el[1])-Omega*tt/2/pi)
	print("Теоретический пролет",Omega*tau/2/pi)
	print("Поворот",atan((1-cos(Omega*tau))/sin(Omega*tau))/2/pi)	
	print('------------------------')
	pass

v0z=sqrt(eta*2*U_a)	# Скорость по вылете из пластин
tau=L/v0z 			# Время пролета в пластинах
E=U/d				# Напряженность в пластинах

T=l/v0z

tt=T+tau

# print(omega*tt/2/pi)


v0y=eta*E*tau		# Однородное электрическое поле: скорость по вылете
R=v0y/omega			# Радиус оборота в однородном магнитном поле

def v_y(t):
	return -eta*E/omega*(np.sin(omega*t))

def v_x(t):
	return eta*E/omega*(np.cos(omega*t)-1)

def y(t):
	return	-(eta*E/omega**2)*(1-np.cos(omega*t))	

def x(t):
	return	(eta*E/omega**2)*(np.sin(omega*t)-omega*t)	

R_=sqrt(v_x(tau)**2+v_y(tau)**2)/omega

def x_(t):
	return R*np.cos(omega*t)-R

def y_(t):
	return -(R*np.sin(omega*t))

# for t in [0, tau/2, tau]:
# 	print(v_x(t),v_y(t),x(t),y(t))
# t=np.linspace(0,2*tau,100)

# plt.plot(x(t), y(t), label='parametric', alpha=0.7,color='blue')
# plt.plot(x(tau), y(tau), marker='^', alpha=0.7,color='blue')
# plt.plot(x_(t), y_(t), alpha=0.7,color='red')
# plt.plot(x_(tau), y_(tau), marker='^', alpha=0.7,color='red')

# # plt.plot(v_x(t), v_y(t), label='parametric', alpha=0.7,color='red')

# plt.show()