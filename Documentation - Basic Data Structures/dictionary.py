'''This script documents features you can use with Python's dictionary data structure.

* Structure:
*   # dictionary_name = {key: value, key2: value2, ...}

A dictionary in Python is a collection of key-value pairs. Each key-value pair maps the key to its associated value.

Characteristics:
- Keys are immutable (e.g., strings, numbers, tuples).
- Values are mutable (e.g., lists, dictionaries).
- Keys must be unique within a dictionary.
- Keys act like index names in a list, providing a way to access the corresponding values.

Common Operations:
- Adding new items to a dictionary.
- Modifying existing values.
- Deleting key-value pairs.
- Checking for the existence of keys.
- Retrieving values using keys.
- Iterating over keys, values, or key-value pairs.
'''

########################################################################################

# CREATE A DICTIONARY
x = {"M": "1234", 2: "BINARY", True: 1, False: '0'}
	# as we can see, keys can be different data types
print('original -', x)

# ADD A NEW KEY-VALUE PAIR
x["empty"] = None
print('after adding -', x)

# MODIFY A VALUE
x["M"] = "moon"
print('after modification -', x)

# DELETE A KEY-VALUE PAIR
del x["empty"]
print('after deleting -', x)

print()

########################################################################################

# USING 'in' AND 'not in' WITH DICTIONARY
## it checks a certain key in dictionary and return boolean
## it does not search an individual character of that key
	## Example: {'sun' : 'hot'}
	## 'sun' in {'sun' : 'hot'} will return True
	## but it does not further check if 's' in 'sun'

# check if a key is in the dictionary
print("M is in x -", 'M' in x)
print("0 is in x -", '0' in x)

# check if a key is not in the dictionary
print("M is not in x -", 'M' not in x)
print("0 is not in x -", '0' not in x)

# INDEXING A DICTIONARY
## keys are used to retrieve values in the dictionary
if 'M' in x:
    print("'M' is a key with value", x['M']) # gets printed

if '0' in x:
	print("'0' is a key with value", x['0'])  # no print since it is not a key

print()

########################################################################################

# FUNCTION get()
## get corresponding value in a dictionary by giving a key
## always return something
	## second argument not given
		## key exists -> a corresponding value
		## key does not exist -> None
	## second argument given
		## key exists -> a corresponding value
		## key does not exist -> None -> replace None with second argument

# proof that they are the same
print("x.get('M') == x['M'] -", x.get("M") == x["M"])

# examples
print(x)
print(x.get("1234")) # this key does not exist -> return None and no second argument
print(x.get("1234", "something_to_replace")) # return None but second argument -> replace None with "something_to_replace"
print(x.get(True, "something_to_replace")) # this key exists -> return corresponding value

print()

########################################################################################

# FUNCTION keys()
## get keys of a dictionary

print(x.keys())
	# is the same as
for key in x:
	print(key, end=" ")
print()


# FUNCTION values()
## get values of a dictionary
print(x.values())
	# is the same as
for keys in x:
	print(x[keys], end=" ")
print()


# FUNCTION items()
## get both keys and values of a dictionary
print(x.items())
	# is the same as
for keys in x:
	print(f'{keys} : {x[keys]},', end=" ")
print('\n')

########################################################################################

# FUNCTION update()
## add other_dictionary's key-value pairs
## similar to list.extend(other_list) in 'list.py'
y = {'a' : 1, 'b' : 2} # another dictionary
x.update(y) # add 'y' key-value pairs to 'x'
print("after updating -", x, y)

# FUNCTION clear()
## clear the dictionary
y.clear() # clear dictionary 'y'
print("after clearing -", x, y)

########################################################################################
