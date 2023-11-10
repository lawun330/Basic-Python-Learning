#algorithm for combinations of payment

import itertools as it

money=[3000,3000,1000,100,200] #the money you have #each can be n of money_element # 3 of 3000 means I have 3 $3000 papers
bill=20000 #the total bill you have to pay
ans=[]
for n in range (1,100):  
	for c in it.combinations_with_replacement(money,n):  #n is number of elements in tuple #(3000,20) >> n=2 
	#combinations_with_replacement(x,n)  where x is an original list
	#The process is - (assuming n=2)
	#(first3000,first3000),(first3000,second3000),(first3000,1000),(first3000,100),(first3000,200)
	#(second3000,first3000),(second3000,second3000),(second3000,1000),(second3000,100),(second3000,200)
	#(1000,first3000),(1000,second3000),(1000,1000),(1000,100),(1000,200)
	#(100,3000),(100,3000),(100,1000),(100,100),(100,200)
	#(200,3000),(200,3000),(200,1000),(200,100),(200,200)
	#IT CAN BE OVERLAPPING
		if sum(c)==bill:
			ans.append(c)

payment=set(ans) #avoid overlaps by making a set
print('no of ways are',len(payment),'\n************************')
print('ways-',payment)

#check
# sum_a=0
# method_a = [3000, 3000, 3000, 1000, 1000, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
# for i in a:
#     sum_a+=i
# print(sum_a)