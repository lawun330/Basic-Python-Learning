import re

pattern = r'(.+) \1' #\number of desired group
#(.+) is a group,having any character of one or more words
#\1 means that subexpression of group 1 ,(a repeatition of what was found in group number 1)

word1=re.match(pattern,'china china china') #(Any_chars) (that_previous-chars) (that_previous-chars)
word2=re.match(pattern,'china china usa')#(Any_chars) (that_previous-chars) (Another_chars)
word3=re.match(pattern,'china russia usa')#(Any_chars) (Another_chars) (Another_different_chars)

if word1:
	print('1')

if word2:
	print('2')

if word3:
	print('3')

#return 1 and 2 only because as in line 9, word3 has three different words
#group 1's subexpression, 'china' is no longer match for the consecutive succeeding words in word3


#NOTE >>>>>>>>>>>>>>>
#(.+)(.+)...(.+) is not the same as (.+)\n that is,
# (.+)(.+) means two groups of expression 
# (.+)(.+)\2 means repeatition of subexpression of group(2) in next consecutive word
#Example - (abc|xyz)\1 means 'abc' or 'xyz' followed by the same thing
#Example - (we)(our)\2 means 'we our our'

#####################################

#More sequences

#=============================================================
#\d - match digits
#\s - match whitespace (including spacebar,tab,enter)
#\w - match word characters

#IN ASCII mode
#[0-9],[\t\n\r\f\v] and [a-zA-Z0-9_] 

#IN UNICODE mode
#\w - match letters and accents

#UPPER and LOWER mattters!!!
#\D - opposite to '\d' , match anything that isn't digit
#\S - opposite to '\s' , match anything that isn't whitespace
#\W - opposite to '\w' , match anything that isn't character
#==============================================================

pattern=r'\D+\d'  #anything except digit with one or more repeatition follwed by one digit
if re.match(pattern,'Hello 323'):
	print('Hi')
print('\n')
#(\D+\s?)+  = one or more of (anything (not digit) of one or more occurrences followed by none or one whitespace)
#[1-6!] = number of one to six and !
#(\d*\W)+ = one or more of (zero or more of digit followed by non character)

#\A - the string starts here (no character may occur before \A anchored)
#^ means the start of the line, \A means the start of the whole string no matter how many lines are separated
#\Z - the string ends here (no character may occur after \Z anchored)
#\b - match 1 or more whitespaces and 0 or more letters, at_least_1_word (\b) at_least_one_word
#\b - match(search) empty string between \w and \W characters 
#'\b(cat)\b' - search the word cat surrounded by boundaries(anything except from char & int)

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

#another use of \b & \B 
#er\b - match 'never' but not 'verb' (it doesn't end with 'er')
#er\B - match 'verb' but not 'never' (opposite to \b)

#\A and \Z

string='We\nneed\nmage'
pattern3=re.compile(r'\A(We)',re.MULTILINE) #re.MULTILINE reads multiple lines to match the word
pattern4=re.compile(r'^(need)$',re.MULTILINE)

if re.search(pattern3,string):  #start the whole string with 'We'
	print('pattern3')

print(re.search(pattern4,string).group(),'\n') #start the second line of a whole string but first word of the line with 'need'

#Email extraction example

string='For more informations, please contact lawun330@gmail.com'
# ([\w\.-]+) = one or more repeatition of class (having any char or dot or dash)
pattern5=r'([\w\.-]+)@([\w\.-]+)([\w\.]+)' #eg - we.l-o-r-a@gm-ail.co.m
#email address, domain name, domain suffix
email=re.search(pattern5,string) #re.findall should find all emails
if email:
	print(email.group())
else : 
	print('no email')

	#NOTE here >>> .  means any char 
	#	   >>>\.  means '.'(a dot) as a char

#learn more in metacharacters.py and regular expressions.py
