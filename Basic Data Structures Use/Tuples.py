#Tuples #immutable VarName and StoredKeys
#VarName=(StoredKeys) , VarName=StoredKeys >>no need of parentheses
#VarName[num] #num starts from 0 and ends in n-1 for n numbers of StoredKey

leaf=("SASUKE","SAKURA","NARUTO")
sand="Garra","Sasori"

print(leaf[2],"fights",sand[0])

#calling whole tuple 
print(leaf)

#print empty tuple and empty string
print('====')
mist=()
rain=''
print(rain,mist) 
print('====','\n')

#slicing
leaf2=leaf[1:] #VarName[start:end+1]
print(leaf2[0],"doesn't love",leaf2[1],'\n') #sliced tuple use

#tuple unpacking
team7=('NARUTO', 'SASUKE', 'SAKURA')
hokage, rogue_ninja, useless = team7 
print(hokage,'and',rogue_ninja,'without',useless)  

#swaping data
hokage, rogue_ninja, useless = rogue_ninja, hokage, useless 
print(hokage,'and',rogue_ninja,'without',useless,'\n')

#tuple with asterisk (*) takes many values as possible
a, b, c, *d, e= (1, 2, 3, 4, 5, 6, 7, 8)
print(*d)
#as *arg in function parameter