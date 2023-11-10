#say or examine "zombie" game
#----------------------------

def get_input():
	command = input (': ').split() #split the input strings into list
	sentence=' '.join(command) #make a full string back from list

	verb_word=command[0] 

	if verb_word in verb_dict:	#if allowed keys are used
		verb=verb_dict[verb_word]
		#dictionary[key]=function 
		#verb is in fact,the function (eg- Say and examine as defined in line 39 & 62)

	else :	#keywords not recognized ==> return NOT RECOGNIZED
		print('NOT RECOGNIZED - "{}"\n'.format(sentence))
		return

#check the keyword and conditional pass
	if len(command)>=2 :
		if 'say' in command:
			command.remove('say') 
			phrase=command
			said_Sentence=' '.join(phrase)
			print(verb(said_Sentence))	#call the function Say with said_Sentence as argument
		if 'examine' in command:
			noun_word=command[1]
			print(verb(noun_word))

	elif len(command)<2: #function (blank) is functioning nothing
		if 'say' in command:
			print('You said nothing.\n')
			return	
		elif 'examine' in command:
			print('You examined nothing.\n')
			return

#say(Noun) == verb(said_sentence)
def Say(Noun):
	return 'You said "{}".\n'.format(Noun)
#---------------

class Gameobj:
	class_name=""
	desc=""
	objects={}  #a dictionary

	def __init__ (self,name):
		self.name=name  #zombobo is name (line 60)
		Gameobj.objects[self.class_name]=self  # class_name is added as key to dictionary and value is self(instance)
		#{"zombie": zombie}, in other words,{"zombie": Zombie('zombobo')} because self is replaced

	def get_desc(self):
		return self.class_name+':'+self.desc+'\n'

class Zombie(Gameobj):
	class_name='zombie'
	desc='a creepy guy'

zombie=Zombie('zombobo') #call the subclass Zombie #this is not related with input, it is the written data

def examine(Noun): #Noun is parameter for self.class_name
	if Noun in Gameobj.objects:  #if zombie in {"zombie": zombie},
		return Gameobj.objects[Noun].get_desc() # return zombie.desc='a creppy guy' 
	else:
		return "There is no {} here.\n".format(Noun)

verb_dict={"say":Say,"examine":examine} #the value of dictionary are functions

while True:
	get_input() 
#---------------------
#*** Flow ***
#line 70 > 4 to 8 > if True > if arg 	> 20 > if say 	  > 20  > 39 > EXECUTED!!
#								   		       if examine > 26 	> 62 > if True  > 48-50,56,60 > 53 >  EXECUTED!!
#																	 > if False > 66 > EXECUTED!!
#						      if noArg	> 30 > if say 	  > 33	> EXECUTED!!
#											   if examine > 36	> EXECUTED!!
#				   if False > 17 > EXECUTED!!