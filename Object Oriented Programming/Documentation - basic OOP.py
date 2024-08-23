'''This script provides a comprehensive overview of Object-Oriented Programming (OOP) concepts.
It includes explanations and examples of:
- Classes and Instances
- Class Attributes
- Polymorphism
- Inheritance
- Multilevel Inheritance
- Magic Methods and Operator Overloading
- More Magic Methods
- Special Attributes
- Instance Methods
- Class Methods
- Static Methods
- Data Hiding
  * Strongly Private Data
  * Weakly Private Data
- Data Encapsulation
  * Properties
  * Getter and Setter Methods
'''

########################################################################################

# CLASS
## STRUCTURE
	## class Anyname: 
	##     def __init__(self, attribute1, attribute2, ...) <- constructor method
	##     def custom_method(self): <- other method(s)
	##     def custom_method(self):
	##     ...
class Arduino:
	# __init__ means using class as a function, called a class constructor
	def __init__ (self, version, hardware):	# constructor method
		self.version = version  			# self.attribute1
		self.hardware = hardware			# self.attribute2
	
	def custom_method(self):  				# other method(s)
		print("My arduino is")

	variable = 'learned at 2019'			# class attribute
		# share with all instances of class 
		# related to class itself and instances of the class


# INSTANCE
## STRUCTURE
	## instance_name = class_name(attribute1, attribute2, ...) <- class instantiation
	## instance_name.defined_method() <- method calling
	## instance_name.attribute <- accessing class attributes
my_arduino = Arduino(1.8, 'uno')  
	# instance -> relate the variable 'my_arduino' to the whole class
	# my_arduino replaces self in class parameters
my_arduino.custom_method()  # methods has procedures
print(my_arduino.hardware)	# attributes are informations
print(my_arduino.version)	# attributes are informations


# DEMONSTRATION OF HOW CLASS ATTRIBUTES ARE SHARED WITH ALL INSTANCES OF CLASS
print(my_arduino.variable)	# accessing class attribute through instance
print(Arduino.variable)		# accessing class attribute directly
if my_arduino.variable == Arduino.variable:
	print("They are the same!")
else:
	print("They are different!")
print()

########################################################################################

# POLYMORPHISM
## it is the ability of something to have or to be displayed in more than one form
## superclass methods can be overriden in each subclass
## the method with the same name acts differently according to the subclass definition

# superclass 'Animal'
class Animal: # superclass / parent class / main class
	def __init__(self, name, color): # constructor method
		self.name = name
		self.color = color
	def voice(self): # method
		print("Hey!")
person = Animal('David','white') # instance of a class 'Animal', a white person named "David" 
print(person.name, person.color) # accessing class attributes through instance
person.voice() # calling method through instance

# a subclass 'Dog' inherits from 'Animal'
class Dog(Animal): # subclass / child class / inherited class
	def voice(self): # override the above method
		print("Woof!")
shiba = Dog('Buddy', 'golden') # instance of a subclass 'Dog', a golden shiba named "Buddy"
print(shiba.name, shiba.color) # accessing class attributes through instance
shiba.voice() # calling method through instance


# INHERITANCE
## attributes and methods of superclass are inherited to subclass
	## superclass <- subclass
	## superclass.method() <- subclass.method()
	## superclass.attribute <- subclass.attribute
## attributes and methods of subclass are not shared with superclass or any other subclasses

# a subclass 'Cat' inherits from 'Animal'
class Cat(Animal): # subclass / child class / inherited class
	def purr(self): # introduce a new method in this subclass
		print("Meow!")
tom = Cat('Tom', 'blue') # instance of a subclass 'Cat', a blue cat named "Tom" # YES, IT IS FROM TOM & JERRY :)
print(tom.name, tom.color) # accessing class attributes through instance

# DEMONSTRATION OF HOW A SUBCLASS INHERITS FROM SUPERCLASS' ATTRIBUTES AND METHODS
## there is no polymorphism for this subclass, i.e., this subclass does not override the method, unlike 'Dog'
## the method from the parent class gets called since it is inherited
tom.voice() # no override -> default parent-class method -> return 'Hey!'

# DEMONSTRATION OF HOW A SUBCLASS' ATTRIBUTES AND METHODS ARE INACCESSIBLE FROM SUPERCLASS AND SIBLING CLASSES
## the purr() method is only defined in subclass 'Cat'
## this method is not shared with the parent class or other subclasses (sibling classes of 'Cat')
## calling this method through instance of superclass or sibling class will raise an error
tom.purr() # calling a newly defined method through instance
try:
	person.purr() # calling this new method through instance of superclass
except:
	print("David from parent class cannot purr!")
try:
	shiba.purr() # calling this new method through instance of another subclass 'Dog' (a sibling class of 'Cat')
except:
	print("Shiba from sibling class cannot purr!")
print()

########################################################################################

# MULTILEVEL INHERITANCE
## a parent class can create multiple subclasses, each of which can create their own subclasses
## thus, there is the main parent class; and each subclass are parent class of their own subclasses
## this is a chain of inheritance
## Note: circular inheritance (last child class is a parent of the main parent class) is impossible

class Parent:
	def method1(self):
		print('parent')
	def parent_method(self):
		print('another parent method')

class FirstLevel(Parent):
	def method2(self):
		print('first level')
	def first_child_method(self):
		print('exclusive first child method')

class SecondLevel(FirstLevel):
	def method3(self):
		print('second level')

class ThirdLevel(SecondLevel):
	def method4(self):
		print('third level')
		
		# super() is used to find certain method in superclasses (the main parent class and parent subclasses)
		super().parent_method()  # method of the main parent class
		super().first_child_method()  # method of the parent subclass

# calling methods from the last-inherited-class instance
testing = ThirdLevel() #  last-level-of-inheritance-class instantiation
testing.method1() # the main parent-class method
testing.method2() # the first-level-of-inheritance-class method
testing.method3() # the second-level-of-inheritance-class method
testing.method4() # the last-level-of-inheritance-class method

# DEMONSTRATION OF HOW MULTILEVEL INHERITANCE WORKS
print(ThirdLevel.__bases__) # the base of ThirdLevel() is SecondLevel()
print(SecondLevel.__bases__) # the base of SecondLevel() is FirstLevel()
print(FirstLevel.__bases__) # the base of FirstLevel() is Parent()
print(Parent.__bases__) # this is the base # returns the <class 'object'>
print()

########################################################################################

# MAGIC METHODS / OPERATOR OVERLOADING
## magic methods, or dunder methods, allow us to define the behavior of our objects with respect to built-in operations such as addition, subtraction, and comparison.
## by overloading these operators, we can customize how our objects interact with each other and with Python's built-in functions.
## overloading = changing the behavior of the operator = rewriting the operator method
## these methods are called automatically when the corresponding operator is used
## these methods are also called magic methods because their names start and end with double underscores
	# Example: __add__ refers to + (addition), but it can be overloaded to print the subtraction of two numbers

# EXAMPLE OF ENHANCING THEIR FUNCTIONALITY
## this class overloads magic operators to operate between two pairs of numbers, rather than two numbers
class operations:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __add__(self, other):
		return (self.first + other.first, self.second + other.second)

	def __sub__(self, other):
		return (self.first - other.first, self.second - other.second)

	def __mul__(self, other):
		return (self.first * other.first, self.second * other.second)

	def __truediv__(self, other):
		return (self.first / other.first, self.second / other.second)

	def __floordiv__(self, other):
		return (self.first // other.first, self.second // other.second)

	def __mod__(self, other):
		return (self.first % other.first, self.second % other.second)

	def __pow__(self, other):
		return (self.first ** other.first, self.second ** other.second)

	def __and__(self, other):
		return (self.first & other.first, self.second & other.second)
			# return the first and second of self

	def __xor__(self, other):
		return (self.first ^ other.first, self.second ^ other.second)
			# return absolute differences of self and other

	def __or__(self, other):
		return (self.first | other.first, self.second | other.second)
			# return the first and second of other

	def __lt__(self, other):
		return (self.first < other.first, self.second < other.second)
			# return True/False

	def __le__(self, other):
		return (self.first <= other.first, self.second <= other.second)
			# return True/False

	def __eq__(self, other):
		return (self.first == other.first, self.second == other.second)
			# return True/False

	def __ne__(self, other):
		return (self.first != other.first, self.second != other.second)
			# return True/False

	def __gt__(self, other):
		return (self.first > other.first, self.second > other.second)
			# return True/False

	def __ge__(self, other):
		return (self.first >= other.first, self.second >= other.second)
			# return True/False

fir = operations(3, 6) # first pair of numbers
sec = operations(2, 4) # second pair of numbers
print(fir + sec) # '+' = __add__(s,o) = overloaded magical operator method
print()

########################################################################################

# MAGIC METHODS / OPERATOR OVERLOADING
# EXAMPLE OF CREATING A DIFFERENT FUNCTIONALITY
## this class overloads two magic operators to perform functions different from their original purposes
## Note: this can create confusion 
class SpecialStr:
	def __init__(self, string):
		self.string = string

	# '/' operator should divide numbers -> overload -> now it returns custom messages
	def __truediv__(self, other):
		design = '^' * len(other.string) # output is ^^^...
		return '--'.join([self.string, design, other.string]) # return 3 values # '--' is joined after each value

	# '>' operator should perform 'greater than' operation -> overload -> now it prints custom messages 
	def __gt__(self, other):
		for i in range(len(other.string) + 1):	# range(16+1) / 17 loops / 17 iterations
			ans = other.string[:i] + '*' + self.string 	# cut the string -> [from start : to i-th char]
			ans += '*' + other.string[i:]				# cut the string -> [from i-th char : to end]
			print(ans, i)

mommy = SpecialStr('eating donaut') # len() = 13
baby = SpecialStr('playing football') # len() = 16
print(mommy / baby) # '/' = __truediv__(s,o) = overloaded magical operator method
mommy > baby # '>' = __gt__(s,o) = overloaded magical operator method
print()

########################################################################################

# MORE MAGIC METHODS

# __len__ 
	## magic method for len()
# __getitem__ 
	## magic method for indexing
# __setitem__ 
	## magic method for assigning values to indexed positions
	## 'x[y] = z' is equal to 'x.__setitem__(y,z)'
# __delitem__ 
	## magic method for deleting indexed values 
	## 'del object[index]' is equal to 'object.__delitem__(index)'
# __iter__ 
	## magic method to make an object iterable 
	## eg. in for loop
# __contains__ 
	## magic method for 'in' keyword, and membership test operations
# __repr__ 
	## magic method for string representation of the instances
	## can be used to return the type of object with 'self.__name__' 
	## eg. <class>, <list>, ...

########################################################################################

# SPECIAL ATTRIBUTES
## special attributes are used to return information about the class or instance
## these attributes are not called like methods, but accessed like variables

# __class__ 
	## special attribute to return the class of an instance
	## eg. 'instance.__class__' is 'ClassName' in 'instance = ClassName(arg)'
# __name__ 
	## special attribute that indicates the module name
	## set to '__main__' if a script is not imported
	## set to 'imported module name' if a script is imported
# __main__ 
	## special attribute for the name of the top-level environment where the script is run
	## also known as the main program
	## ensure it executes only when the file is intentionally run directly as a script or application
# __doc__ 
	## special attribute to return the documentation, usually written in class or function
# __module__ 
	## special attribute to return the module name in which a class is defined 
	## 'Classname.__module__' 
		## returns '__main__' if the class is defined in interactive mode
# __bases__ 
	## special attribute to return the immediate parent class (base class) in multilevel inheritance
# __all__ 
	## special attribute to define the public interface of the module
	## specifying which things (a list of strings) should be imported when 'from <module> import *' is used
# __dict__ 
	## special attribute containing the class' namespace
	## store the class' or instance's attributes and methods

########################################################################################

# MAGIC METHODS / OPERATOR OVERLOADING + SPECIAL ATTRIBUTES
# EXAMPLE OF CREATING A DIFFERENT FUNCTIONALITY

import random

## this class overloads magic operators to perform functions different from their original purposes
class  CustomList:
	def __init__(self, context):
		self.context = context

	# 'list[index]' should return corresponding value -> overload -> now it returns random value
	def __getitem__(self, index):
		return self.context[index + random.randint(-1, 1)]
	
	# 'len()' should return the length of the list -> overload -> now it returns random value
	def __len__(self):
		return random.randint(0, len(self.context) * 2)

	# 'del' should delete the specified indexed value -> overload -> now it returns the random indexed value
	def __delitem__(self, index):
		print("Hello world!")

some_list = CustomList(["A", False, "Car", 9]) # the whole list is a set

print("custom len(): ", len(some_list)) # 'len()' = __len__(s) = overloaded magical operator method
print("custom len(): ", len(some_list))

print("custom indexing: ", some_list[2]) # 'list[index]' = __getitem__(s,i) = overloaded magical operator method
print("custom indexing: ", some_list[2])

print("input list before custom del: ", some_list.context) # ["A", False, "Car", 9] is the assigned data in self.context
del some_list.context[2] # 'del' = __delitem__(s,i) = overloaded magical operator method
print("input list after custom del: ", some_list.context)

# USING SPECIAL ATTRIBUTES TO GET NAMESPACES
## namespaces are all the attributes and methods defined in the 'CustomList' class
	## key -> name of attribute or method 
	## value -> that attribute or method itself
	## eg. '__init__':<something>, '__getitem__':<something>, '__len__':<something>, '__delitem__':<something>, ...
print(CustomList.__dict__)

# USING SPECIAL ATTRIBUTES '__name__' and '__main__'
## if the script is run directly, the '__name__' attribute is set to '__main__'
if __name__=='__main__':
	print ('File is running directly')
print()

########################################################################################

# DATA HIDING

class MyanmarCountry:
	__ethnic_groups = 'Kachin Kayar Kayin Chin Burma Mon Rakhine Shan' # double underscores -> strongly private
	__ethnic_groups_as_list = __ethnic_groups.split(' ')
	
	def __init__(self, year_of_independent):
		self._year_of_independent = year_of_independent # single underscore -> weakly private

	def getPeople(self):
		print(self.__ethnic_groups)

mm = MyanmarCountry(1948)

# WEAKLY PRIVATE DATA
## it is easy to access single underscore variables' data directly
## but data is not accessible with 'from module import *'
print("Weakly private data: ", mm. _year_of_independent)

# STRONGLY PRIVATE DATA
## data is not accessible with an instance of the class alone
## the name of the class is needed to access the data
print("Strongly private data: ", mm._MyanmarCountry__ethnic_groups_as_list) # instance._className__strongly-private-variableName
## data is accessible with an instance of the class alone <- only if there is a method that returns the data
mm.getPeople() # the method 'getPeople()' returns the strongly private data

# DEMONSTRATION OF HOW STRONGLY PRIVATE DATA IS NOT ACCESSIBLE WITH AN INSTANCE OF THE CLASS ALONE
try:
	print(mm.__ethnic_groups)  # raise attribute error because this data is strongly private
except AttributeError:
	print('Strongly private data is not accessible with an instance of the class alone!')
print()

########################################################################################

# 3 TYPES OF METHOD IN CLASS
# CLASS METHOD VS. STATIC METHOD

## this class implements 3 types of method
## for comparison, the area is calculated with the same width and height
class RectangleArea:
	side = 4 # class attribute

	# constructor
	def __init__(self, width, height):
		self.width = width
		self.height = height

	# define normal method
	def normalArea(self):
		return self.width * self.height

	# define class method
	@classmethod
	def classArea(cls, width1, height1):
		cls.width = width1
		cls.height = height1
		return cls.width * cls.height

	# define static method
	@staticmethod
	def staticArea(width2, height2):
		return width2 * height2

rectangle_instance = RectangleArea(2, 4) # instance of a class
print('Area with normal method: %d, Area with class method: %d, Area with static method: %d'
	   % (rectangle_instance.normalArea(), RectangleArea.classArea(2, 4), RectangleArea.staticArea(2, 4)))
print()

# DIFFERENCES

## NORMAL METHOD is called by an instance of the class
## this type should be used: when data belongs to instance; to access instance-level attributes;
## this type needs an instance
	## instance_name.normal_method() -> rectangle_instance.normalArea() -> normalArea() -> a normal method

## CLASS METHOD is called by a class name
## this type should be used: when data belongs to class; to modify class-level attributes;
## this type needs no instance
	## the class name is passed to the parameter 'cls'
	## class_name.class_method(parameters) -> RectangleArea.classArea(2, 4) -> classArea(x,y) -> a class method

## STATIC METHOD is called by a class name
## this type should be used: no need to access instance-level attributes; no need to modify class-level attributes;
## this type needs no instance
	## class_name.static_method(parameters) -> no self or class parameter -> RectangleArea.staticArea(2, 4) -> staticArea(x,y) -> a static method

########################################################################################

# DATA ENCAPSULATION
# PROPERTIES 
	## it is a read-only data
	## it looks like a variable but it is a function (read-only)
	## data cannot be changed 

class Number:
	@property
	def fixed_num(self):
		return '101010'

binary1 = Number()
print(binary1.fixed_num)	
	# normally it is binary.fixed_num() but here '()' is unnecessary
	# you don't need '()' because of @property
try:
	binary1.fixed_num = '202020' # try to modify data
except AttributeError:
	print("Error rewritting data")


# DATA ENCAPSULATION
## SETTER AND GETTER
	## setter sets(changes) the property's value, with @moduleName.setter
	## getter gets(retrieves) the property's value, with @property

class Number2:
	def __init__(self, num): # get the number from instance initiation and store in variable
		self.input_num = num

	# getter function
	@property
	def fixed_num(self): # return the value of the variable
		return self.input_num
	
	# setter function
	@fixed_num.setter
	def fixed_num(self, new_num):	# modify that variable
		self.input_num = new_num

binary2 = Number2('101010')
print(binary2.fixed_num)
	# normally it is binary2.fixed_num() but here '()' is unnecessary
	# you don't need '()' because of @property
try:
	binary2.fixed_num = '202020' # try to modify data
	print(binary2.fixed_num)
except AttributeError:
	print("Error rewritting data")
print()

########################################################################################
