'''This educational script illustrates the use of the numpy library for various operations.

It covers:
- Basic Array Creation
- Array Reshaping
- Matrix Operations
- Attributes
- Statistical Functions
- Slicing
- Copying
- Indexing
- Boolean Operations
- Random Number Generation

This script serves as a practical guide for beginners to understand and utilize numpy effectively.
'''


# %pip install numpy # uncomment this line to install
import numpy as np


# FUNCTION zeros()
## fill zeros to dimension-specified matrix
print('Matrix with 0s')
print(np.zeros((10, 10))) # 10 x 10 zeros
print()

## zeros() and ones() take a single parameter -> (row, col) should be wrapped in second-level parentheses -> ((row, col))

########################################################################################

# FUNCTION ones()
## fill ones to dimension-specified matrix
print('Matrix with 1s')
print(np.ones(5)) # 1 x 5 ones
print()

########################################################################################

# FUNCTION eye()
## create an identity matrix -> need no specifying (row, col)
print("Identity matrix")
print(np.eye(3)) # 3 rows, 3 columns since it is identity
print()

########################################################################################

# CONVERT LIST TO NUMPY ARRAY
## np.array(any_list)
listA = [1, 2, 3, 4, 5, 6]
print(listA, 'vs', np.array(listA)) # a variable for list -> no need [] 
print('Another list into array:')
print(np.array([1, 10, 100, 1000])) # direct list -> need []
print()

########################################################################################

# FUNCTION reshape()
## reshape(row, col) -> reshape the array / matrix into desired shape
print('Reshaped above array:')
print(np.array([1, 10, 100, 1000]).reshape(2, 2))
print()

########################################################################################

# MATRIX OPERATIONS
A = np.array(listA).reshape(2, 3)
B = np.array([0, 1, 2])

print('Matrix A:\n', A) # original
print('A+A:\n', A + A) # addition
print('A-A:\n', A - A) # subtraction
print('A multiplied with constant:\n', A * 2) # multiplication
print('A divided with constant:\n', A / 2) # division
print('Squared A:\n', A ** 2) # square
print('Matrix B:\n', B)
print('Row-wise multiplication between A and B:\n', A[0] * B) # row-wise multiplication
print('Column-wise multiplication between A and B:\n', A[0] * B.reshape(3, 1)) # column-wise multiplication (broadcasting)
print('Hadamard product between B and C:\n', B * np.array([2, 1, 3])) # element-wise multiplication or Hadamard product
	# similar to element-wise multiplication in octave -> .*
	# similar to element-wise division in octave -> ./
print()

########################################################################################

A = np.ones((3, 4))

# ATTRIBUTE shape
## 0 for number of rows
## 1 for number of columns
print('num_row:', A.shape[0], 'num_col:', A.shape[1])

# ATTRIBUTE dtype
## find the data type
print('data type:', A.dtype)
print()

########################################################################################

# change some values
for i in range(A.shape[1]):
	A[i-1] = i # i-1 because arrays start at zero
print("Matrix A:\n", A)

# OTHER FUNCTIONS

print('sum:', np.sum(A)) # sum of everything
print('row addition:', np.sum(A, axis=1)) # axis=0 -> row sum
print('col addition:', np.sum(A, axis=0)) # axis=1 -> column sum

print('STD:', np.std(A)) # standard deviation
print('squared root:\n', np.sqrt(A)) # square roots of each element
print('sin:\n', np.sin(A)) # sine values of each element
print("log:\n", np.log(A)) # log values of each element
print("exponential:\n", np.exp(A)) # exponential values of each element

print("maximum element:", np.max(A)) # return greatest element
print("maximum element:", A.max()) # return greatest element
print("index position of maximum element:", A.argmax()) # return position of greatest element

print("minimum element:", np.min(A)) # return least element
print("minimum element:", A.min()) # return least element
print("index position of minimum element:", A.argmin()) # return position of least element

print()

########################################################################################

# SLICING
## np matrix can be sliced as in Python list
## [start is inclusive : end is exclusive]
print('sliced:', A[2:, 1:2]) # 2: -> 3rd row to end, 1:2 -> 2nd column to 3rd column
print()

# COPYING
## FUNCTION copy()
### the original data is not modified when its copy is modified
original = np.array([2, 312, -4, 45])
copy = original.copy()
print("BEFORE ANY CHANGES\n\toriginal:", original, "copy:", copy)
copy[:] = 0 # change all elements to 0
print("AFTER CHANGING A COPY\n\toriginal:", original, "copy:", copy)
print('- copy() approach does not affect the original.')

## SLICING FOR A COPY [:]
## sliced part is not a true copy; simply holding values!
sliced_copy = original[:]
print("BEFORE ANY CHANGES\n\toriginal:", original, "copy:", sliced_copy)
sliced_copy[:] = 0  # changing all elements to 0
print("AFTER CHANGING A COPY\n\toriginal:", original, "copy:", copy)
print('- slicing approach affects the original.')

print()

########################################################################################

# INDEXING AN ELEMENT
print('2 ways to locate element:', A[1, 1],' is the same as ', A[1][1])

# FANCY INDEXING TO REORDER ROWS
print('rows reordered:\n', A[[2, 0, 1]]) # the third row, followed by the first row, followed by the second row
print()

########################################################################################

# BOOLEAN OPERATIONS AND SELECTION
greater_than_2 = A > 2
print("boolean check:\n", greater_than_2) # return True / False
print("part of matrix A that satifies the check:\n", A[greater_than_2]) # True positions replaced by real numbers
print()

########################################################################################

# RANDOM IN NUMPY

# FUNCTION rand(n) -> returns an array containing 'n' numbers of uniformly distributed values
    ## uniform distribution -> [0.0, 1.0) -> a range between 0 and 1, where 0 is inclusive and 1 is exclusive
# FUNCTION randn(n) -> returns an array containing 'n' numbers of standard normal distribution
# FUNCTION randint(l, size=n) -> returns an array containing 'n' random integers, all less than 'l'
# FUNCTION random() -> returns a single random float in the range [0.0, 1.0)
# FUNCTION arange(start, end, increment) -> returns an array containing numbers
    ## specify the constant difference between values, but not how many numbers there are in the array
# FUNCTION linspace(start, inclusive_end, number_of_values_to_generate) -> returns an array containing numbers
    ## specify how many numbers there are in the array, but not the constant difference

print('rand:', np.random.rand(3)) # 3 uniformly distributed numbers
print('randn:', np.random.randn(2)) # 2 standard normal distributions
print('randint:', np.random.randint(2, size=10)) # 10 random integers under 2
print('random:', np.random.random()) # a single float value

print('arange (end-exclusive):', np.arange(0, 11, 2)) # tips: can generate an arithmetic progression (AP)
print('linspace (end-inclusive):', np.linspace(0, 11, 6)) # tips: can generate an arithmetic progression (AP)
print()

########################################################################################
