#normal use of if/else

a='woof'
b='dog'
c='cat'

def animal():
	global a,b,c
	if a=='woof':
		print (b)
	else :
		print (c)

animal()
a='meow'
animal()
print('\n')
#################

#condition use or ternary operator (so called because of 3 arguments)

a='woof'
b='dog' if a=='woof' else 'cat'
print(b)

a='meow'
b='dog' if a=='woof' else 'cat'
print(b)
print('\n')
#################

#Example - email use

state=1
string='login' if state==1 else 'logout'
print('You have successfully {}'.format(string))
print('\n')
#################

#else with for / while

for i in range(5):
	if i==6: # i!=6 so code will not reach the break
		print("'i' is 6")
		break

else : #so it does this after for loop
	print("'i' will not be 6")

for i in range(5):
	if i==3: # i==3 at some point so the loop break
		print("'i' is 3")
		break

else :  #loop already break, this never execute
	print("'i' will not be 3")
print('\n')
#################

#else with try / except blocks

try :
	print(1/1) #this is true
except ZeroDivisionError : #this is not executed
	print('ERROR1')
else :	#so this is executed
	print('no error1')

try :
	print(1/0) #this is false
except ZeroDivisionError : #this is executed
	print('ERROR2')
else : #so this is skipped
	print('no error2')

#################

#NOTE	- else is avoided or skipped if for/while loop is broken or Error exception is executed
#		- else is executed after complete execution of for loop and no Error is raised

a=[12,4,7,8]
print(a)