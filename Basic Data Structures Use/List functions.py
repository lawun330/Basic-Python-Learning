#the functions related with list
#mutable var and storedVar
#the keywords 'in' and 'not'
#var=[StoredVars]

Days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',678]
Years=[2017,2019,2019,2019,2020,2020]
print(Days)
print(Years)
print(len(Years),len(Days)) #len(list) function to count the StoredVar

if 'Friday' in Days : print ("true")
if '2018' not in Days:print("TRUE")

print('Friday is at Days[',Days.index('Friday'),']') #index function for finding the placed index number of StoredVar  #listName.index(StoredVar)
print() 

Years.append(2021) #add 2021 from last
Years.insert(1,2018) #(at this selected place, insert(add) 2018)

Days.remove(678) #remove
Years.reverse() #make it reversed order

print(Days)
print(Years)
print()

print("There are",Years.count(2020),"2020s in the Years") #count the lapping of 2020
print("There are",Years.count(2019),"2019s in the Years")

print(max(Days),'has the longest string') #return max string
print(min(Days),'has the shortest string') #return min string
print()

lim = Years #make a copy of list
print("ori_lim=",lim)
lim=Years[0:7:2] #slice the list #listName[start : end+1 : increasement] #if increasement=-1 >>> it can be reversed
print("lim=",lim) 
lim=Years[4::-1] #as ever, -1 means last digit #in  listName[4:(empty):-1] >>> (empty)!=0
print("NewLim=",lim)
lim=Years[-2]
print("Newest=",lim)
print()

math=[i*2 for i in range(11) if i%2 != 0 ] #multiply with  2 if the num is odd
print("odds have become",math)

#newly added informations

List = [1,2,3,4,5]
List2 = List.copy() #copy the list
List2.pop(-1)  #.pop(x) removes the element where x=index #.remove(x) removes the element where x=element
List2.remove(1)
print(List, List2)

List.clear()	#clear the list
List2.extend(Years) #extent elements from one list to the main_list #same as dictionary.update(other_dict) in 'dictionary use.py'

print(List, List2)

#nested_lists
#{1} in format(A,B,C,D,etc) is B , B=ListB[3] where 3 in ListB=[b,B,bB,Bb] is Bb , {1} position is replaced by Bb
#{i} in format(0,1,2,,..) and i=list[x] where x in list=[1,'2','aa',...] is '...'/ i is replaced by '...'