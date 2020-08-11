import re

pattern =r"gr.y"
# meta character "." matches any character (other than a new line)
# "." is also called wildcard and special character since it matches any character.
if re.match(pattern, "grey"): #gr(Anychar)y=gray,grey
	print("match 1")

if re.match(pattern, "gray"):
	print("match 2")

if re.match(pattern, "blue"):
	print("match 3")

print("\n")

pattern2=r"^La.........a$"	#^ is for start , $ is for end
#^La=start with 'La'
#......=any characters
#a$= end with 'a'
#They are special characters - ^ and $ , for matching start and end

if re.match(pattern2, "Lawun Nannda"):
	print("True\n")
###################################

#character classes

pattern3=r"[aeiou][s]" #square brackets are meant for matching one of a specific set of characters
#here, if a word contains a match from 'a,e,i,o,u'' then test if it contains 's' 
word1='apples'
word2='myths'
if re.search(pattern3,word1):
	print(word1,"contains vowels and plural")
else :
	print(word1,"is no vowels or not plural")

if re.search(pattern3,word2):
	print(word2,"contains vowels and plural\n")
else :
	print(word2,"is no vowels or not plural\n")

pattern4=r"[0-9]" 
#[0-9][3-5] = numbers between 03 to 95
#[A-Z]{3} = 3 consecutive capitals (has to be between 'A' to 'Z') (start-end) as range)
#[a-t] = 1 small letter between 'a' to 't'
#[A-Za-z] = any alphabet of any case
#[a-z]{2}[A-Z][a-z]{2} = two lower case, one upper case, two lower case
address=input('address containing no - ')
if re.search(pattern4,address):
	print('address contains numbers\n')

pattern5=r"[^A-Z]"
#using ^ inside bracket is not same as above case, it means exclude everything that followed after it
#[^A-Z] any character,number is allowed, exclude the capitals
letter='IMYOURS'
if re.search(pattern5,letter):
	print('Other than upper case')
else : print ('upper case found')
print('\n')
###################################

#more metacharacters
#repetition qualifiers

pattern6=r'egg(spam)*'
#* zero or more #same as {0,} #same as {,}
#+ one or more #same as {1,}
#? zero or one #same as {0,1} #same as {,1}

#numeric repeatition qualifiers
#{X} repeat exactly X times
#{X,} repeat exactly X times or more
#{X,Y} repeat exactly X times, not more than Y # between X and Y repeatitions

#(previous thing)* = zero or more repetitions of previous thing
#previous thing = can be a single character, a class, a group of characters in parentheses
# this example matches string starting with 'egg' and having zero or more 'spam's
if re.search(pattern6,'egg'):
	print('True')

if re.search(pattern6,'eggspamegg'):
	print('True again')

if re.search(pattern6,'spam'): #this won't be printed
	print('True again again')

#another example
pattern7=r'colo(u)?r' #zero or one occurence of (thing) # thing = 'u' in here
if re.search (pattern7,'color'):
	print("correct spelling")

if re.search (pattern7,'colour'):
	print('correct spelling again')

if re.search (pattern7,'colouur'): #this won't be printed
	print('correct spelling again again') 
print('
      n')
#r".*9{1-3}$" means any character(. represents) of zero or more repeatitions (* represents) and after that, one to three 9s (9{1-3}) at the end ($ represents)
####################################


#groups 
#this is a group - (u) and (spam) as in line 63 and 84

pattern8= r"a(bc)(de)(f(g)h)i"

match = re.match (pattern8,'abcdefghijklmnop')
#group(n) returns the n-th term 
if match:
	print(match.group())  #all
	print(match.group(0)) #group(0)=group()
	print(match.group(1)) #return first group letters #(bc)
	print(match.group(2)) #(de)
	print(match.group(3)) #(fgh)
	print(match.group(4)) #(g)
	#print(match.group(5)) >>> Index error for 'n' group where match.group(n+1)
	print(match.groups(),'\n') #return all groups in tuples
	
pattern9 = r'(?P<name>teacher)(?:children)(parent)'
#(?<any_name>matching_char) #giving a group a name
#(?:NON_matching_char) #this is non-capturing group meaning this group is avoided for capturing
match2 = re.match (pattern9,'teacherchildrenparent')
#NOTE non capturing group has to be matched too like regular expression
#It is just that they cannot be called or captured
if match2:
	print(match2.group('name'),'=',match2.group(1)) #group(1)
	print(match2.group(2)) #return parent because children is non capturing group
	print(match2.groups()) #return 2 capturing groups

#another example for non captured groups
example=r'(a)(b(?:c)(d)(?:e))?'
A=re.match(example,'abcde')
if A:	
	print('example-',A.groups())
print('\n')
######################################
      
#escape character '\' backslash
#used when we want to match the actual dot "." and not to confuse with wildcard dot
print(re.search(r'\.com','www.google.com'))

######################################
      
#metacharacter '|' refers to 'OR'

pattern=r'gr(a|e)y' 
# . = any_char #at line 3
# | = any_limited_char (this or this)

if re.match(pattern, "grey"):
	print("match 1")

if re.match(pattern, "gray"):
	print("match 2")
#class and group similarity
#[aeiou] = (a|e|i|o|u)

#learn more in Special sequences.py and regular expressions.py
