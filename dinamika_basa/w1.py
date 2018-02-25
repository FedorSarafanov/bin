with open('input.txt') as f:
	lines=f.readlines()
	a=[int(i) for i in lines[1].split()]
	A=a
	b=[int(i) for i in lines[2].split()]
	B=b
	c=[int(i) for i in lines[0].split()]
	n=c[0]
	m=c[1]
	p=c[2]
	q=c[3]
	f.close()

c=[0 for j,B in enumerate(b)] # массив занятых маршрутов
r=[[0]*len(a) for j,B in enumerate(b)] # массив радиусов

while a!=[] and (0 in c):
	mini,minj=0,0
	for i in range(len(b)):
		for j in range(len(a)):
			if r[i][j]!=float('inf'):
				R=r[i][j]=abs(b[i]-a[j])
			if R<=r[mini][minj]:
				mini,minj=i,j
	c[mini]=a[minj]
	del A[minj]
	r[mini][minj]=float('inf')

r=[0]*len(B)
for i in range(len(B)):
	r[i]=abs(B[i]-c[i])
	if c[i]==0:
		r[i]=0

for i,R in enumerate(r):
	if R>q+p:
		A+=[c[i]]
		c[i]=0
		r[i]=0

penalty=len(A)*p+c.count(0)*q+sum(r)
print(penalty)

with open('output.txt','w') as f:
	f.write(str(penalty))
	f.close()