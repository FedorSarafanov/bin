# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt, animation
from numpy import   zeros, ones, empty, append, random, array, \
					sinh, min, argmin, ndenumerate, \
					nditer, logical_or,arange,delete, \
					hstack as hjoin, where as find, setdiff1d as setdiff, log
from numpy.random import rand
import time
start_time = time.time()

T,h = 2000,3000
Dx,Dy = 2,2
cx,cy = 1,1 

b = b0 = 3.0e-04  
N = 1
a = 0.001  
na = 1	# Количество случайных дислокаций 
ds = 0.1 # Расстояние между случайными дислокациями
Sila  = 0.001 
omega = 0.04 

n0 = 300
qp = 0 
qm = 0 

xdd = array([0.5*Dx, 0])
ydd = array([0, 0])
xd  = array([0.5*Dx ])
yd  = array([0 ])
x1  = x2 = array([])

x = array(Dx*rand(N))
y = array(Dy*rand(N))

nn = No = q1 = q2 = zeros(T)
omeg  = zeros(2) 

fig = plt.figure()
ax = plt.axes()
plt.axis([-0.2,Dx+0.2,0,Dy])
hp1, = ax.plot([], [], "ro",markersize = 10, marker=r'$\perp$')
hp2, = ax.plot([], [], "bo",markersize = 10, marker=r'$\perp$')
hp3, = ax.plot([], [], "^",c = "black",markersize = 20)
time_text = ax.text(-0.1,1.75,'', fontsize = 15)

def Dxy(x,y):
	return -y*x/(x**2+y**2+b**2)

def Gxy(x,y):
	return x*(x**2-y**2)/(x**2+y**2+b**2)**2

tic=0
toc=0
def step(i):
	global x,y,b, qp,qm,nn,No,x1,x2,start_time,tic,toc
	omeg = omega*array([1, 0])
	#####################################################################
	#Iter (саый тяжелый)
	G = empty(len(y))
	Go = omeg[0]*Dxy(x-xdd[0],y-ydd[0])+omeg[1]*Dxy(x-xdd[1],y-ydd[1])

	for j, y_j in ndenumerate(y):
		G[j] = sum(b*Gxy(x[j]-x,y[j]-y))

	S = sinh(b*(Sila+G+Go))
	x += h*S	
	#####################################################################
	# Рождение дислокаций
	xi = (Dx-2*ds)*rand(na)+ds
	yi = (Dy-2*ds)*rand(na)+ds

	if i%2 == 0:
		xii = xi-ds
		yii = yi
	else:
		xii = xi+ds
		yii = yi

	x, y = hjoin([x, xi, xii]), hjoin([y, yi, yii])

	bn = b0*ones(na)
	b = hjoin([b, bn, -bn])
	#####################################################################
	# Аннигиляция дислокаций (тяжелый) ~1.2
	g1 = find(b>0)
	g2 = find(b<0)

	for j in nditer(g1):
		A = (x[g2]-x[j])**2+(y[g2]-y[j])**2
		e,ii = min(A),argmin(A)
		k = g2[0][ii]
		if e<a:
			g1 = [setdiff(g1,j)]
			g2 = [setdiff(g2,k)]
	
	x1,y1,x2,y2,b1,b2 = x[g1],y[g1],x[g2],y[g2],b[g1],b[g2]
	x, y, b = hjoin([x1, x2]), hjoin([y1, y2]), hjoin([b1, b2])
	#####################################################################
	# Накопление деформации (возможна ошибка) (оптимизировано)
	kp = find(x>Dx) 
	if len(x[kp]) != 0:
		if min(kp)>0:
			qp += len(kp)
	q1[i] = qp

	km = find(x<0) 
	if len(x[km]) != 0:	
		if min(km)>0:
			qm += len(km)	
	q2[i] = qm
	#####################################################################
	# Формирование массива для сохранения
	nn[i] = len(y)

	# Сток дислокаций 
	kk = find(logical_or(x<0 , x>Dx))
	x, y, b = delete(x,kk), delete(y,kk), delete(b,kk)

	# Рост субграницы
	f1 = find(abs(x1-Dx/2)<Dx/4)
	f2 = find(abs(x2-Dx/2)<Dx/4)
	No[i] = len(f1[0])-len(f2[0]) 
	#####################################################################
	#toc
	# if (i%100==0)and(i!=0):
	# 	print('Время работы за ',i,' шагов: ',time.time()-start_time, ' с')
	# 	# print('Время работы за последние 100 шагов: ',time.time()-tic, ' с')
	# 	tic=time.time()
	# if i==0:
	# 	tic=time.time()
	# print('---------------')
	return x1,x2,xd,y1,y2,yd

def animate(i):
	x1,x2,xd,y1,y2,yd = step(i)
	hp1.set_data(x1, y1)
	hp2.set_data(x2, y2)
	hp3.set_data(xd, yd)
	time_text.set_text(str(i))
	return hp1, hp2, hp3,time_text

anim = animation.FuncAnimation(fig, animate, 
	# init_func = init,
	frames = T, 
	interval = 1, 
	blit = True, 
	repeat = False
	)

plt.show()
t = arange(T)
R = nn/(Dx*Dy*1e-8) 

e2 = q2*b0/Dy
e1 = q1*b0/Dy
O = No*b0/Dy

result = plt.figure()

ax1 = result.add_subplot(221)
ax1.axis([0,Dx,0,50])
ax1.hist(x1, 40, facecolor = 'blue', alpha = 0.5)

ax2 = result.add_subplot(222)
ax2.axis([0,Dx,0,50])
ax2.hist(x2, 40, facecolor = 'blue', alpha = 0.5)

ax3 = result.add_subplot(223)
ax3.plot(t, O, '-', c="black")
ax3.plot(t, R, '-', c="blue")

ax4 = result.add_subplot(224)
ax4.plot(t, e1, 'b-')
ax4.plot(t, e2, 'r-')

plt.tight_layout()
result = plt.gcf()
plt.show()