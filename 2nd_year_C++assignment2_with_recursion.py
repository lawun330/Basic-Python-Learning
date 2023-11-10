even=0
odd=0
#determine even or odd up to the number 498
#x>498 will return RuntimeError
def is_even(x):
	if x==0:
	 return True
	else:
	 return is_odd(x-1)

def is_odd(x):
	return not is_even(x)

for i in range(10):
	x=int(input("enter 10 numbers up to 498 :"))
	is_even(x)
	is_odd(x)
	if is_even(x):even+=1
	if is_odd(x):odd+=1
print('even=',even,' odd=',odd)