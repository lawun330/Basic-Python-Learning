'''This script illustrates all metacharacters available in Python regex.'''

import re

# WILDCARD - .
## metacharacter "." matches any character (other than a new line)
## "." is also called a wildcard and is a special character since it matches any character.

# example
pattern = r"gr.y"

if re.match(pattern, "grey"): # gr(wildcard)y works for 'gray' or 'grey'
	print("Matches the word 1.")

if re.match(pattern, "gray"): # gr(wildcard)y works for 'gray' or 'grey'
	print("Matches the word 2.")

if re.match(pattern, "blue"):
	print("Matches the word 3.")

print()

# DIFFERENCE BETWEEN WILDCARD AND DOT
## .  -> wildcard
## \. -> '.'(a dot) as a char

########################################################################################

# MATCHING INITIAL CHARACTER - ^
# MATCHING FINAL CHARACTER - $

# example
pattern2 = r"^La.........a$"	# ^ is for start # $ is for end
	# ^La -> starts with 'La'
	# ......... -> any characters x 8
	# a$ -> end with 'a'

if re.match(pattern2, "Lawun Nannda"):
	print("Matches initial and final characters.\n")

########################################################################################

# CHARACTER CLASSES - []
## square brackets are meant for matching one character from the specified set of characters

# example
pattern3 = r"[aeiou][s]" 
	# test if a word contains a match from 'a,e,i,o,u'
	# then test if it contains 's'

word1 = 'apples'
word2 = 'myths'
if re.search(pattern3, word1):
	print(word1, "has vowels and plural.")
else:
	print(word1, "does not have vowel nor plural.")

if re.search(pattern3, word2):
	print(word2, "has vowels and plural.\n")
else:
	print(word2, "does not have vowel nor plural.\n")

########################################################################################

# CHARACTER CLASSES WITH RANGE - [start - end] {repetition}

## [0-9][3-5] -> numbers between 03 to 95
## [A-Z]{3} -> 3 consecutive capitals (must be between 'A' to 'Z')
## [a-t] -> small letter between 'a' to 't'
## [A-Za-z] -> any alphabet of any case
## [a-z]{2}[A-Z][a-z]{2} -> two lower case, one upper case, two lower case characters

# example
pattern4 = r"[0-9]"
address = input('Address no. - ')
if re.search(pattern4, address):
	print('Given address have numbers.\n')
else:
	print('Given address does not have numbers.\n')

########################################################################################

# EXCLUDING CHARACTER CLASSES - [^]

# example
pattern5 = r"[^A-Z]"
	# using ^ inside a bracket is not the same as above 
	# it means exclude everything that followed after it
	# [^A-Z] -> any character or number, but exclude the capitals

letter = 'IMYOURS'
if re.search(pattern5, letter):
	print('Matches other than upper case.\n')
else:
	print ('Matches upper case.\n')

########################################################################################

# REPETITION QUALIFIERS

## NON-NUMERIC
### * -> zero or more occurrences # same as {0,} # same as {,}
### + -> one or more occurrences # same as {1,}
### ? -> zero or one occurrences # same as {0,1} # same as {,1}

## NUMERIC
### {X} -> repeat exactly X times
### {X,} -> repeat exactly X times or more
### {X,Y} -> repeat exactly X times, but no more than Y # between X and Y repetitions

# example
pattern6 = r'(egg)(spam)*'
	# starting with 'egg' and having zero or more 'spam's
	# (something)* = zero or more occurrences of something

if re.search(pattern6, 'egg'): # one egg, zero spam -> true
	print('Matches the repetition.')

if re.search(pattern6, 'eggspamegg'): # one egg, one spam, one egg -> true
	print('Matches the repetition again.')

if re.search(pattern6, 'spam'): # no egg -> false -> there is no * after (egg) in the pattern6
	print('Matches the repetition again again.')

print()

# another example
pattern7 = r'colo(u)?r' # zero or one occurence of (something) # something is 'u' in this case
if re.search(pattern7, 'color'): # one color, zero u -> true
	print("color or colour is typed correctly for once.")

if re.search(pattern7, 'colour'): # one color, one u -> true
	print('color or colour is typed correctly for twice.')

if re.search(pattern7, 'colouur'): # one color, two u -> false
	print('color or colour is typed correctly for thrice.')

print()

# another example
pattern_ = r".*9{1-3}$" 
# any character of zero or more occurrences, one to three 9s at the end

########################################################################################

# GROUP - ()

## (u) and (spam) in line 124 and 108 are groups 
## group(n) function -> returns the n-th term

# example
pattern8 = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern8, 'abcdefghijklmnop')
if match:
	print(match.group())  # return all
	print(match.group(0)) # group(0) = group()
	print(match.group(1)) # return first group letters # (bc)
	print(match.group(2)) # (de)
	print(match.group(3)) # (fgh)
	print(match.group(4)) # (g)
	#print(match.group(5)) # index error for 'n' group where match.group(n+1)
	print(match.groups(),'\n') # return all groups in tuples

########################################################################################

# MORE ABOUT GROUP

## NAMING A GROUP (?P<>)
### (?P<any_name>matching_char) # naming a group

## NON-CAPTURING GROUP (?:)
### (?:NON_matching_char) # this group is not captured # avoided for capturing
### non-capturing group has to be matched, but they cannot be called or captured

# example
pattern9 = r'(?P<the_job>teacher).*(?:children).*(parent)'
match2 = re.match(pattern9, 'teacher eats children and parent')
if match2:
	print(match2.group('the_job'), '=', match2.group(1)) # group(1) can be also called by group name
	print(match2.group(2)) # return parent because children is a non-capturing group
	print(match2.groups()) # return 2 capturing groups

# another example
example = r'(a)(b(?:c)(d)(?:e))?'
A = re.match(example, 'abcde')
if A:
	print('example-', A.groups()) # (c) and (e) are not not captured
print()

########################################################################################

# ESCAPE CHARACTER - '\' backslash

## use to match the actual dot "." 
## to distinguish from the wildcard dot

# example
if re.search(r'\.com', 'www.google.com'):
	print("It's a website.\n")

########################################################################################

# OR METACHARACTER - '|'

## . -> any character
## | -> any character between (this or that)

# example
pattern = r'gr(a|e)y'
if re.match(pattern, "grey"):
	print("OR is used 1.")

if re.match(pattern, "gray"):
	print("OR is used 2.")

########################################################################################

# CLASS AND GROUP SIMILARITY
## [aeiou] = (a|e|i|o|u)

########################################################################################
