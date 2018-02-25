import numpy as np
from scipy.signal import argrelextrema

data = np.loadtxt("data/phi-t.dat",delimiter="	", skiprows=1)

print(data)
a=[]
phi=-1
t=-1
for dat in data:
	if phi!=-1:
		print((dat[1]-phi)/(dat[0]-t))
	phi=dat[1]
	t=dat[0]
print(a)
for dat in a:
	print(str(a[0])+'	'+str(a[1]))
# r=17.5*10**(-1)
# m=280
# g=981
# dt=0.2
# dm=0.5
# dr=0.005
# dh=0.1

# def dI(t1,t2,f1,f2,h1,h2):
# 	df1=(h1*dr+dh*r)/r**2
# 	df2=(h2*dr+2*dh*r)/r**2

# 	f=(m*g*r*(t2-t1))/(f2-f1*(1-(t2/t1-1)**2))

# 	delta=f*(t2-t1)*(g*dm*r+g*dr*m)+r**2*dm+2*m*r*dr+2*f*2*dt+2*f*(t2-t1)*2*dt*f1/t1*(t2/t1-1)+f*(t2-t1)*(df2-df1*(1-(t2/t1-1)**2))

# 	return delta#(m*g*r*(t2-t1)**2)/(f2-f1*(1-(t2/t1-1)**2))-m*r**2

# def dI2(t1,t2,f1,f2,h1,h2):
# 	e8=2*dt
# 	e7=2*(t2-t1)*e8
# 	e6=(dm*r+dr*m)*g
# 	e5=e7*m*g*r+(t2-t1)**2*e6
# 	e4=(h1*dr+dh*r)/r**2
# 	e3=(h2*dr+dh*r)/r**2
# 	e2=2*t2/t2*(t2+t1)*dt/t1**2
# 	e1=2*r*dr*m+dm*r**2	

# 	a=m*g*r*(t2-t1)**2
# 	b=f2-f1*(1-(t2/t1-1)**2)
# 	c=1-(t2/t1-1)**2

# 	delta=e1+(a*(e3+f1*e4+e4*c)+b*e6)/b**2
# 	return delta#(m*g*r*(t2-t1)**2)/(f2-f1*(1-(t2/t1-1)**2))-m*r**2

# def I(t1,t2,f1,f2):
# 	return (m*g*r*(t2-t1)**2)/(f2-f1*(1-(t2/t1-1)**2))-m*r**2

# def M(t1,t2,f1,f2):
# 	return (m*g*r*(f2-f1*(1+(t2/t1-1)**2)))/(f2-f1*(1-(t2/t1-1)**2))

# def omega0(t1,t2,f1,f2):
# 	return 2*(f2-f1)/(t2-t1)

# def omega1(t1,t2,f1,f2):
# 	return 2*(f1)/(t1)

# names=['end_1','end_2','end_3',
# 		'start_1','start_2','start_3','none_1','none_2','none_3','middle_1','middle_2']
# # names=['end_1']

# for name in names:
# 	# pass
# 	data = np.loadtxt("data/cargo_"+name+".dat",delimiter="	", skiprows=1)

# 	nah=np.where(data[:,[1]] > 0.315)[0][0]
# 	data=data[nah:]
# 	data[:,[0]]-=data[:,[0]][0] # Время от нуля
# 	# print(data)

# 	t=data[:,0]
# 	x=data[:,1]

# 	idnx_1=x.argmax(axis=0);
# 	t_1=t[x.argmax(axis=0)]
# 	H=x[x.argmax(axis=0)]

# 	phi_1=H/r

# 	t=data[idnx_1:][:,0];
# 	x=data[idnx_1:][:,1];

# 	t_2=t[x.argmin(axis=0)]
# 	h=x[x.argmin(axis=0)]
# 	H2=H-h

# 	phi_2=H2/r
# 	print('cargo_'+name)
# 	print('----')
# 	print('t_1=',t_1)
# 	print('h=',153-H)
# 	print('phi_1=',phi_1)
# 	print('t_2=',t_2)
# 	print('h"=',H2)
# 	print('phi"=',phi_2)
# 	print('phi_2=',phi_1+phi_2)
# 	print('I=',I(t_1,t_2,phi_1,phi_1+phi_2))
# 	print('M_0=',M(t_1,t_2,phi_1,phi_1+phi_2))
# 	print('omega_0=',omega0(t_1,t_2,phi_1,phi_1+phi_2),r'\text{c}^{-1}')
	
# 	print('omega_1=',omega1(t_1,t_2,phi_1,phi_1+phi_2),r'\text{c}^{-1}')
# 	print('\eta=',(omega1(t_1,t_2,phi_1,phi_1+phi_2)**2-omega0(t_1,t_2,phi_1,phi_1+phi_2)**2)/omega1(t_1,t_2,phi_1,phi_1+phi_2)**2*100,r'\%')
# 	print(r'A_\text{тр}=',m*g*h-(omega1(t_1,t_2,phi_1,phi_1+phi_2)**2-omega0(t_1,t_2,phi_1,phi_1+phi_2)**2)*I(t_1,t_2,phi_1,phi_1+phi_2)/2,r'\text{erg}')

# 	print('dI=',dI2(t_1,t_2,phi_1,phi_1+phi_2,153-H,H2))
# 	print('----')
# 	print()

# for name in names:
# 	# pass
# 	data = np.loadtxt("data/cargo_"+name+".dat",delimiter="	", skiprows=1)

# 	nah=np.where(data[:,[1]] > 0.315)[0][0]
# 	data=data[nah:]
# 	data[:,[0]]-=data[:,[0]][0] # Время от нуля
# 	# print(data)


# 	t=data[:,0]
# 	x=data[:,1]




# 	idnx_1=x.argmax(axis=0);
# 	t_1=t[x.argmax(axis=0)]
# 	H=x[x.argmax(axis=0)]

# 	phi_1=H/r
# 	data=data[idnx_1:];

# 	# print(data[:,[1]]);
# 	print('cargo_'+name)
# 	print(data[np.where((152-data[:,[1]]) > 9.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 19.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 29.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 39.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 49.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 59.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 69.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 79.999)[0][0]][0])
# 	print(data[np.where((152-data[:,[1]]) > 89.999)[0][0]][0])


# 	# phi_2=H2/r
# 	# print('cargo_'+name)
# 	print('----')
# 	# print('t_1=',t_1)
# 	# print('h=',153-H)
# 	# print('phi_1=',phi_1)
# 	# print('t_2=',t_2)
# 	# print('h"=',H2)
# 	# print('phi"=',phi_2)
# 	# print('phi_2=',phi_1+phi_2)
# 	# print('I=',I(t_1,t_2,phi_1,phi_1+phi_2))
# 	# print('dI=',dI2(t_1,t_2,phi_1,phi_1+phi_2,153-H,H2))
# 	# print('----')
# 	print()
