#format function for strings
#===========================
List=['A','B','C','E','S','X','N']
print(List)

string= "Char : {1} {0} {2} ".format(List[3], List[4],  List[5])  #format(E,S,X) /1=S/0=E/2=X >>> {1},{0},{2}=SEX
print(string)

#"{var1},{var2}" is assigned with values by format
a='{b},{c}'.format(c=0,b=1)
print(a)
print()

#rounding a float number
price = 100.23443534
new_price = price * 0.9
print("price = {:.3f} new_price = {:.2f}".format(price, new_price))
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
	print("{:>7.2f}".format(a)) #note - .f counts as one decimal place
print()

#other way of printing variables in string
print("Char : %c %c %c" % (List[3],List[4],List[5]))

#f-string
#this is like .format() but {} takes values from variables instead of parameters in the case of .format()
print(f'Hello {List[4]}')
print()

#useful string functions
#===================

snake=["python","anaconda","VIPeR","cobra"]
print(' '.join(snake))  #join the StoredVar with 'string' #create a string from list
print(snake)
snake[-1]=snake[-1].upper() #change the whole string to upper case 
snake[2]=snake[2].lower() #change the whole string to lower case
print(snake)
print(snake[1].replace("anaconda","mway G")) #a string replaced by string temporarily
print(snake[1])
print()


letter="this is a letter for you"

print(letter.startswith("this")) #check if the string is starts with 'substring' #return True since condition is true
print(letter.endswith("you")) #check if it ends with 'substring'
print(letter.startswith("This")) #return False
print(letter.split(" "))  #create a list from string
print(len(letter)) #the count alphabet of string

space_added_string = "Hello "  #strip function for removing indexes and spaces
print(space_added_string+"!"+space_added_string.strip()+"!")
print()
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
print()

#slicing
s = "hey_there"
print(s[:]) #the whole string
print(s[1::2]) #[start:end+1:increasement] where blank start = 0
#the indexes are fixed as in the string no matter it is parted or not
#if slicing has negative, the string is parted first, then the start point works with increasement
print(s[4:7],'\t',s[-5:7]) #[-x:] means the last x-digit characters of the string in usual order(not reverse)
#[-x:y] means the above line string stops at y (counted from beginning which is 0)
print(s[1:-5]) #[:-x] means the remaining string except last x-digit characters of the string 
#[y:-x] means the above line string starts at y (counted from beginning which is 0)
print(s[-5::2],'\t',s[:-5:2]) #with increasement