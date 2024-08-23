'''This script documents various features and operations you can perform with Python's string.

* Structure:
* 	# string_name = "a sequence of characters ..."

Characteristics:
- Strings are immutable. Once a string is created, it cannot be changed.
- Strings maintain the order of characters.
- We can iterate over each character in a string.
- Characters do not need to be unique and can contain duplicates.
- Characters are indexed by numerical positions, starting from 0.

Common Operations:
- Concatenation: Combining strings using the + operator.
- Repetition: Repeating strings using the * operator.
- Slicing: Extracting parts of strings using slicing syntax.
- Searching: Finding substrings using methods like find() and index().
- Replacing: Replacing parts of strings using the replace() method.
- Formatting: Creating formatted strings using f-strings, format(), and % formatting.
- Joining: Concatenating strings in a list using the join() method.
- Splitting: Splitting a string into a list using the split() method.
- Counting: Counting characters or substrings using len() and count() methods.
- Manipulation: Converting case using upper() and lower(), and replacing substrings using replace().
- Checking: Checking string properties using startswith(), endswith(), isalpha(), and isnumeric().
- Stripping: Removing whitespace using strip(), lstrip(), and rstrip().
'''

########################################################################################

# CONCATENATION
print("Hello" + " World")


# REPETITION
print("Hello " * 3)

########################################################################################

# STRING SEARCHING
my_string = "Monday is boring"
my_string2 = "Friday is fun"

# FUNCTION find()
## string.find(substring)
## find the corresponding index of the first character of a substring in a string
## return -1 if the substring is not found
print(my_string.find("is"))


# FUNCTION index()
## string.index(substring)
## similar to list.index(element) in 'list.py'
## find the corresponding index of the first character of a substring in a string
## return ValueError if the substring is not found
print(my_string2.index("is"))
print()

########################################################################################

# STRING FORMATTING
## help us create strings with dynamic content by embedding variables and expressions within string literals
## can be implemented using f-strings or the format() function.
List = ['A', 'B', 'C', 'E', 'S', 'X', 'N']

# f-string
formatted_string = f"This is a formatted string using 'f-string': {List[1]}{List[3]}{List[-1]}"  
print(formatted_string)

# format()
formatted_string = "This is a formated string using '.format()': {1}{2}{0}".format(List[-1], List[1], List[3])
print(formatted_string)

# DIFFERENCE BETWEEN TWO APPROACHES
## f-string -> {} directly embeds the value of a variable or expression
## format() -> {} uses positional or keyword arguments to embed values; that argument is a variable or expression

########################################################################################

# STRING FORMATTING
# PRINTF-STYLE
# PERCENT (%) FORMATTING
    # %c -> single character
    # %s -> string
    # %d -> integer
    # %f -> float
## this is another way of string formatting using C functionalities
print("This is a formatted string using 'C printf-style' : %c%c%c" % (List[1], List[3], List[-1]))
print()

########################################################################################

# FORMAT SPECIFIERS
    # {:d} -> integer value
    # {:.2f} -> float with (two) decimal places (.f counts as one decimal place)
    # {:.2s} -> string with (two) characters
    # {:<5s} -> string aligned to the left; space-inclusive string's length is (five)  -> "st   "
    # {:>5s} -> string aligned to the right; space-inclusive string's length is (five) -> "   st"
    # {:^5s} -> string centered; space-inclusive string's length is (five) -> "  st "
## they are used to format values in a string

# example 1: round the price and use format specifiers
price = 100.23443534
new_price = price * 0.9
print(f"price = {price:.3f}\nnew_price = {new_price:.2f}")
print()

# example 2: align float numbers with format specifiers
print("aligned numbers: ")
for a in [0.24, 4234.23, 23.4245]:
	print(f"{a:>7.2f}")
print()

########################################################################################

# JOINING STRING
## join() is used to concatenate strings in a list
snake = ["python", "anaconda", "VIPeR", "cobra"]
snake_string  = ' and '.join(snake) # join each element with a specified string
print(snake_string)


# SPLITTING STRING
## split() is used to split a string into a list
snake_list = snake_string.split(" and ") # split the string into a list by removing specified string
print(snake_list) # the list after joining and splitting
print(snake) # the original list

# check if we obtain the original list back
if snake == snake_list:
    print("the original list and the list after joining and splitting are the same")
else:
    print("the original list and the list after joining and splitting are different")
print()

########################################################################################

# COUNTING IN STRING

some_string = "this is an example string"
some_string_list = some_string.split(' ')

## len() is used to count the number of characters in a string
    ## len(string) -> count each character
    ## len(list) -> count each word
print("length of string: ", len(some_string))
print("length of list: ", len(some_string_list))

## count() is used to count the number of occurrences of a substring in a string
    ## string.count(substring) -> count the number of occurrences of a substring in a string
print("number of times 'i' appears in the string: ", some_string.count("i"))
print()

########################################################################################

# STRING MANIPULATION
## upper() is used to convert a string to uppercase
## lower() is used to convert a string to lowercase
## replace() is used to replace a substring with another substring
print("original: ", snake)
snake[-1] = snake[-1].upper() # convert the string to upper case
print("upper: ", snake)
snake[2] = snake[2].lower() # convert the string to lower case
print("lower: ", snake)
snake[1] = snake[1].replace("anaconda", "mway G") # a string replaced by another string
print("replaced: ", snake)
print()

########################################################################################

letter = "this is a letter for you"

# FUNCTION startswith()
# check if the string starts with a specified substring
if letter.startswith("this"):
    print("starts with 'this'")
elif letter.startswith("This"):
    print("starts with 'This'")


# FUNCTION endswith()
# check if the string ends with a specified substring
if letter.endswith("you"):
    print("ends with 'you'")
elif letter.endswith("You"):
    print("ends with 'You'")
print()

########################################################################################

# FUNCTION strip()
## string.strip() function removes spaces from the left and right of the string
## variations of strip() function
    # string.lstrip() -> same as string.strip(), but it strips only left
    # string.rstrip() -> same as string.strip(), but it strips only right    
space_added_string = "Hello "
print(space_added_string + "!" + "vs." + space_added_string.strip() + "!")


# FUNCTION isalpha()
# string.isalpha() -> return whether the string contains only alphabets
if space_added_string.strip().isalpha():
    print("the string is alphabetic")
else:
    print("the string is not alphabetic")


# FUNCTION isnumeric()
# string.isnumeric() -> return whether the string contains only numbers
numeric_string = "12345"
if numeric_string.isnumeric():
    print("the string is numeric")
else:
    print("the string is not numeric")
print()

########################################################################################

# SLICING A STRING
## similar to SLICING A LIST in 'list.py'
## similar to SLICING A TUPLE in 'tuple.py'
## string_name[start : end+1 : increment] 
    ## if increment is -1 -> string is reversed
## -1 refers to the last index
## if there is nothing, it does not mean 0
    ## [start : : increment] is not equal to [start : 0 : increment]
s = "hey_there"

# the whole string
print(s[:]) 

# every 2nd character
print(s[::2]) 

# reverse the string
print(s[::-1]) 

# [-x:y] -> starts at the 'x'-th character from the end of the string (index start from -1)
#        -> stops at the 'y'-th character from the beginning of the string (index start from 0)
print(s[4:7], '\t', s[-5:7])

# [y:-x] -> starts at the 'y'-th character from the beginning of the string (index start from 0)
#        -> stops at the 'x'-th character from the end of the string (index start from -1)
print(s[2:-4])

########################################################################################