''' #### DEFEAT THE EVIL GAME ####
This script implements Object-Oriented Programming (OOP) concepts and creates a simple game via CLI/CMD.
It illustrates the following concepts:
- class variables
- inheritance
- constructor function of parent class
- constructor function of child class
- super()
- property function
- polymorphism
- type annotation
- custom class type checking
- user input
- function dictionary

This script creates a single type of evil boss: the ghost.
Multiple evil bosses can be created by defining more subclasses.

Multiple ghosts can be created by creating more instances of the Ghost subclass.
This script creates three ghosts: 
	- Hellen;
	- Murphy;
	- Simon.

Multiple evil bosses can be killed in multiple ways by defining more functions with a type check.
This script only implements one way to kill all evils: by reducing 1 HP per attack.
The goal is to kill all evil bosses.

# Commands:
- how
- attack
- check

# Example Usage:
- Know how a specific character would attack you: "how ghost murphy"
- Attack a character: "attack ghost helen"
- Check HP: "check ghost simon"
'''

########################################################################################

# main class for all evil bosses
class EvilBosses:
	# class variables
	class_name = ""
	desc = ""
	objects = {}
		# structure to store in 'objects'
		## {"ghost":[<Ghost 1 instance>, <Ghost 2 instance>, ...], "Other Boss":[instance, instance, ...], ...}
	placeholder_list = []

	# constructor function of parent class
	def __init__ (self, name):
		self.name = name
		EvilBosses.objects[self.class_name] = self.placeholder_list # create a new list for every child class

	# method from the parent class
	def getAttacked(self):
		return f"Evil boss attacks you!" # this string gets overriden

########################################################################################

# INHERITANCE example
# define a subclass for a ghost character
class Ghost(EvilBosses):
	# constructor function of child class
	def __init__(self, name):
		self.class_name = "ghost"
		self.health = 5
		super().__init__(name) # inherit the constructor of the parent class
			## the above line makes 
				## Evil.Bosses.objects -> {"ghost":[]}
		self.placeholder_list.append(self) # add the instance to the list
			## in this script, the above line makes
				## self.placeholder_list -> [<Ghost('Hellen') instance>, <Ghost('Murphy') instance>]
			## in this script, now this is true
				## Evil.Bosses.objects -> {"ghost":[<Ghost('Hellen') instance>, <Ghost('Murphy') instance>]}

		self._desc = f"Be Aware! A dead human, {self.name}, is next to you.\n"

	# POLYMORPHISM example
	# method from the child class overrides the method from the parent class
	def getAttacked(self):
		return f"Ghost {self.name} attacks you with a chilling scream!" # a new string

	# PROPERTY FUNCTION example # getter function
	@property
	def desc(self):		
		indicator = f"The ghost is angry. HP: {self.health}\n" # for in-between hp
		if self.health >= 5: # for full hp
			return self._desc
		elif self.health == 2: # for half hp
			indicator = f"Your attack does not seems harmful to them. HP: {self.health}\n"
		elif self.health == 1: # for low hp
			indicator = f"The ghost is running away. Finish them before they escape. HP: {self.health}\n"
		elif self.health <= 0: # for 0 hp
			indicator = f"The ghost is dead. HP: {self.health}\n"
		return indicator

########################################################################################

# helper function to process input string arguments
def specifyCharacter(something: str):
	if len(something.split()) >= 1:
		evil_type = something.split()[0]
		if evil_type in EvilBosses.objects: # if 'something' is at the position {"something": [<subclass instance>,...]}
			try:
				evil_name = something.split()[1] # get the name of the evil through global var "evils"
				evil_character_instance = evils[evil_name] # get the corresponding instance
				return evil_character_instance # return specific instance
			except:
				return f'There is {evil_type}, but the character you asked do not exist.\n'
	return f'There is no "{something}" here.\n'


# function to know how a boss can attack you # POLYMORPHISM demonstration
def bossAttack(something: str): # TYPE ANNOTATION example
	processed_input = specifyCharacter(something)
	if isinstance(processed_input, str): # if instance is not returned
		return processed_input
	evil_character_instance = processed_input # if instance is returned
	return evil_character_instance.getAttacked() + '\n' # call overriden method


# function to get specific descriptions of an evil # (class property function of an object)
def checkHealth(something: str): # TYPE ANNOTATION example
	processed_input = specifyCharacter(something)
	if isinstance(processed_input, str): # if instance is not returned
		return processed_input
	evil_character_instance = processed_input # if instance is returned
	return evil_character_instance.desc # call class property function


# function to set health of an evil # (class attribute of an object)
def attack(something: str): # TYPE ANNOTATION example
	processed_input = specifyCharacter(something)
	if isinstance(processed_input, str): # if instance is not returned
		return processed_input
	evil_character_instance = processed_input # if instance is returned
	print(f"The boss type is {type(evil_character_instance)}.") # CUSTOM CLASS TYPE CHECKING example
	
	# attacking the evil
	if evil_character_instance.health > 0: # if there is health
		evil_character_instance.health = evil_character_instance.health - 1	# reduce health by 1
	msg = f"You infilct damage on the ghost, namely {evil_character_instance.name}.\n"
	
	# if the evil is defeated
	if evil_character_instance.health == 0:
		msg = f"You've defeated the ghost, namely {evil_character_instance.name}.\n"
	
	return msg


# function to get user input and process it
def getInput():
	splitted_command = input('Syntax: (how | attack | check) (evil type) (evil name)\n: ').lower().split()
	command = ' '.join(splitted_command)

	function_word = splitted_command[0]

	if function_word in func_dict:	# if valid key -> get corresponding function
		chosen_function = func_dict[function_word]

		if len(splitted_command) >= 2 : # if something passed after valid key -> pass it to function
			remaining_phrase = ' '.join(splitted_command[1:])
			print(chosen_function(remaining_phrase))

		elif len(splitted_command) < 2: # if nothing passed after valid key
			print(f'You {function_word} nothing.\n')
			return

	else :
		print(f'COMMAND NOT RECOGNIZED - "{command}"\n')
		return


# function when all evils are defeated
def victory():
	all_defeated = all(evil.health <= 0 for evil in evils.values()) # check each instance's HP
	if all_defeated:
		print("VICTORY!!!\nYou have won this game. All evils are defeated!")
		return True # to break the loop


# dictionary to store functions
func_dict = {'how':bossAttack, 'attack':attack, 'check':checkHealth}

########################################################################################

# create two instances of the Ghost subclass in a dictionary
evils = {"hellen":Ghost('Hellen'), "murphy":Ghost('Murphy'), "simon":Ghost('Simon')}

########################################################################################

# main script
if __name__ == '__main__':
	while(True):
		getInput()
		if victory():
			break
