#the functions related with list
#mutable var and storedVar
#the keywords 'in' and 'not'
#var=[StoredVars]

Days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',678]
Years=[2017,2019,2019,2019,2020,2020]
print(Days)
print(Years)

if 'Friday' in Days : print ("true")
if '2018' not in Days:print("TRUE")

print('Friday is at Days[',Days.index('Friday'),']') #index funtion for finding the placed number of StoredVar  #listName.index(StoredVar)

Years.append(2021) #add 2021 from last
Years.insert(1,2018) #(at this selected place, insert 2018)

Days.remove(678) #remove
Years.reverse() #make it reversed order

print(Days)
print(Years)

print("There are",Years.count(2020),"2020s in the Years") #count the lapping of 2020
print("There are",Years.count(2019),"2019s in the Years")

print(max(Days),'has the longest string') #return max string
print(min(Days),'has the shortest string') #return min string

lim=Years[0:7:2] #slice the list #listName[start : end+1 : increasement] #if increasement=-1 >>> it can be reversed
print("lim=",lim) 
lim=lim[4::-1] #as ever, -1 means last digit #in  listName[4:(empty):-1] >>> (empty)!=0
print("NewLim=",lim)
lim=lim[-2]
print("Newest=",lim)

math=[i*2 for i in range(11) if i%2 != 0 ] #multiply with  2 if the num is odd
print("odds have become",math)

#newly added informations

List = [1,2,3,4,5]

List2 = List.copy() #copy the list

List2.pop(-1)  #remove the element by means of index #remove() is by means of element
print(List, List2)

List.clear()	#clear the list

List2.extend(Years) #extent elements from one list to the main_list #same as dictionary.update(other_dict) in 'dictionary use.py'

print(List, List2)