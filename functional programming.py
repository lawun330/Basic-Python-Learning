#related with functions and some of the use


l=[]
for x in range(0,101):
	if x<=50:
		l.append(x)
		#l=[1,2,3,..,50]
s=list(map(lambda x: x*x ,l)) #lambda is a function undefined #use as one use function
#map maps the x and y in (x,y) where x=function() and y is any type of iterable .ie.for eg y=[] or y=()
#list() lists the variables
def Filter(): 		#filter function
	global f
	f=tuple(filter(lambda y: y%5==0,s)) #map is used with function and filter is used with equation
	print(f)

def decorator(func):  #decorating function 
	def wrap():
		print("==================") #can be replace with any decorations
		func()
		print("==================")
	return wrap
	
def square():
	print("0-50 square=",s)
    
decoratedSquare=decorator(square) #square function is modified with decorator
decoratedSquare()
 
#The above function procedures is-
#decoratedSquare() >> decorator(square)() >> decorator(square) + something // decorator(square)>> wrap() >> ...>>square + ()=square() >> ....

#another way of decorating 
def decor2(func):
	def wrap2():
		print("***********")
		func()
		print("***********")
	return wrap2


@decor2  #same as decor2(haha)() #must be above the prefer function 
def haha():
	a=0
	def local():
		for i in enumerate(f):  
			nonlocal a   #the following 'a' is the same as assigned local variable
			a+=1
	local()
	print("number of squares divisible by 5=",a)
	return a

Filter()
haha()
#########################################################

def empty(): #this function has nothing aside from name
	pass	#since function cannot really be empty >>pass statement is used


#generator function #for prime numbers
def is_prime(a):
	for n in range(2,a):
		if a%n==0: 
			return False
		else: 
			if n==a-1:
				return True

def prime_generator(x):
	num=2
	yield 2
	while num<x:
		is_prime(num)
		if is_prime(num)==True:
			yield num 			#return the value to the function()
		#yield can be used as infinite anything generator since they are one use ie.they don't store data
		#yield always replace the last values with new values until the for/while is False 
		#yield don't delete the value, it doesn't stored values since beginning
		num+=1

j=list(prime_generator(100)) #that's why it has to be listed
print('prime=',j)
##########################################################

#recursive function - function that calls itself 
#base on n!=n*(n-1)! until base case is reached>>> eg-5!=5*4!  until 5 becomes 1! which is 1 
def Factorial(z):
	if z==1:  #base case (a base that doesn't need another call of function)
		return 1
	else:
		return z*Factorial(z-1) #the function calls itself until z=1, when z=1, if statement(base case) is worked
z=7
print('{0}! ={1}'.format(z,Factorial(z)))

#recursion between two functions
def is_even(x):
	if x==0:
	 return True
	else:
	 return is_odd(x-1)

def is_odd(x):
	return not is_even(x)
#is_odd(3) means-
#NOT is_even(3)
#NOT is_odd(2)
#NOT NOT is_even(2)
#NOT NOT is_odd(1)
#NOT NOT NOT is_even(1)
#NOT NOT NOT is_odd(0)
#NOT NOT NOT NOT is_even(0) >> NOT (NOT (NOT (NOT True)))) >>True

#odd to even - put NOT, even to odd - subtract one

print(is_odd(3))
###########################################################
p=(3,4,5,6) 
#filter the iterables' elements
print(set(filter(lambda x: x%3==0,p))) #filter(func,iterable obj)