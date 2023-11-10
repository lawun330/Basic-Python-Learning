
#object Lifecycle
#garbage collection
#Python's memory cleaning and management
def docu():
	'''Python auto deletes values and objects if they're not used for enough time and it can be viewed through gc module'''
	pass

print (docu.__doc__,'\n') #__doc__ calls documentation under function Gcollect()

#--------------------------

#simple version
#understand as reference count
a=42   #ref count for a=42 is 1 
#<42> is an new object

a=409  #ref count for a=42 is 0 #ref count for a=409 is 1 
#<409> is an new object, the older object is deleted by gc since ref count==0

a=67   #ref count for a=42 is 0 #ref count for a=409 is 0 #ref count for a=67 is 1 
#<67> is an new object, the older objects are deleted by gc since ref count==0

import gc  #garbage collection module for controlling it
gc.get_threshold() #returns (700,10,10) in shell  #meaning 700 occurences and python will run its garbage collection
'''Python consists of three generations. Each generation has a certain threshold number of objects that it can allow. 
A new object starts its life in the first generation of the garbage collector. 
If Python executes a manual garbage collection process on a generation and an object survives, it moves up into a second, older generation.'''
#--------------------------


#class version

class CarWheels:
	def __init__(self,w):
		self.wheels=w

b=CarWheels(4) #ref count of object b is 1 
print(b.wheels)
print("b memory location :",hex((id(b))))

import weakref #weak reference module
r=weakref.ref(b) #weak reference which means ref count for object r=0
#the weak reference value is linked with b value

print("Before : ",r) #check the weak reference

b=None #b has None value

print("After : ",r) #now the weak reference is dead
#-------------------------

#another example 

a=30  #<30> object is created  
#ref count =1

b=a   #<30> object is linked with b again
#ref count =2

c=[b] #<30> object is linked with c again as a list
#ref count =3

del a # a is deleted  #<30> object is not linked or related with a anymore 
#ref count =2

b=100 #<30> is not linked with b #<100> is linked with b
#ref count for <30>=1
#ref count for <100>=1

c[0]=-8 #<30> is not linked with c list  #<-8> is linked
#ref count for <30>=0
#<30> object is deleted by python gc
#ref count for <-8>=1