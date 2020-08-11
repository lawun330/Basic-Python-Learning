import math as m
import random as r
import itertools as it

side=[x*0.1 for x in range (1,1001)]
reqArea=int(input('The required area - '))
sideLengths=[]
print('\n')
u=0.0
v=0.0
z=0.0


for L in it.combinations(side,3):
	p=sum(L)
	s=round(p/2,2)
	Q=s*(s-L[0])*(s-L[1])*(s-L[2]) #heron's formula
		
	u=round(L[0],1)
	v=round(L[1],1)
	z=round(L[2],1)

	if Q>0:
		Area= int(m.sqrt(Q))
		if Area==reqArea:
			sideLengths.append(L)

	print(u,v,z) 	

Set=set(sideLengths)

print('The following is a set of lengths of triangle that can satisfy the required Area of {0} -\n\n{1}'.format(reqArea,Set))
