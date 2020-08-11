#class Anyname: def __init__(Anyvar,attribute1,attribute2)  #__init__ means using class as function, called class constructor
class arduino:
	def __init__ (self,version,hardware):	#usually written as self in Anyvar #method
		self.version=version  				#self.attribute1
		self.hardware=hardware

	def meth1(self):  						# another methods
		print("My arduino is")

	l='learned at 2019'						#class attributes are share with all instances of class #related with class itself and instance of the class


my_arduino=arduino(1.8,'uno')  #>>>>relate the name 'my_arduino' to the whole class  
#instance of class is my_arduino #my_arduino replaces self
my_arduino.meth1()							#calling methods #methods has procedures  #name.method()
print(my_arduino.hardware)
print(my_arduino.version)					#name.attribute #attributes are informations

print(my_arduino.l)							#instances of class.attribute
print(arduino.l)							#class.attribute  

print('\n')

############################


#inheritance

class Animal:
	def __init__(self,name,color):	#related with whole class 
		self.name=name
		self.color=color

	def bark(self):					#method
		print("hahaha")

#>>>>relate the name 's' to the whole class 		
s=Animal('man','red')
print(s.name,s.color)
s.bark()
print("\n")

#creating a new class Dog inheriting from Animal
class Dog(Animal):					#related with class constructor and inherited class or subclass itself
	def bark(self):					#same method name overwrites 
		print("Woof!")

dopamin=Dog('wallet','black')
print(dopamin.name,dopamin.color)
dopamin.bark()
print('\n')

class Cat(Animal):							
	def purr(self):
		print("Meow")

#>>>>relate the name 'tom' to the subclass 
tom=Cat('Tom','blue')	#inserting the name tom with 2 arguments in class Cat which is under class Animal 
#now 2 args are related with superclass Animal and name is related with both superclass and subclass

print(tom.name,tom.color)
tom.purr()
print('\n')
############################


#inheriting from subclasses

class alphabet:
	def method1(self):
		print('AA')

	def x(self):
		print('xoxo')

class A(alphabet):
	def method2(self):
		print('BB')

	def h(self):
		print('hoho')

class B(A):
	def method3(self):
		print('CC')

class C(B):
	def method4(self):
		print('DD')
#super() is used to find certain method in superclass and parent subclasses
		super().h()  #find in parent subclasses
		super().x()  #find in superclass

haha=C()
haha.method1()
haha.method2()
haha.method3()
haha.method4()

print(C.__bases__) #the base of C() is B() 
print(B.__bases__) #the base of B() is A()
print(A.__bases__) #the base of A() is alphabet()
print(alphabet.__bases__) #this is the base #returns the <class 'object'>

#circular inheriting is impossible
############################



#magic method #operator overloading

class operations:
	def __init__(self,first,second):
		self.first=first
		self.second=second

	def __add__(self,other):
		return (self.first+other.first , self.second+other.second)

	def __sub__(self,other):
		return (self.first-other.first , self.second-other.second)

	def __mul__(self,other):
		return (self.first*other.first , self.second*other.second)

	def __truediv__(self,other):
		return (self.first/other.first , self.second/other.second)

	def __floordiv__(self,other):
		return (self.first//other.first , self.second//other.second)

	def __mod__(self,other):
		return (self.first%other.first , self.second%other.second)

	def __pow__(self,other):
		return (self.first**other.first , self.second**other.second)

	def __and__(self,other):
		return (self.first&other.first , self.second&other.second)
		#return the first and second of self

	def __xor__(self,other):
		return (self.first^other.first , self.second^other.second)
		#return absolute differences of self and other

	def __or__(self,other):
		return (self.first|other.first , self.second|other.second)
		#return the first and second of other

	def __lt__(self,other):
		return (self.first<other.first , self.second<other.second)
		#return True/False

	def __le__(self,other):
		return (self.first<=other.first , self.second<=other.second) 
		#return True/False

	def __eq__(self,other):
		return (self.first==other.first , self.second==other.second)
		#return True/False

	def __ne__(self,other):
		return (self.first!=other.first , self.second!=other.second)
		#return True/False
	
	def __gt__(self,other):
		return (self.first>other.first , self.second>other.second)
		#return True/False
	
	def __ge__(self,other):
		return (self.first>=other.first , self.second>=other.second)
		#return True/False

fir=operations(3,6)
sec=operations(2,4)
total=fir+sec  #add the class' objects using __add__(magic method)
print(total)

#more uses of magic methods
class SpecialStr:
	def __init__(self,string):
		self.string=string

	def __truediv__(self,other):
		design= '^' * len(other.string) #output is ^^^...
		return '--'.join([self.string,design,other.string])
		#returning 3 values, '--' is joined after each value

	def __gt__(self,other):
		for i in range(len(other.string)+1): #range(13) /13 loops/ 13 iterations
			ans=other.string[:i]+'*'+self.string  #cut the string [from start : to i-th char]
			ans+='*'+other.string[i:]				#[from i-th char : to end]
			print(ans,i)

sex=SpecialStr('eating donaut')
baby=SpecialStr('killing insects')

print(sex/baby) # / is equal to __truediv__(s,o) #method calling

sex>baby #recall the method __gt__

#more magic methods

#-------------> __len__ for len()
#-------------> __getitem__ for indexing
#-------------> __setitem__ for assigning index values eg- x[y]=z  x.__setitem__(y,z)
#-------------> __delitem__ for deleting indexed values (USE del func)
#-------------> __iter__ for iteration over objects (eg. in for loop)
#-------------> __contains__ for 'in' keyword 
#-------------> __type__ returns the type of obj (eg. class,list,etc)
#-------------> __class__ for returning the class of the  (eg. name=ClassName(etc) then name.__class__ is ClassName)
#-------------> __name__ variable is set to __main__ if module is not imported otherwise it is set to the imported module name
#-------------> __main__ refers to the main module i.e,executed file is not imported from another module or file
#-------------> __doc__ returns the documentation in class or function
#-------------> __module__ module name in which class is defined (__main__ in interactive mode) (as line 197,198)
#-------------> __bases__  (line 92)
#-------------> __all__ - a list of strings (each can be a name of variable) to be exported when --> from <module> import * <-- is used. eg. pi from math
#-------------> __dict__ dictionary containing class' namespace (line 231)
#-------------> __repr__ for string representation of the instances
import random

class  vaguelist:
	def __init__(self,context):
		self.context=context

	def __getitem__(self,index):
		return self.context[index+random.randint(-1,1)]
		#return the value of the random index in a list, like overriding the original indexing function

	def __len__(self):
		return random.randint(0,len(self.context)*2)
		#return the random number as len(), like overridding the original len() function

	def __delitem__(self,index):
		del self.context[index]
		print (self.context[index])

List=vaguelist(["A","B","Car",9]) #the whole list is set , not individual (as line 230)

print(len(List))	#len() is calls to __len__
print(len(List))

print(List[2])		#AnyList[index] calls to __getitem__
print(List[2])

print(List.context) 	#print the assigned data in self.context
del List.context[3]		#del calls to __delitem__
print(List.context)  

#namespaces are eg- '__init__','__getitem__','__len__','__delitem__' .,etc 
print(vaguelist.__dict__) #key is namespace of class and value is that method of the namespace


if __name__=='__main__':
	print ('File is running directly\n')

#############################

#object Lifecycle
#garbage collection in other file
#############################

#data hiding

class YourName:
	__myanmar='Lawun'  #double underscores are strongly private
	__asList=__myanmar.split(' ')
	def __init__(self,age):
		self._age=age #single underscore is weakly private

	def Name(self):
		print(self.__myanmar)

me=YourName(18)

#can access single underscore datas #_variables cannot be used with --> from module import * <--
print(me._age) #print age

#ways to access double underscores datas
me.Name() #same as print(me._YourName__myanmar)
print(me._YourName__asList) #print in list 

try:
	print(me.__myanmar)  #raise attribute error because data is private
except AttributeError :
	print('Error jumped')

#############################


#Class and Static methods
#3 types of class methods

class R3ctangle:
	
	side=4 #class attribute (goto line 310)

	def __init__(self,width,height):
		self.width=width
		self.height=height

	@classmethod #this method will be class method
	def area(cls,width1,height1):			#A1
		return width1 * height1

	def Area(self):	#normal method			#A2
		return self.width * self.height

	@staticmethod #static method
	def AREA(width,height):
		return width * height


#NOTE>>>>>rectangleA1.side is equal to R3ctangle.side
#>>>>>class attributes can be used with instances and class

rectangleA1=R3ctangle(2,4) #instance of a class, passed to the self parameter and use the methods

#class method is called by class, passed to the cls parameter

print('A1 %d A2 %d A3 %d\n'% (rectangleA1.Area(),R3ctangle.area(2,4),R3ctangle.AREA(2,4)))

#differences

#--class.method(parameters) => R3ctangle.area(2,4) >>> .area(x,y) is class method
#should use when data belongs to class

#--instance.method() => rectangleA1.Area() >>> .Area() is method called by instance of a class
#should use when data belongs to instance

#--class.method() => no self or class parameter, no need instance mentioning >>> static method
#doesn't belong to any of the data of instance or class
#pieces of code attached to the class


#############################

#properties or data encapsulation

class Num:
	@property
	def fixed_num(self):
		return '101010'

binary=Num()
print(binary.fixed_num)	#normally it is binary.fixed_num() but here '()' is unnecessary
#it looks like a variable but still it is a function but it can be read-only 
#NOT AVAILABLE to change as usual and you don't need '()' 

#trying to change the data as usual
try: 
	binary.fixed_num='202020'

except AttributeError:
	print("error rewritting\n")

#cannot change the data as usual
#can be used in restrictions (eg- 18+)
#--------------------------------------

#****setter and getter ****
#setter sets(changes) the property's value  ie. @moduleName.setter
#getter gets the value, it is written in system => you only need @property

#example-
class digital:
	
	def __init__(self,num): #get the number from instance initiation and save in variable
		self.bin=num

	@property
	def bi(self):			#always return value of the variable 
		return self.bin
		
	@bi.setter
	def bi(self,newNUM):	#save a new number in a variable
		self.bin=newNUM

my_num=digital('111000') #insert number
print(my_num.bi)
my_num.bi='303030' #rewrite it
print(my_num.bi)
#############################