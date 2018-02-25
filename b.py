from math import *
H=0.85 #m
dh=0.01 # 0.1cm
h_0=0.59 #m
l=H-h_0
p_a=100258 #pa
rho=1000
g=9.81

ch=-(p_a-rho*g*h_0+rho*g*l)
sq=sqrt((p_a-rho*g*h_0+rho*g*l)**2+4*rho**2*g**2*h_0*l)
zn=2*rho*g

print((ch+sq)/zn*100)
print(rho*g*h_0*dh)