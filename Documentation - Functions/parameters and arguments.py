'''This script documents the utility of Python functions, parameters, and arguments.'''

# FUNCTION AS AN ARGUMENT

def func1(x, y):
    return x + y
def func2(c, d):
    return c - d
def func3(anyfunc, e, f):  # call a function as in the position of anyfunc
    return anyfunc(anyfunc(e, f), anyfunc(e, f))

# example
a = 3
b = 6
print(func3(func1, a, b)) # print the value of 2(a+b)
print(func3(func2, a, b)) # print 0 since any (a-b)-(a-b) is zero
print()

###################################################

# UNLIMITED (VARYING NUMBERS OF) PARAMETERS, *args

def func4(parameter1, *Xparameters):
	print(parameter1, '+', Xparameters)

func4('arg1', 'arg2', 'arg3', 'arg4', 'arg5')
# when the number of arguments are greater than that of parameters, 
# the remaining args are stored in *parameters
# compared it to tuple functionality
a, b, c, *d, e = (1, 2, 3, 4, 5, 6, 7, 8)
print("*d =", *d, '\n') # *d has 4 values

###################################################

# PREDEFINED ARGUMENTS

def func5(x, y, name = 'haha'):
	print(x, name, y)

func5(4, 'LOLs') # no argument -> apply default
func5(4, 'LOLs', name = 'hehe') # an argument -> overwrite default

# compared it to class
class Class:
	def __init__(self, name = 'ROFL'):
		self.name = name
print(Class().name) # no argument -> apply default
class5 = Class('LMAO')
print(class5.name) # an argument -> overwrite default

## STRUCTURE
# good code is the one where default arg is defined after placeholder parameters # eg.
def func6(para1, para2, *paras, para = 'PARA'):
	pass
print()

####################################################

# INTRODUCING **kwargs

def func7(para1, para2, *arg, **kwarg):
	print(kwarg)

func7(1, 2, 3, 4, 6, 7, 8, lol=3, nolol=5)
# para1 is 1
# para2 is 2
# *arg is 3 to 8 in tuples -> (3,4,5,6,7,8)
# **kwarg (called keyword argument) is a dictionary with name and value -> {'lol':3, 'nolol'=5}

####################################################
