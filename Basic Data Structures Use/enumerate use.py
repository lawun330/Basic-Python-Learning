#enumerate function 
#equaling each iteable to count_number

#enumerate(iterable, start=0)

l1 = ["eat","sleep","repeat"] #list
s1 = "geek" #string

# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 

print (obj1,obj2)
print ("Return type:",type(obj1)) #type() returns the type of object

print (list(enumerate(l1))) #make a list with values inside #this is what we usually want to use
print (list(enumerate(s1)))

#change the start index to 2 from 0 
print (list(enumerate(s1,2)))
