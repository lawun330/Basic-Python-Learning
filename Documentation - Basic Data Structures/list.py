'''This script documents various features and operations you can perform with Python's list data structure.

* Structure:
* 	# list_name = [element1, element2, ...]

Characteristics:
- Lists can contain multiple elements.
- Elements in a list are mutable (i.e., they can be changed).
- Elements are not required to be unique and can be duplicated.
- Elements are indexed by numerical positions, starting from 0.

Common Operations:
- Creating lists
- Adding elements
- Removing elements
- Accessing elements
- Slicing lists
- Copying lists
- Extending lists
- Nested lists
- Clearing lists
- List comprehensions
'''

########################################################################################

# CREATE A LIST
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # contain unique elements
Years = [2017, 2019, 2019, 2019, 2020, 2020] # contain duplicate elements
print(Days)
print(Years)

# INDEXING A LIST
print(Days[0]) # print the first element
print(Years[4]) # print the 5th element
print()

########################################################################################

# FUNCTION len()
## find the number of elements in a list (length of a list)
print("Length of 'Years' -", len(Years))
print("Length of 'Days' -", len(Days))
print()

########################################################################################

# USING 'in' AND 'not in' WITH LIST
## it checks a certain element in list and return boolean
if 'Friday' in Days:
    print("It is in days")
if '2018' not in Days:
    print("It is not in days")
print()

########################################################################################

# FUNCTION index()
## list.index(element)
## similar to string.index(substring) in 'string.py'
## find the corresponding index of an element in a list
print('Friday is at Days [', Days.index('Friday'), ']')
print()

########################################################################################

# ADDING ELEMENTS TO THE END OF A LIST
# FUNCTION append(element)
Years.append(2021) # add 2021 to the end
print(Years)

# ADDING ELEMENTS TO A SPECIFIC POSITION IN A LIST
# FUNCTION insert(index, element)
Years.insert(1, 2018) # add 2018 to the index 1
print(Years)

# REMOVING ELEMENTS FROM ANY POSITION IN A LIST
# FUNCTION remove(element)
Years.remove(2017) # remove 2017 from 0th index
Years.remove(2020) # remove 2020 from 6th index
Years.remove(2020) # remove 2020 from 5th index
print(Years)

# REMOVING ELEMENTS FROM A SPECIFIC POSITION IN A LIST
# FUNCTION pop(index)
Years.pop(1) # remove element from index 1
print(Years)

# REVERSING THE ORDER OF ELEMENTS IN A LIST
# FUNCTION reverse()
Years.reverse() # reverse order
print(Years)

print()

########################################################################################

# FUNCTION count(element)
## count the number of times an element appears in a list
print("There are", Years.count(2020), "2020s in the Years")
print("There are", Years.count(2019), "2019s in the Years")

# FUNCTION max(list)
## return the maximum element in a list
print(max(Days),'has the longest string')

# FUNCTION min(list)
## return the minimum element in a list
print(min(Days),'has the shortest string')
print()

########################################################################################

# COPYING A LIST

List1 = [1, 2, 3, 4, 5]

## SIMILAR TO PASS-BY-REFERENCE
### create a new reference to the same object
### point to the same memory location
### modify one list will also modify the other
List2 = List1

## SIMILAR TO PASS-BY-VALUE
### create a new object and copy the contents of the original object to the new object
### different memory location
### modify one list will not affect the other
List3 = List1.copy() # a shallow copy

# test
print("List1 =", List1, "List2 =", List2, "List3 =", List3)
List1[0] = 100 # modify list1 -> list2 get modified too
List3[0] = 200 # modify list3 -> no other list is modified
print("List1 =", List1, "List2 =", List2, "List3 =", List3)
print()

########################################################################################

# SLICING A LIST
## similar to SLICING A TUPLE in 'tuple.py'
## similar to SLICING A STRING in 'string.py'
## list_name[start : end+1 : increment] 
    ## if increment is -1 -> list is reversed
## -1 refers to the last index 
## if there is nothing, it does not mean 0
    ## [start : : increment] is not equal to [start : 0 : increment]

print("unsliced list =", List1)
print("sliced list1 =", List1[0:7:2])
print("sliced list2 =", List1[4::-1])
print("second last =", List1[-2])
print()

########################################################################################

# EXTENDING A LIST
## add elements from one list to the end of other list
## similar to dictionary.update(another_dict) in 'dictionary.py'
print("Days =", Days)
print("List2 before adding Days =", List2)
List2.extend(Days)
print("List2 after adding Days =", List2)
print()

# NESTED LIST
## a list can contain other lists
## this can go on and on
List4 = [2, 4, List3]
List5 = [List4, 0, 12]
print("Nested one-level =", List4)
print("Nested two-level =", List5)
print()

# CLEARING A LIST
## delete all elements of a list
## do not delete the list itself
print("List2 =", List2)
print("List3 =", List3)
List2.clear()
List3.clear()
print("List2 =", List2)
print("List3 =", List3)
print()

########################################################################################

# LIST COMPREHENSION
## provide a concise way to create lists
## [expression for item in iterable if condition]
val = [i * 2 for i in range(11) if i % 2 != 0] # multiply with 2 if the num is odd
print("squared of odds in 1 to 10 =", val)

########################################################################################
