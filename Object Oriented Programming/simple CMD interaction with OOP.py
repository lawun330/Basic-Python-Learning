'''This script creates a simple CLI/CMD interaction using Object-Oriented Programming (OOP) concepts.
The script covers topics such as:
- Inheritance
- Class properties
- Class methods
- Class instances
- Class instance attributes
- Class instance methods
- Functions stored in an external dictionary
- Instances stored in an external dictionary
- Instances stored in an internal class dictionary

The script allows users to input commands to either "say" something or "find" an item. 
The items are represented as instances of subclasses that inherit from a main class.

# Commands:
- say
- find

# Example Usage:
- Say something: "say hello"
- Find an item: "find my pencil"
'''

########################################################################################

# main class
class Items:
	# declare class properties / attributes (predefined variables)
	parent_class_name = "Items"
	class_name = ""
	desc = ""
	str_to_instance_mappings = {} # a dictionary to map an item's name to its instance

	# SELF IS REPLACED BY AN INSTANCE

	# constructor function
	def __init__ (self, name): 
		self.name = name # parameter is set to "self.something"
		Items.str_to_instance_mappings[self.name] = [self]
		# ILLUSTRATION OF DIFFERENCE BETWEEN "self" and "self.something" WITH DICTIONARY
			## self.something -> parameter -> key of dictionary here
			## self -> <object instance> -> value of dictionary here	
				### {"some_input" : <object instance>} as self is replaced

	# method / behavior to get class properties / attributes (predefined variables)
	def getProperties(self):
		return f"The parent class is {self.parent_class_name}. The class name is {self.class_name} and it can {self.desc}. Also it is {self.new_subclass_variable}.\n"


# 1st subclass
class Pencil(Items):
	# add data to class properties / attributes (predefined variables)
	class_name = 'pencil'
	desc = 'write on things'
	
	# instance properties / attributes (not predefined variable) only for this subclass
	new_subclass_variable = 'a new pencil'

# 2nd subclass
class Ruler(Items):
	# add data to class properties / attributes (predefined variables)
	class_name = 'ruler'
	desc = 'measure things'

	# instance properties / attributes (not predefined variable) only for this subclass
	new_subclass_variable = 'a new ruler'

# 3rd subclass
class Eraser(Items):
	# add data to class properties / attributes (predefined variables)
	class_name = 'eraser'
	desc = 'erase written things'

	# instance properties / attributes (not predefined variable) only for this subclass
	new_subclass_variable = 'a new eraser'

########################################################################################

# create instance of subclasses
my_first_item = Pencil('my pencil') # argument goes into constructor function's parameters
my_second_item = Ruler('my ruler') # argument goes into constructor function's parameters
my_third_item = Eraser('my eraser') # argument goes into constructor function's parameters


# Inheritance of main class to subclasses
print("MAIN CLASS HAS THESE-")
print("-", Items.str_to_instance_mappings)
print()
print("SUBCLASSES HAVE THESE-")
print("-", my_first_item.str_to_instance_mappings)
print("-", my_second_item.str_to_instance_mappings)
print("-", my_third_item.str_to_instance_mappings)
print()
if (Items.str_to_instance_mappings == my_first_item.str_to_instance_mappings == my_second_item.str_to_instance_mappings == my_third_item.str_to_instance_mappings):
	print("Inheritance is working!")
else:
	print("No inheritance.")
print()


# store instances and their constructors' argument
valid_items = {"my pencil":my_first_item, "my ruler":my_second_item, "my eraser":my_third_item}

########################################################################################

# function to get user input and process it
def getInput():
	command = input('What do you want to say or find?: ') # get string input
	splitted_command = command.lower().split() # split the string into list of words
	verb_word = splitted_command[0] # get the verb (the first word)
	phrase_list = splitted_command[1:] # get the rest of the words
	phrase = ' '.join(phrase_list) # make a full string back from list

	# check the verb
	if verb_word in verb_dict:	# if valid as a dictionary key -> get corresponding function
		chosen_function = verb_dict[verb_word] # verb_dict dictionary[verb_word key] is a function
	else: # if not valid as a dictionary key -> return NOT RECOGNIZED
		print(f'COMMAND NOT RECOGNIZED - "{command}"\n')
		return

	# execute the function
	if len(command) >= 2 :
		print(chosen_function(phrase))

	# if nothing after the verb
	elif len(command) < 2:
		if 'say' in command:
			print('You said nothing.\n')
			return
		elif 'find' in command:
			print('You find nothing.\n')
			return


# function to say something # work without class
def sayFunction(something):
	return f'You said "{something}".\n'


# function to find something # work with class
def findFunction(something): # something refers to -> parameter 'name' -> self.name
	if something in valid_items:  # if a user finds constructor function's parameter
		# DESCRIBING DIFFERENT WAYS TO GET INSTANCE
		item_instance_from_subclass = valid_items[something] # from external dictionary
		item_instance_from_parent = Items.str_to_instance_mappings[something] # from dictionary inside parent class
		return Items.getProperties(item_instance_from_subclass) + "It is here >>> " + str(item_instance_from_parent) + "\n"
	else:
		return f"There is no {something} here.\n"


# dictionary to store the functions
verb_dict = {"say":sayFunction, "find":findFunction} # keys are inputs # values are functions

########################################################################################

# main function
if __name__ == '__main__':
	while (True):
		getInput()
