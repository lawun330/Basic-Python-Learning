import re

pattern = r'(.+)\1' # \number of desired group 
#(.+) is a group,having any character of one or more words
#\1 means that subexpression of group 1 ,(whether a repetition of what was found in group number 1 exists or not)

word1=re.match(pattern,'china china china') #(Any_chars) (that_previous-chars) (that_previous-chars)
word2=re.match(pattern,'china china usa')#(Any_chars) (that_previous-chars) (Another_chars)
word3=re.match(pattern,'china russia russia')#(Any_chars) (Another_chars) (that_previous_another_char)

if word1:
	print('1')

if word2:
	print('2')

if word3:
	print('3')
print("Another test")
#return 1 and 2 only because as in line 9, word3 has three different words
#group 1's subexpression, 'china' is no longer match for the consecutive succeeding words in word3

#another test
pattern = r'(.+).(russia) \2'
word1=re.match(pattern,'china china china') #(Any_chars) (that_previous-chars) (that_previous-chars)
word2=re.match(pattern,'china china usa')#(Any_chars) (that_previous-chars) (Another_chars)
word3=re.match(pattern,'china russia russia')#(Any_chars) (Another_chars) (that_previous_another_char)
if word1:
	print('1')

if word2:
	print('2')

if word3:
	print('3')
print()
#NOTE >>>>>>>>>>>>>>>
#(.+)(.+)...(.+) is not the same as (.+)\'x'
#\'x' is not the no of repetition of group. It is the repetition of group (x)
# (.+)(.+) means two groups of expression 
# (.+)(.+)\'x' means group(x) has repetition of subexpression
#Example - (abc|xyz)(s)\1 means the pointer is on 'abc' or 'xyz' 
#Example - (we)(our)\2 means the pointer is on 'our'

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

pattern=r'\D+\d'  #anything except digit with one or more repetition followed by one digit
if re.match(pattern,'Hello 323'):
	print('Hi')
print('\n')
#(\D+\s?)+  = a group of, one or more of anything (not digit) followed by one or zero occurrence of a whitespace
#[1-6!] = number of one to six and !
#(\d*\W)+ = a group of, zero or more digits followed by exactly one non character

#\A - the string starts here (no character may occur before \A anchored)
#^ means the start of the line, \A means the start of the whole string no matter how many lines are separated
#\Z - the string ends here (no character may occur after \Z anchored)
#\b - 1 or more whitespaces (or) 0 or more letters #Use as - at_least_1_word (\b) at_least_one_word
#\b - empty characters between \w and \W characters 
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
print()

#another use of \b & \B 
#er\b - match 'never' but not 'verb' (it doesn't end with 'er')
#er\B - match 'verb' but not 'never' (opposite to \b)

#\A and \Z

string='We\nneed\na mage'
pattern3=re.compile(r'\A(We)',re.MULTILINE) #re.MULTILINE reads multiple lines to match the word
pattern4=re.compile(r'^(need)$',re.MULTILINE) #start at the second line of a whole string paragraph 
#first word of the second line is 'need' and it is also the last word

if re.search(pattern3,string):  #start the whole string with 'We'
	print('pattern3')

print(re.search(pattern4,string).group(),'\n') 

#Email extraction example

string='For more informations, please contact wun555@gmail.com'
# ([\w\.-]+) = a group which is one or more repetition of (any char or dot or dash)
pattern5=r'([\w\.-]+)@([\w\.-]+)' #eg - we.l-s-a@gm-ail.co.m
#email address, domain name, domain suffix
email=re.search(pattern5,string) #re.findall should find all emails
if email:
	print(email.group())
else : 
	print('no email')

	#NOTE here >>> .  means any char 
	#	   >>>\.  means '.'(a dot) as a char

#learn more in metacharacters.py and regular expressions.py
