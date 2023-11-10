#Dictionary #can be add #immutable key  #mutable value
#key is a index name in a dictionary and it has value
#Dictionary = {key : value}
#Dictionary = {keys} is called a set (immutable) #explained in "set use.py"

x={"M": "1234", 2: "BINARY", True: 1, False : '0'}

x["empty"]=None #adding a new key and value to a dictionary

print('original -',x)

x["M"]="moon" #rewriting value
del x[2] #deleting key-value pair

print('modified - ',x)
print()

#########################################

#in and not in 
#used to check a certain key in dictionary and return boolean
#it does not search individual string  #'s' in 'sun' will not be found

print('M' in x)
print('0' in x)
if 'M' in x :
    print("Yes, ",x["M"] + " is a key")
if '0' in x:
	print("It is a value")  #this doesn't print out since it is not a key

print()

#########################################

#used to get value in dictionary by giving keys
print(x.get("M") == x["M"]) #proof that they are the same
print()

#.get() function 
print(x.get("1234"))  #can search for only key #Always return something (None) or AssignedWord
print(x.get("1234","Replaced_texts")) #if return is None, it is replaced by "ANY_TEXT" 
print(x.get(True,"Replaced_texts")) #if return is not None, it returns the actual value

print()

########################################

#get only keys of the dictionary
print(x.keys())
#or
for key in x:
	print(key, end=" ")
print()

#get only values of the dictionary
print(x.values())
print()

#get both
print(x.items())
#or
for key, value in x.items():
	print('{key} : {value},'.format(key=key,value=value),end=" ")
print()
#######################################
y = {'a' : 1, 'b' : 2}
x.update(y) #add other_dictionary's key-value pairs #same as list.extend(other_list) in 'List functions.py'
print(x,y)

y.clear()#clear the dictionary
print(x,y)