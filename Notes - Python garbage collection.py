'''This file explains the Python garbage collection process in details. 
It can be executed.
Python consists of three generations.
Each generation has a certain threshold number of objects that it allow. 
A new object starts its life in the first generation of the garbage collector. 
If Python executes a manual garbage collection process on a generation and an object survives, it moves up into a second, older generation.'''

# OBJECT LIFECYCLE # GARBAGE COLLECTION # PYTHON MEMORY MANAGEMENT
import gc  # garbage collection module for controlling it
gc.get_threshold() # returns (700, 10, 10), meaning 700 occurences and python will run its garbage collection

#######################################################

# HOW GC WORKS WITH A VARIABLE

# ref count stands for reference count
a = 42	# ref count for 'a = 42' is 1
# <42> is a new object

a = 409	# ref count for 'a = 42' is 0 # ref count for 'a = 409' is 1
# <409> is a new object # the older object is deleted by gc since its ref count reaches 0

a = 67	# ref count for 'a = 42' is 0 # ref count for 'a = 409' is 0 # ref count for 'a = 67' is 1
# <67> is a new object # the older objects are deleted by gc since their ref counts reach 0

#######################################################

# HOW GC WORKS WITH CLASS

## NORMAL REFERENCE
class CarWheels:
	def __init__(self, w):
		self.wheels = w

b = CarWheels(4) # ref count for object 'b' is 1
print(b.wheels)
print("b memory location :", hex(id(b)))

## WEAK REFERENCE
import weakref  # a module
r = weakref.ref(b) # this creates a weak reference for 'r' 
# ref count for object 'r' is 0
# the weak reference is linked with 'b' ref count
print("Before : ", r) # check the weak reference while ref count for 'b' is 1

b = None # 'b' is None # ref count for 'b' is 0
print("After : ", r) # the weak reference is dead after 'b' ref count is 0

#######################################################

# HOW GC WORKS WITH VARIABLES

a = 30  # <30> object is created
# ref count for <30> = 1

b = a   # <30> object is linked with 'b'
# ref count for <30> = 2

c = [b] # <30> object is linked with 'c'
# ref count for <30> = 3

del a # a is deleted # <30> object is no more linked or related with 'a'
# ref count for <30> = 2

b = 100 # <30> is unlinked with 'b' # <100> is linked with 'b'
# ref count for <30> = 1
# ref count for <100> = 1

c[0] = -8 # <30> is unlinked with 'c' # <-8> is linked with 'c'
# ref count for <30> = 0
# ref count for <-8> = 1
# <30> object is deleted by gc

#######################################################

## RELATED TOPICS - PRINTING DOCSTRING WITH GC

def docu():
	'''Python auto deletes values and objects if they're not used for enough time and it can be viewed through gc module.'''
	pass

print (docu.__doc__,'\n') # __doc__ calls documentation under the function Gcollect()

#######################################################
