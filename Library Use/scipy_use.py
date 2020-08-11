import numpy as np
from scipy import linalg #import linear algebra
from scipy import sparse
from scipy.sparse import linalg

#so advanced that I understand only determinent
A=np.array([[1,2],[4,5]])
detA=linalg.det(A)
print(A,'\n determinent=',detA)

#PLU
#P for permutation matrix having exactly single one on each row & column
#L for lower triangular with unit diagonal element 
#U for upper triangular
# |
# |\
# | \		- this is lower triangular matrix, anything outside is zero
# |  \
# -----	
P, L, U = linalg.lu(A)
print('\nP\n',P,'\nL\n',L,'\nU\n',U,'\n')

#eigenvalue and eigenvectors
#when linear transformation occurs, the matrix magnitude can be changed ie "stretching/compressing"
#A * v = lambda * v
#A is square matrix
#v is column vector denoted as eigenvector
#lambda is diagonal matrix denoted as eigenvalue

EW, EV = linalg.eig(A)
print('eigen value',EW,'\neigen vector\n',EV)

#solve Equations
# 2x+3y=5
# x-y=2 		x,y???
a=np.array([[2,3],[1,-1]])
v=np.array([5,2])
answer= linalg.solve(a,v)
print(answer)

#sparse library use
B = sparse.lil_matrix((10,10)) #build blank m x n matrix
B[:,:] = np.ones(10) #filled with ones
B.setdiag(np.ones(3)*100) #setting data on diagonal matrix 
print(B)

L=np.array([[1,2,4],[3,7,9],[2,5,6]])
#Linked List format to Compressed Sparse Row format
L.tocsr()

# original L is linked list as 1 2 4 3 0 9 0 5 6 and with their indexes
# 1 2 4
# 3 0 9
# 0 5 6
# CSR fotmatting
# value 		- 1 2 4 3 9 5 6 #left to right, then up to down
# index(Col) 	- 0 1 2 0 2  1 2 #corresponding columns
# Rowptr		- 0     3   5	#1,3,5 are starts of rows, their corresponding position or index

#solve equation
linalg.spslove(matrixA,vectorV)