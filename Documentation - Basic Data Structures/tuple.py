'''This script documents features you can use with Python's tuple.

* Structure:
* 	# tuple_name = (element1, element2, ...)

Characteristics:
- Tuples are immutable; you cannot add or change items once a tuple is created.
- Tuples can contain elements of different data types.
- Elements in a tuple are not required to be unique; duplicates are allowed.
- Tuples maintain the order of elements, meaning they are ordered collections.
- Tuples support indexing and slicing operations.
- Elements in a tuple are indexed by numerical positions, starting from 0.

Common operations:
- Creating tuples with or without parentheses.
- Accessing elements using indexing.
- Slicing tuples to create sub-tuples.
- Unpacking tuples into individual variables.
- Swapping values using tuple unpacking.
- Using extended iterable unpacking with the asterisk (*) operator.
- Creating nested tuples, where tuples can contain other tuples.
'''

########################################################################################

#Tuples #immutable VarName and StoredKeys
#VarName=(StoredKeys) , VarName=StoredKeys >>no need of parentheses
#VarName[num] #num starts from 0 and ends in n-1 for n numbers of StoredKey

# CREATE A TUPLE
## a tuple can be created with or without parentheses
leaf_village_ninjas = ("NEIJI", "MINATO", "NARUTO")
sand_village_ninjas = "GARRA", "SASORI"
_th_hokage = ("NARUTO", 7, True) # tuple can store different data types
print(leaf_village_ninjas)
print(sand_village_ninjas)
print(_th_hokage)

# INDEXING A TUPLE
print(leaf_village_ninjas[2], "fights", sand_village_ninjas[0])
print()

########################################################################################

# SLICING A TUPLE
## similar to SLICING A LIST in 'list.py'
## tuple_name[start : end+1 : increment] 
    ## if increment is -1 -> tuple is reversed
## -1 refers to the last index
## if there is nothing, it does not mean 0
    ## [start : : increment] is not equal to [start : 0 : increment]
hokages = leaf_village_ninjas[1:]
print(hokages[0], "is the father of", hokages[1])
print()

########################################################################################

# TUPLE UNPACKING
team7 = ('NARUTO', 'SASUKE', 'SAKURA')
hokage, rogue_ninja, useless_ninja = team7
print(hokage, 'and', rogue_ninja, 'are more powerful than', useless_ninja)
print()

########################################################################################

# DATA SWAPPING
hokage, rogue_ninja, useless_ninja = rogue_ninja, hokage, useless_ninja
print("What if the life of", hokage, "is swapped with", rogue_ninja, "?")
print()

########################################################################################

# Extended Iterable Unpacking
## tuple with asterisk (*) can take multiple values
## similar to '*arg' from function parameter in 'parameters and arguments.py'
a, b, c, *d, e= (1, 2, 3, 4, 5, 6, 7, 8)
print(*d)
print()

########################################################################################

# NESTED TUPLE
## a tuple can contain other tuples
## this can go on and on
t1 = (team7, 4, 5, 5) # duplicate elements are allowed
t2 = (0, 1, t1, 3)
print("Nested one-level =", t1)
print("Nested two-level =", t2)
print()

########################################################################################