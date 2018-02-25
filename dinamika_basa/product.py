from matplotlib import pyplot as plt, animation
from numpy import   zeros, ones, empty, append, random, array, \
					sinh, min, argmin, ndenumerate, \
					nditer, logical_or,arange,delete, \
					hstack as hjoin, where as find, setdiff1d as setdiff, log
from numpy.random import rand
import numpy as np


A=ones([10,10])
B=ones([10,10])
# print(A)
grad=0.5
lines=10
days=10

cday=1
for day in arange(1,days):
	cday+=1
	#взятие
	for i in arange(0,lines):
		count=int(9/(i+1)+0.1)
		A[i][0:count]=0
		B[i][0:count]=0
		A[i]=np.random.permutation(A[i])
		B[i]=np.random.permutation(B[i])
	#сортировка
	A=np.sort(A, axis=0)
	# print(A)
	#расстановка
	for i in arange(0,lines):
		A[i][find(A[i]==0)]=day+1
		B[i][find(B[i]==0)]=day+1
print(A)
print('---------')
print(B)
# print(C)
X=A.flatten()
Y=B.flatten()
x=array(find(X<cday-8))
y=array(find(Y<cday-8))
# print('С сортировкой просрочено: ')
print(len(x[0]),len(y[0]))