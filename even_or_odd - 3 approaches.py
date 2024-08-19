'''This script is used to determine a number whether it is even or odd using different methods.
Numbers are from 0 to 99.'''

# method 1 - even and odd separated by % (remainder)
print("method 1:\n")

even = []
odd = []

for i in range(0, 100):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print('even=', even, '\n\n', 'odd=', odd)
print("\n##############################################\n")

##############################################

# method2 - use of itertools
print("method 2:\n\n")

import itertools as iter

evens = iter.count(0,2)
e = list(next(evens) for i in range(50)) # for next 50 numbers

odds = iter.count(1,2)
o = list(next(odds) for i in range(50))

print('even=', e, '\n\n', 'odd=', o)
print("\n##############################################\n")

##############################################

# method3 - use of recursion (functional programming)
print("method 3:\n\n")

E = []
O = []

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

ALL = tuple(is_even(i) for i in range(100)) # make a total of 100 (trues and falses with true being even)

All = list(enumerate(ALL)) # number it by enumerating

# check the tuple and separate
for a in range(100):
    if All[a][1] == True:
        E.append(All[a][0])
    else :
        O.append(All[a][0])

print('even=', E, '\n\n', 'odd=', O)

#######################################