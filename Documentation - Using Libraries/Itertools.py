'''This educational script illustrates the use of the itertools module for efficient iteration.
This module contains a set of fast, memory efficient tools that are useful by themselves or in combination.

It covers:
- Basic Functions -> (permutations, combinations, product, chain)
- Infinite Iterators -> (count, cycle, repeat)
- Iterator Utilities -> (zip_longest, takewhile, dropwhile, accumulate)

This script serves as a practical guide for understanding and utilizing itertools for various iteration tasks in Python.
'''


import itertools as it


# BASIC FUNCTIONS

name = ['A', 'B', 'C']
num = [1, 2, 3]
string = ['hello', 'world']

print("permutation is", list(it.permutations(name)))	# permutation
print("combination is", list(it.combinations(name, 2)))	# combination
print("product is", list(it.product(name, num)))	# product
	## example
		### product((x, y, 2),(x, 2)) -> [(xx), (2x), (yx), (2y), (2x), (2)] for "(x + y + 2)(x + 2) = (xx + 2x + yx + 2y + 2x + 2)"
print("chain is", list(it.chain(name, num)))	# chain
print("chain from iterable is", list(it.chain.from_iterable(string)))	# chain
print()

########################################################################################

# FUNCTION count(x, y)
## count from x with y steps
## need to set the terminal condition
print("count function:")
for i in it.count(-10, 2):
	print(i)
	if i > 0:	# terminal condition
		break
print()

########################################################################################

# FUNCTION iter()
## make an iterator object for the next() function
iterable1 = iter(string)
print(iterable1)

# FUNCTION next()
## iterate each element of the iterator object
## return error once the iterator object is exhausted of elements to be retrieved
print("the next element is", next(iterable1))
print("the next element is", next(iterable1))
print()

########################################################################################

# FUNCTION zip_longest()
## create a tuple in a list -> [(a,b),(c,d)] 
## if the iterables are of different lengths, the missing values are filled with None
	### return [(<something>, <something>), (None, <something>), ...] if the iterator object is exhausted
latitudes = [1, 2, 3]
longitudes = [4, 5, 6, 7]
coordinates = list(it.zip_longest(latitudes, longitudes)) 
print("zip_longest function:", coordinates)
print()

########################################################################################

# FUNCTION repeat()
## repeat(thing_to_repeat, number_of_repetitions)
## repeat a value (an element) (up to infinite-th)
repeated_element = list(it.repeat(3, 5))
print("repeat function:", repeated_element)
print()

########################################################################################

# FUNCTION cycle()
## repeat the iterator object for infinite times till the memory is not enough
	### if 1, 2, 3 is the iterator object -> 1, 2, 3, 1, 2, 3, 1, 2, 3, ...
## UNCOMMENTING WILL CONSUME TOO MUCH MEMORY
# try:
# 	repeated_iterable = list(it.cycle(num))
# 	print("cycle function:", repeated_iterable)
# except MemoryError:
# 	print("cycle function: MemoryError")
# print()

########################################################################################

# FUNCTION takewhile()
## return the iterator object's elements which satisfy the condition
## if the condition is true for all elements, return all elements
## if the condition is false for the first element, return an empty list
print("takewhile function:", list(it.takewhile(lambda x: x > 0, [213, 12, 442, -3, 2, 424])))
print("takewhile function:", list(it.takewhile(lambda x: x > 0, [213, 12, 442, 3, 2, 424])))
print("takewhile function:", list(it.takewhile(lambda x: x > 0, [-213, 12, 442, 3, 2, 424])))
print()

########################################################################################

# FUNCTION dropwhile()
## return the iterator object's elements which do not satisfy the condition
## if the condition is true for all elements, return an empty list
## if the condition is false for the first element, return all elements
print("dropwhile function:", list(it.dropwhile(lambda x: x > 0, [213, 12, 442, -3, 2, 424])))
print("dropwhile function:", list(it.dropwhile(lambda x: x > 0, [213, 12, 442, 3, 2, 424])))
print("dropwhile function:", list(it.dropwhile(lambda x: x > 0, [-213, 12, 442, 3, 2, 424])))
print()

########################################################################################

# FUNCTION accumulate()
## return the accumulated sum of the iterator object
## add up to i for accumulate(i)
## if the iterator object is a list of numbers, return the list of accumulated sum
print("accumulate function:", list(it.accumulate(range(5))))
	# range 0 -> 0
	# range 1 -> 0+1=1
	# range 2 -> 0+1+2=3
	# range 3 -> 0+1+2+3=6
	# range 4 -> 0+1+2+3+4=10
	# the output -> 0,1,3,6,10
print()

########################################################################################
