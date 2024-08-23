'''This script demonstrates the usage of Python's built-in enumerate function.
* Usage: enumerate(iterable, start=0)
The enumerate function adds a counter to an iterable and returns it as an enumerate object. '''

list_example = ["eat", "sleep", "repeat"]
string_example = "geek"

# creating enumerate objects
obj1 = enumerate(list_example)
obj2 = enumerate(string_example)
print("enumerate with list: ", obj1, "\nenumerate with string: ", obj2)
print()

# checking type with type()
if type(obj1) == type(obj2):
    print("Return type:", type(obj1))
print()

# create a list with index positions
print(list(enumerate(list_example)))
print(list(enumerate(string_example)))
print()

# make the index starts at an arbitary position instead of 0
print(list(enumerate(list_example, 10)))
print(list(enumerate(string_example, 2)))
print()

# unpacking the enumerate object
for index, value in enumerate(list_example):
    print(index, value)
for index, value in enumerate(string_example):
    print(index, value)
