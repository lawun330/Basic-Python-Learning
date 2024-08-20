'''This script documents the use of if/else conditionals with loop and exception handling.
It also documents the normal and ternary operator styles of writing if/else statements.'''

# IF/ELSE NORMAL CONDITIONAL STATEMENT

a = 'woof'
b = 'dog'
c = 'cat'

def animal():
	global a, b, c
	if a == 'woof':
		print(b)
	else :
		print(c)

# check
animal()

# check again with a new value
a = 'meow'
animal()
print()

#################

# IF/ELSE TERNARY OPERATOR

# it is known as ternary operator because of 3 arguments

# check
a = 'woof'
b = 'dog' if a == 'woof' else 'cat'
print(b)

# check again with a new value
a = 'meow'
b = 'dog' if a == 'woof' else 'cat'
print(b)

# example - Email
state = 1
string = 'login' if state == 1 else 'logout'
print(f'You have successfully {string}')
print()

#################

# EXPERIMENTING CONDITIONALS WITH (FOR / WHILE) LOOP
## IF CONDITION NOT MET
for i in range(5):
	if i == 6: # i != 6 so code will not reach the break
		print("'i' is 6")
		break
else : # it does this after for loop
	print("'i' will not be 6")

## IF CONDITION MET
for i in range(5):
	if i == 3: # i == 3 at some point so the loop breaks
		print("'i' is 3")
		break
else :  # already exit loop # this never execute
	print("'i' will not be 3")
print()

#################

# EXPERIMENTING ELSE WITH (TRY / EXCEPT) BLOCKS
## IF ERROR NOT RAISED
try :
	print(1 / 1) # this raises no error
except ZeroDivisionError : # this is not executed
	print('ERROR1')
else :	# so this is executed
	print('no error1')

## IF ERROR RAISED
try :
	print(1 / 0) # this raises error
except ZeroDivisionError : # this is executed
	print('ERROR2')
else : # so this is skipped
	print('no error2')

#################
