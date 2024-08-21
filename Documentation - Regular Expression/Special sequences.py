'''This script '''

import re

# USING '\'
## the group number is passed after '\'
## that group should contain repetitions
	### \4 -> 4th group contains repetitions

# example
pattern = r'(.+)\1'
	# (.+) is a group -> having any character of one or more words
	# since there is a single group, it is group 1
	# \1 -> backreference to group 1

word1 = re.match(pattern,'china china china') # (any_chars) (that_previous_chars) (that_previous_chars)
word2 = re.match(pattern,'china china russia') # (any_chars) (that_previous_chars) (different_chars)
word3 = re.match(pattern,'china russia russia') # (any_chars) (different_chars) (that_previous_another_char)

if word1:
	print('Match word1.')
if word2:
	print('Match word2.')
if word3:
	print('Match word3.')
	# return 1 and 2 only
	# group 1's subexpression, 'china', does not match the consecutive succeeding word, 'russia' in word3
print()

# another example
pattern = r'(.+)(.russia)\2' # \2 -> backreference to group 2
word1 = re.match(pattern,'china china china') # (any_chars) (that_previous_chars) (that_previous_chars)
word2 = re.match(pattern,'china china russia') # (any_chars) (that_previous_chars) (different_chars)
word3 = re.match(pattern,'china russia russia') # (any_chars) (different_chars) (that_previous_another_char)

if word1:
	print('Match word1.')
if word2:
	print('Match word2.')
if word3:
	print('Match word3.')
print()

########################################################################################

# NOTES TO DISTINGUISH '\'
## (.+)(.+)...(.+) is not equivalent to as (.+)\'x'
## In other words, \'x' is not the number of repetitions of a group.
## It is the group number. That group has repetitions.
	### (.+)(.+) means two groups of expression
	### (.+)(.+)\'x' means group(x) has repetition of subexpression
	#### Example - (abc|xyz)(s)\1 -> the backreference is on 'abc' or 'xyz'
	#### Example - (we)(our)\2 -> the backreference is on 'our'
	#### Example - (this)(is)\3 -> error because there is only two groups, no group 3 exist

########################################################################################

# MORE ABOUT SEQUENCES 1

## IN ASCII
### [0-9],[\t\n\r\f\v] and [a-zA-Z0-9_]

## IN UNICODE
### \w - match letters and accents

## LOWERCASES
### \d - match digits
### \s - match whitespace (including spacebar,tab,enter)
### \w - match word characters

## UPPERCASES
### \D - opposite to '\d' , match anything that isn't digit
### \S - opposite to '\s' , match anything that isn't whitespace
### \W - opposite to '\w' , match anything that isn't character

# example
pattern = r'\D+\d'  # anything except digit with one or more repetition # one any digit
if re.match(pattern, 'user323'):
	print('Match more about sequences.')
print()

# other examples
# (\D+\s?)+ -> one or more of a group; one or more of anything (not digit); followed by one or zero whitespace;
# [1-6!] -> number of one to six; and '!';
# (\d*\W)+ -> one or more of a group; zero or more digits; followed by exactly one non-character;

########################################################################################

# MORE ABOUT SEQUENCES 2

## \A - string starts here (no character may occur before \A anchored)
## ^ and \A DIFFERENCE
	### ^ -> the start of the line; 
	### \A -> the start of the whole string no matter how many lines are separated;

# example
string = 'We\nneed\na mage' # 3-line string
pattern3 = re.compile(r'\A(We)', re.MULTILINE)
pattern4 = re.compile(r'^(need)$', re.MULTILINE)
	# start at the second line of a whole string
	# first word of the second line is 'need' and it is also the last word

if re.search(pattern3, string):  # search the whole string start with 'We'
	print('pattern3')

print(re.search(pattern4, string).group(),'\n')

########################################################################################

# MORE ABOUT SEQUENCES 3

## \Z - string ends here (no character may occur after \Z anchored)
## \b - 1 or more whitespaces (or) 0 or more letters 
	### usage: at_least_1_word \b at_least_one_word
## \b - empty characters between \w and \W characters
	### '\b(cat)\b' - search the word cat surrounded by boundaries (anything except from char & int)

# example
pattern2=r'\b(eats)\b'
if re.search(pattern2,'tiger eats rabbit'):
	print('match 1')
if re.search(pattern2,'tiger-eats.rabbits'):
	print('match 2')
if re.search(pattern2,'tiger$eats]rabbit'):
	print('match 3')
if re.search(pattern2,'tiger+eats*rabbit'):
	print('match 4')
if re.search(pattern2,'tiger eats(rabbit'):
	print('match 5')
print()

########################################################################################

# \b AND \B DIFFERENCE

# example
	## er\b - match 'never' but not 'verb' (it doesn't end with 'er')
	## er\B - match 'verb' but not 'never' (opposite to \b)

########################################################################################

# EXAMPLE - Email Extraction

## find email address, domain name, domain suffix

string = 'For more informations, please contact wun555@gmail.com'
pattern5= r'([\w\.-]+)@([\w\.-]+)'
	# ([\w\.-]+) -> a group in which one or more repetition of a class
	# that class allows any char, dot, and dash
	# eg: we.l-s-a@gm-ail.co.m

email = re.search(pattern5, string) # re.findall should find all emails
if email:
	print(email.group())
else :
	print('no email')

########################################################################################
