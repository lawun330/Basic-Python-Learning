#-simple game with ghost
#touch and examine Horny_ghost

class Gameobj:
	class_name=""
	desc=""
	objects={}  

	def __init__ (self,name):
		self.name=name
		Gameobj.objects[self.class_name]=self 

#{"Horny_ghost":Ghost('MM')}

class Ghost(Gameobj):
	def __init__(self,name):
		self.class_name="Horny_ghost"
		self.health=5
		self._desc="Be Aware! A dead woman is next to you.\n"
		super().__init__(name)

	@property
	def desc(self):
		indicator="She's angry. Available count: {}\n".format(self.health)
		if self.health >=5:
			return self._desc
		elif self.health ==2:
			indicator="She seems ignoring. Available count:{}\n".format(self.health)
		elif self.health ==1:
			indicator="She's smiling. Available count:{}\n".format(self.health)
		elif self.health<=0:
			indicator="She's satisfied and you're saved.\n"

		return indicator 

def examine(Noun): 
	if Noun in Gameobj.objects:  
		return Gameobj.objects[Noun].desc
	else:
		return "There is no {} here.\n".format(Noun)

def touch(Noun):
	msg="There's no {} here.\n".format(Noun)
	if Noun in Gameobj.objects:
		thing=Gameobj.objects[Noun]
		if type(thing)==Ghost: #if {"Horny_ghost":Ghost} == {"Horny_ghost":thing}  >>> Ghost==thing 
		#this is done in case there are more key-class_val to dictionary
			thing.health=thing.health-1	#Ghost.health-=1
			if thing.health<=0:
				msg="You've satisfied the ghost.\n"

			else :
				msg="You've touched the {}.\n".format(thing.class_name)
	return msg 

def get_input():
	command = input (': ').split()
	sentence=' '.join(command) 

	func_key=command[0] 

	if func_key in func_dict:	#if allowed keys are used
		func=func_dict[func_key]

		if len(command)>=2 :
			noun_word=command[1]
			print(func(noun_word))

		elif len(command)<2:
			print('You {} nothing.\n'.format(func_key))
			return
		
	else :	
		print('NOT RECOGNIZED - "{}"\n'.format(sentence))
		return

func_dict={'touch':touch,'examine':examine}
ghost=Ghost('MM')

while True:
	get_input()