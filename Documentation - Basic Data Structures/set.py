'''This script documents features you can use with Python's set.

* Structure:
*   # set_name = {element1, element2, ...}

Characteristics:
- You can add new items to a set.
- A set has elements.
- Elements are immutable (cannot be changed once added).
- Elements are unique and cannot be duplicated.
- Sets are unordered collections, so elements do not have a fixed position.
- Sets do not support indexing or slicing.

Common operations:
- Adding elements: set_name.add(element)
- Removing elements: set_name.remove(element)
- Removing an arbitrary element: set_name.pop()
- Converting a list to a set: set(list_name)
- Set operations: union, intersection, difference, symmetric difference
'''

########################################################################################

import random
import string

r = {3, 2, 5, 6} #create a set of r #similar to dictionary but don't have index
print('r =', r)

# ADDING ELEMENTS TO A SET
## FUNCTION add(element)
## set_name.add(element)
## similar to list.append(element) in 'list.py'
r.add(-3) # add -3  
r.add('A') # add string
r.add(4) # add 4
r.add(4) # add 4 again
	# adding duplicate elements doesn't work

# REMOVING ELEMENTS FROM A SET
## FUNCTION remove(element)
## set_name.remove(element)
## similar to list.remove(element) in 'list.py'
print("before remove: ", r)
r.remove(5) # remove 5
print('after remove, before pop: ', r)

# REMOVING THE FIRST ELEMENT FROM A SET
## FUNCTION pop()
## set_name.pop()
## different from list.pop() in 'list.py'
	## set.pop() can't take an index as an argument
	## list.pop() can take an index as an argument
	## set.pop() removes the first element from the set
	## list.pop() removes the last element from the list
r.pop()  # pop the first element
print('after pop: ', r)
print()

########################################################################################

# FUNCTION set()
## convert a list into a set
## set_name = set(list_name)

l = []

for i in range(6):
	ch = random.choice(string.ascii_letters) # produce random character
		# string.ascii_letters >> any alphabet
		# string.ascii_lowercase >> lower case alphabet
		# string.ascii_uppercase >> upper case alphabet
	l.append(ch) # add to a list

s = set(l) # create a set in random order from list
print('list: ', l, '\nset: ', s)
print()

########################################################################################

# SET OPERATIONS

print('r = ', r)
j = {2, 4, 5, 25, 6}
print('j = ', j)

print('union: ', r | j) # union
print('intersection: ', r & j) # intersection
print('setR - intersectionRJ: ', r - j) # setR - intersectionRJ
print('setJ - intersectionRJ: ', j - r) # setJ - intersectionRJ
print('union - intersection: ', r ^ j) # union - intersection
print()

########################################################################################
