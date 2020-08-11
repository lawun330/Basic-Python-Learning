#matrix and np use

import numpy as np 

#print 10 x 10 zeros
print('Zeros??')
print(np.zeros((10,10)))
print('\n')


#print 1 x 5 ones 
print('uses of ones()')
print(np.ones(5))
print('\n')

#NOTE when we want to write matrix for zeros and ones, (row,col) should have double parentheses
#it is because ones() and zeros() only take one parameter

#identity matrix doesn't need to define rows, col
print("identity matrix")
print(np.eye(3))
print('\n')

#change lists into arrays 
#np.array(any_list)
print('list into array!')
a = [1,2,3,4,5,6]
print(a,'vs',np.array(a)) #inserting a variable defined as list #no need []
print('undefined as list')
print(np.array([1,10,100,1000])) # need [] if the list is undefined before
print('\n')

#reshape(desired row,col) - reshape the array or matrix 
print('reshape')
print(np.array(a).reshape(6,1))
print('\n')

#operations
A=np.array(a).reshape(2,3)
B=np.array([0,1,2])
print('a matrix\n',A)
print('addition-\n',A+A)
print('subtraction-\n',A-A)
print('squared-\n',A**2)
print('multiply with constant-\n',A*2)
print('division with constant-\n',2/A) #can also be A/2

print('another matrix\n',B)
print('multiplication between elements of matrices-\n', A*B)
#like like octave ./ or .* stuff
#no function about normal math matrix multiplication
print('\n')


#matrix operations and slicing
I= np.ones((3,4))
print('row-',I.shape[0],'col-',I.shape[1])	#0 for rows / 1 for columns

for i in range(I.shape[1]):
	I[i-1] = i #i-1 because arrays start at zero
print(I)
print('sum=',np.sum(I)) #sum everything
print('std=',np.std(I)) #standard deviation
print('row addition-',np.sum(I,axis=0)) #sum for row or column as axis being variable
print('col addition-',np.sum(I,axis=1))
print('squared root-\n',np.sqrt(I)) #square rooted each element
print('sin- \n',np.sin(I)) #sine values of each element
#np.log(I) - log
#np.exp(I) - exponential (e^)
#np.max(I) or I.max()- return max value within I
#np.min(I) or I.min()- return min value within I
#I.argmin() and I.argmax() return index locations of their corresponding max, min values
print('\n')

#slicing
print('sliced-',I[2:,1:2]) #2+1= 3rd row to end, 1+1= 2nd column to 2+1= 3rd column
#NOTE that [start inclusive : end exclusive]

#indexing
print('2 ways to locate element',I[1,1],' same as ',I[1][1])
#matrix can be sliced as list

#fancy indexing
print('moved',I[[2,0,1]]) #allows in any index order 
print('\n')



#Boolean operations and selections
greater2= I>2
print(greater2)
print(I[greater2])

#random numbers
print('rand ',np.random.rand(2)) #uniformly distributed (0 inclusive to 1 exclusive range)
print('randn ',np.random.randn(2)) #standard normal distribution
print('randint',np.random.randint(2,size=10)) #radom integer up to 2 with size of 10
print('random',np.random.random()) # [0,1) of three times
print('arange',np.arange(0,11,2)) #arange function (start inclu, end exclu, increasement)
#use when you know the differences between value, not knowing how many numbers we will get

print('linspace',np.linspace(0,11,5)) #linspace function (start inclu, end inclu, total no between them)
#use when you know the numbers between, not knowing what each difference is

#to find data type
print('data type',I.dtype) 
print('\n')



#copy() stuff
#They aren't copied, they are holding values!!!!
s=np.array([2,3,4,45])
q=s[1:3]
print('datas',s,'place to changed',q) 
# q=[0,0] 	#this is assigning a completely new values to fixed variable 'q', eg- q='hi'
q[:]=0  #this is changing values of 'q' that holds 's' values ,eg [2,3,4] to [0,0,0]
print('changed datas',s,q) #the old data changed due to new changes

s=np.array([2,3,4,45])
c=s.copy()
c[:]=0
print('unchanged copy',s,c) #unchanged values result in old data as new data has been copied and changed