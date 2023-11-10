#making function as arguments
#changing values of variable arguments with argumental positions

def func1(x,y):
    return x+y
def func2(c,d):
    return c-d
def func3(anyfunc,e,f):  #call any required function in the position of anyfunc
    return anyfunc(anyfunc(e,f),anyfunc(e,f))  #(x,y)
a=3
b=6

print(func3(func1,a,b)) #2(a+b) results # func1(func1(a+b),func1(a+b))
print(func3(func2,a,b)+1)  #this will print 1 since any (a-b)-(a-b) is zero
print('\n')
###################################################

#function and uncontrolled or varying number of arguments

def func4(parameter1,*Xparameters):
	print(parameter1,'+',Xparameters)

func4('arg1','arg2','arg3','arg4','arg5') 
#when arguments are much greater than parameters, the remaining args are stored in *paras as in tuple

#compared it to tuple
a, b, c, *d, e= (1, 2, 3, 4, 5, 6, 7, 8)
print(*d,'\n') #*d has 4 values
###################################################

#default values in function

def func5(x,y,name='haha'):
	print(x,name,y)

func5(4,'LOLs') #if no args are put, default value is returned
func5(4,'LOLs',name='hehe') #arg is put and the origin arg is changed

#compared it to class
class Class():
	def __init__(self,name='ROFL'):
		self.name=name

print(Class().name) #if no args are put, default value is returned

class5=Class('LMAO')

print(class5.name) #arg is put and return that arg

#the default arg should be followed after non-default args eg. 
def func6(para1,para2,*paras,para='PARA'):
	pass
print('\n')
####################################################

def func7(para1,para2,*arg,**kwarg):
	print(kwarg)

func7(1,2,3,4,6,7,8,lol=3,nolol=5)
#para1 = 1 
#para2 = 2 
#*arg  = 3 to 8 in tuples = (3,4,5,6,7,8)
#**kwarg (called keyword argument) = dictionary with name and value = {'lol':3, 'nolol'=5}
