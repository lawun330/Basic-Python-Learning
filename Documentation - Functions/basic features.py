'''This script documents lambda function, map(), filter(), @decorator, pass, yield, and recursions.'''

# LAMBDA FUNCTION

# it is a function that does not have a name or definition
# it is recommended to use lambda function for a single use

#########################################################

## USING MAP WITH LAMBDA FUNCTION

l = []
for x in range(0, 101):
	if x <= 50:
		l.append(x) # l=[1,2,3,..,50]

# example
s = list(map(lambda x: x * x, l)) # lambda function
# map() maps the 'a' and 'b' given two arguments (a, b) 
	# here, position of 'a' is lambda function
	# position of 'b' is any type of iterable # eg. b=[] or b=()
# list() lists the variables

#########################################################

## USING FILTER WITH LAMBDA FUNCTION

# map() is used with function
# filter() is used with equation
# map() feeds all iterables as arguments into function 
# filter() compares the true/false statement with iterables in equation, taking only iterables that make 'true'
def Filter():
	global f # variable 'f' can be used globally
	f = tuple(filter(lambda y: y % 5 == 0, s)) 
	g = set(filter(lambda x: x % 5 == 0, s))
	print('filtered =', f)
	print('filtered set =', g) # filter(func,iterable obj)

# example
Filter()

#########################################################

# DECORATOR

def decorator(func):  # decorating function
	def wrap(): # inner function
		print("==================") # can be replace with any decorations
		func()
		print("==================")
	return wrap # this calls the inner function

def square():
	print("0-50 square=", s)

# example
decoratedSquare = decorator(square) # square function is modified with decorator
decoratedSquare()

# the process is as follows-
# decoratedSquare() >> decorator(square)() >> decorator(square) + something 
	# decorator(square) >> wrap() >> ... >> square + () = square() >> ....

# alternatively decorator can be applied to a function by putting @decorator above that function
@decorator	# same as decorator(func)()
def anyFunction():
	a = 0
	def local():
		for i in enumerate(f):
			nonlocal a	# the 'a' below is the assigned local variable
			a += 1
	local()
	print("number of squares divisible by 5 is", a)
	return a

# example
anyFunction()

#########################################################

# USING PASS

def empty():	# this function has nothing aside from its name
	pass	# since function cannot really be empty, 'pass' statement is used

#########################################################

# USING YIELD

# 'yield' can be used as infinite generator since they don't store data
# 'yield' always replace the last values with new values until the for/while loop is False
# 'yield' doesn't delete the value, it just did not stored any values since the beginning
# that's why list() has to be used with 'yield' 
# values will be lost otherwise

# example functions - to generate prime numbers
def is_prime(a):
	for n in range(2,a):
		if a % n == 0:	# divide the last number with previous numbers excluding the last number itself as a denominator because i/i=1 and i%i=0
			return False
		else:
			if n == a - 1:	# reaches the end and still the number is not divisible
				return True

def prime_generator(x):
	num = 2
	yield 2
	while num < x: # prime begins with 2
		if is_prime(num) == True:
			yield num
		num += 1

# example
j = list(prime_generator(100)) # using list() to store the values from 'yield'
print('prime=', j)

##########################################################

# RECURSIVE FUNCTION 

# it is a function that calls itself
# there is always a base case in recursion
# a base case does not need another recursive activity

##########################################################

## RECURSION BETWEEN ONE FUNCTION

# example function - to generate factorials
# n! = n * (n - 1)! until base case is reached
	# eg. 5! = 5 * 4! until 5 becomes 1! (1! is 1)
def Factorial(z):
	if z == 1:  # base case condition
		return 1
	else:
		return z * Factorial(z - 1) # the function calls itself until z = 1 
		# if z = 1 -> base case condition

# example
Z = 7
print(f'{Z}! = {Factorial(Z)}')

##########################################################

## RECURSION BETWEEN TWO FUNCTIONS

# example - function to check if a number is even or odd
def is_even(x):
	if x == 0:
		return True
	else:
		return is_odd(x - 1) # even to odd - subtract one

def is_odd(x): # odd to even - put NOT
	return not is_even(x)

# example
print(is_odd(3))
# the process is as follows-
# is_odd(3) means-
# NOT is_even(3)
# NOT is_odd(2)
# NOT NOT is_even(2)
# NOT NOT is_odd(1)
# NOT NOT NOT is_even(1)
# NOT NOT NOT is_odd(0)
# NOT NOT NOT NOT is_even(0) >> NOT (NOT (NOT (NOT True))) -> True

###########################################################
