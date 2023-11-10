#printing function
def Print(x,y):
    print('even=',x,'\t','odd=',y)
    
#method1 - even and odd separated by %(remainder)
even=[]
odd=[]
for i in range(0,101):
    for n in range(0,101):
        if i==100:
            print('even=',even)
            print('\n')
            print('odd=',odd)
            break
    if i%2==0:
        even.append(i)
        continue
    odd.append(i)
print("\nother_way\n")
#######################################

#method2 - use of itertools

import itertools as it  
evens=it.count(0,2)
e=list(next(evens) for i in range(50)) #for next 50 numbers

odds=it.count(1,2)
o=list(next(odds) for i in range(50))
Print(e,o)

print("\nother_way\n")
#######################################

#method3 - use of recursion (functional programming)
#search for even
E=[]
O=[]
def is_even(x):
    if x==0:
     return True
    else:
     return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

ALL=tuple(is_even(i) for i in range(100)) #make a total of 100 (trues and falses with true being even)

All=list(enumerate(ALL)) #number it by enumerating

#check the tuple and separate
for a in range(100):
    if All[a][1] == True: 
        E.append(All[a][0])
    else :
        O.append(All[a][0])
Print(E,O)