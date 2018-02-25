from sympy import *
from sympy import Rational as RR
from sympy import ln as ln
vz=Symbol('U_\\text{з}')
vg=Symbol('U_\\text{г}')
R0=Symbol('R_0')
R=Symbol('R')
rho=Symbol('\\rho')
C=Symbol('C')
E=Symbol('\\mathcal{E}')
tau2=Symbol('\\tau_2')
v0=Symbol('U_0')

dE=Symbol('\\Delta \\mathcal{E}')
dVz=Symbol('\\Delta U_\\text{г}')
dVg=Symbol('\\Delta U_\\text{з}')
dR=Symbol('\\Delta R')
dC=Symbol('\\Delta C')
dR0=Symbol('\\Delta R_0')

rho=1/R+1/R0

tau2=rho*C*ln(((vz-v0)*R+(vz-E)*R0)/((vg-v0)*R+(vg-E)*R0))
F1=diff(tau2,E)*dE
F2=diff(tau2,vz)*dVz
F3=diff(tau2,vg)*dVg
F4=diff(tau2,R)*dR
F5=diff(tau2,R)*dR0
# F1=diff(tau2,E)
# x=abs(F1)+abs(F2)+abs(F3)+abs(F4)+abs(F5)

# su={
# 	dE:1,
# 	dVz:1,
# 	dVg:1,
# 	dR:10,
# 	dR0:10,
# 	dC:0.001,
# 	C:0.001,
# 	R:300000,
# 	E:123,
# 	vz:119.52,
# 	vg:109.78,
# 	R0:123600,
# 	v0:107
# }
# print(x.subs(su))
x=abs(factor(together(simplify(F1))))
print(latex(x))
print('+\\\+')
x=abs(factor(together(simplify(F2))))
print(latex(x))
print('+\\\+')

x=abs(factor(together(simplify(F3))))
print(latex(x))
print('+\\\+')

x=abs(factor(together(simplify(F4))))
print(latex(x))
print('+\\\+')

x=abs(factor(together(simplify(F5))))
print(latex(x))
