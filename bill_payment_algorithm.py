'''This script uses combination to find all possible combinations of payment to pay a bill.

It uses combinations_with_replacement(x, n) where
	# x is an original list
	# n is number of elements in tuple
		## (3000,20) >> n=2

Assuming n is 2. For this particular example, the process is as follows.
	# (first3000,first3000),(first3000,second3000),(first3000,1000),(first3000,100),(first3000,200)
	# (second3000,first3000),(second3000,second3000),(second3000,1000),(second3000,100),(second3000,200)
	# (1000,first3000),(1000,second3000),(1000,1000),(1000,100),(1000,200)
	# (100,3000),(100,3000),(100,1000),(100,100),(100,200)
	# (200,3000),(200,3000),(200,1000),(200,100),(200,200)
'''

import itertools as it

money = [3000, 3000, 1000, 100, 200] # type of money paper you have 
# each can be n of money_element 
	## 3 of 3000 means I have 3 $3000 papers

bill = 20000 # total bill you have to pay
ans = []

for n in range (1, 30):
	for c in it.combinations_with_replacement(money, n):  # there can be duplicates
		if sum(c) == bill:
			ans.append(c)

payment = set(ans) # delete duplicates by making a set
print('no of ways are', len(payment), '\n************************')
print('ways-', payment)
