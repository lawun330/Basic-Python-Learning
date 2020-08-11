#immutable set

import random
import string
r={3,2,5,6} #create a set of r #similar to dictionary but don't have index
print('r=',r)
l=[]
d=[]
r.add(-3) #add -3  #set.add() while list.append()
r.add('A') #add string
r.add(4) 
r.add(4) #adding 4 twice doesn't duplicate #ONLY sets don't contain duplicate elements
r.remove(5) #remove five
print("before ",r)
r.pop()  #remove the first element
print('after r=',r)

for i in range(6):
	e=random.choice(string.ascii_letters) #produce random character 
	#string.ascii_letters >> any alphabet
	#string.ascii_lowercase >> lower case alphabet
	#string.ascii_uppercase >> upper case alphabet
	l.append(e) #add to a list
s=set(l) #create a set in random order of previous random character from list
#set() operates by making a set of list elements
print('s=',s)

j={2,4,5,25,6}
print('j=',j)
print(r|j) #union 
print(r&j) #intersection
print(r-j) #produce (setR -intersectionRJ) part
print(j-r) #produce (setJ -intersectionRJ) part
print(r^j) #union- intersection