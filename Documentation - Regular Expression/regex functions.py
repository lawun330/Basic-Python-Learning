'''This script illustrates different Python functions for dealing with regular expression.'''

import re

# RAW STRING
## it is a pattern used to match strings
## raw strings don't escape anything which makes regular expression easier
string = r"@"

########################################################################################

# FUNCTION re.match()

## match one string with another
	## matching starts from the first index of both strings
	## matching ends when one of the strings indices reaches the end
## return false if two strings are not matched AT ANY INDEX POSITION

# example
if re.match(string, "wun555@gmail.com"): 
	print("Match!")
else:
	print ("No match!")

print()

########################################################################################

# FUNCTION re.search()

## search for a match
## return true or false

# example
confirmation = re.search(string, "wun554@gmail.com") 
if confirmation:
	print("vaild email")
	print(confirmation.group()) # return the matched substrings 
	print(confirmation.start()) # return the first matching index
	print(confirmation.end()) # return the last matching index
	print(confirmation.span()) # return above indices in tuple

else:
	print("It's not an email.")

print()

########################################################################################

# FUNCTION findall()
## return a list containing substrings(of one full string) that matches the pattern

# FUNCTION finditer()
## return iterator instead of list

# example
string = r"@gmail"
print(re.findall(string, "wun550@gmail.com is not wun554@gmail.com"))
print(re.finditer(string, "@gmail.com")) 
print()

########################################################################################

# FUNCTION sub()
## a substitution function that replaces matched strings with new strings

# example
mistake = r'1email'
incomplete_email = 'wun5501email.com'
complete_email = re.sub(mistake, "@gmail", incomplete_email)
print(incomplete_email, 'to', complete_email)
# we can then extract the email using r"[\w.%+-]+@[\w.-]+"
print()

########################################################################################

# FUNCTION split()
## split the strings or sentences into list
## special characters act like a normal character that is passed to match

# example
sentence = "A sentence. Second sentence? Yes it is!"
example = re.split(r"[.?!]", sentence) 
print(example)

# with grouping, '()' -> we can return '.' '!' characters which are in the [] bracket
example2 = re.split(r"([.?!])", sentence) 
print(example2)

print()

########################################################################################

# FUNCTION compile() AND re.MULTILINE
## read multiple lines to match the word

# example
string = 'line 1\nline 2\nline 3' # 3-line string
p = re.compile(r'(line 2)', re.MULTILINE)
if re.search(p, string):
	print('line 2 found.')

########################################################################################
