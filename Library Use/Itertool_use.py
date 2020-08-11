import itertools as it

name=['H','2','O']
num=[2,3,4]
w=['haha','hehe']


print("permutation is",list(it.permutations(name)),"\n")  #permutation==============================


#count=================================
for i in it.count(-10,2):  #count(x,y)-count from x with y step
	num.append(i)
	if i>11:		#need to set stopping case
		break
print('new num is',num)



#zip_longest============================
a=list(it.zip_longest(name,num)) #create a tuple in a list #eg [(a,b),(c,d)] #can be use for coordinates
#return [(x,NONE)] if the iterable is exhausted
print(a,'\n')


#count in another way==================================
b=it.count(start=-10,step=2) #10,12,14,...
s=list(next(b) for i in range(10))  #for 10 numbers
#next() uses with iterators #extract each element of the list 
#iter() function makes obj(eg-list) iterated one element at a time , making an iterator used with next()
print('s=',s)


#repeat=====================================
#assign the vari with const value up to infinite-th #repeat(repeatedVal,repeatedTime)
all_3=list(it.repeat(3,5)) #repeated 3 for 5 times and list these
print(all_3)


#list======================================
#>>>>>>>>>>>>>>>>>cyc=list(it.cycle(num),2) #repeating the iterating for infinite i.e. 2,3,4,2,3,4,2,3,4,...  #not enough memory occurs



#product================================
print(list(b+a for a,b in it.product(name,w))) #add two strings for n number of products 
#eg-like (x+y+2)(x+2)=(xx+2x+yx+2y+2x+2) >> [(xx),(2x),(yx),(2y),(2x),(2)] is result of product((x,y,2),(x,2))



#takewhile=======================
j=[35,224,2]
print(list(it.takewhile(lambda x:x > 2,j))) #like filter function (func,iterable) 



#accumulate==========
print(list(it.accumulate(range(5)))) #add up to i for accumulate(i)
#range 0 >> 0
#range 1 >> 0+1=1
#range 2 >> 0+1+2=3
#range 3 >> 0+1+2+3=6
#range 4 >> 0+1+2+3+4=10
#the output is 0,1,3,6,10