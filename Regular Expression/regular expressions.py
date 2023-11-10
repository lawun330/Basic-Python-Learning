#regular expressions work with strings

import re

string=r"@" #a raw string called "ha" desired to be matched
#raw strings don't escape anything which makes regular expression easier

if re.match(string,"wun555@gmail.com"): 
#re.match() matches one string with another starting from the beginning of both strings until one is exhausted
#return false if two strings are no longer matched at any point. 
	print("Match!")
else :
	print ("No match!")

print("\n")

confirmation=re.search(string,"wun554@gmail.com") 
#re.search() check if the desired string matches as string (search for a match)
#return True / False
if confirmation:
	print("vaild email")
	print(confirmation.group()) #return the matched substrings 
	print(confirmation.start()) #return the first matching position
	print(confirmation.end()) #return the last matching position
	print(confirmation.span()) #return the above positions in tuple

else :
	print("It's not an email")

string = r"@gmail"
print (re.findall(string,"wun550@gmail.com is not wun554@gmail.com")) #findall() returns a list containing substrings(of one complete string) that match the desired string 
print (re.finditer(string,"@gmail.com")) #return iterator instead of list
print()

#replacing function sub()
incomplete_email='wun5501email.com'
mistake=r'1email'
complete_email=re.sub(mistake,"@gmail",incomplete_email) #re.sub() is substitution function for replacing raw strings from main strings with new words(strings)
print(incomplete_email,'to', complete_email
#we can then extract the email by using r"[\w.%+-]+@[\w.-]+"
print()

#split function to split the strings or sentences into list
sentence = "A sentence. Second sentence? No It is not!"
example = re.split(r"[.?!]", sentence) #here in split(), special characters act like a normal character that is passed to match
print(example)
#by grouping, ie, '()' , we can include such '.' '!' characters that are in a [] bracket when returning a list. eg - try use re.split(r"([.?!])",sentence)

#learn more in metacharacters.py and Special sequences.py
