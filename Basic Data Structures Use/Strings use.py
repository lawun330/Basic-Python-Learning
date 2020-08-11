#format function for strings
#===========================
List=['A','B','C','E','S','X','N']
print(List)

#{i^th} in format(0,1,2,,..,i) and i=list[x] where x in list[1,'2','aa',...x] / x is replaced
#{1} in format(A,B,C,D,etc) is B , B=ListB[3] where 3 in ListB=[b,B,bB,Bb] is bB , {1} position is replaced by bB

string= "Char : {1} {0} {2} ".format(List[3], List[4],  List[5])  #format(E,S,X) /1=S/0=E/2=X>>>1,o,2=SEX
print(string)

#"{var1},{var2}" is assigned with values by format
a='{b},{c}'.format(c=0,b=1)
print(a)

#rounding a float number
price = 100.23443534
new_price = price * 0.9
print("price = {:.2f} new_price = {:.2f}".format(price, new_price))
'''
{:d} for integer value
{:.2f} for float with two decimal places
{:.2s} for string with two characters
{:<5s} for string aligned to the left that many spaces  - "st   "
{:>5s} for string aligned to the right that many spaces - "   st"
{:^5s} for string centered in that many spaces 			- "  st "
'''
#aligning numbers
for a in [0.24,4234.23,23.4245]:
	print("{:>7.2f}".format(a)) #note - . counts as one space

#other way of printing variables in string
print("Char : %c %c %c" % (List[3],List[4],List[5]))

#f-string
#this is like .format() but it takes values from variables instead of parameters
print(f'Hello {List}')

#useful string functions
#===================

snake=["python","anaconda","viper","cobra"]
print('+'.join(snake))  #join the StoredVar with 'string' #create a string from list
print(snake[1].replace("anaconda","mway G")) #a string replaced by string
print("shwe dagon".upper()) #change the whole string to upper case 
print("RIVER".lower()) #change the whole string to lower case

letter="this is a letter for you"

print(letter.startswith("this")) #check if the string is starts with 'substring' #return True since condition is true
print(letter.endswith("you")) #check if it ends with 'substring'
print(letter.startswith("This")) #return False
print(letter.split(" "))  #create a list from string

space_added_string = "Hello "  #strip function for removing indexes and spaces
print(space_added_string+"!"+space_added_string.strip()+"!")
'''
string.lstrip() #same as string.strip() but it strips only left
string.rstrip() #same as string.strip() but it strips only right
string.isnumeric() #return whether it is just numbers
string.isalpha() #return whether it is just alphabets
string.count("S") #counts the number of repeatition of substring "S" in string
'''
#numeric functions
#=================

num=(6,7,3,-376,673,67)
print("maximium : " ,max(num)) #return the maximum number or string but work ONLY in SAME DATA TYPE
#max() don't know if "string">number
print("minimum : ",min(num)) #return minimum number
print("absolute value : ",abs(num[3])) #absolute value of that number (count from zero)
print("sum is",sum(num)) #sum all

if all(i>0 for i in num): #all() take a list as arguments  #return True if condition is true for all arguments
    print("positive")
if any(i>0 for i in num): #return True if at least one argument is met with condition
    print("at least positive")

for x in enumerate(num):  #iterate through values and indices
    print("here",x)
