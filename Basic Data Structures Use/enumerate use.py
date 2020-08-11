#enumerate function 
#equaling each iteable to count_number

#enumerate(iterable, start=0)

l1 = ["eat","sleep","repeat"] #list
s1 = "geek" #string

# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 

print ("Return type:",type(obj1)) 

print (list(enumerate(l1)) )

# changing start index to 2 from 0 
print (list(enumerate(s1,2)) )
