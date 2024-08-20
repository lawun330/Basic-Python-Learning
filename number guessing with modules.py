'''This script explains about importing modules.
Modules are Python files with the ".py" file format.

The script shows two kinds of import-
    # importing the whole module
    # importing a part of the module

It also proves that we can change the module name using the keyword 'as'.'''

# import the whole module
import random

# import a module, specifically an item, without a name change
from math import pi  

# import a module, specifically an item, with a name change
from math import sqrt as haha # sqrt is a function # use 'as' keyword to change the name

m = 0
s = round(pi, 2)
a = float(input("Enter pi to two decimals : "))

if a == s :
    for i in range(3): # ask the user to guess the number 3 times
        x = random.randint(1,3)  # (start,end)
        a = int(input("Guess the number : "))
        if a == x :
            m += 1
            print("Huh!")
        else : print("Random number is ", x)

print('\nCompute this to know your score.')

x=random.randint(1,10)
y = haha(x) # equivalent to sqrt(m)
y = round(y, 2) # round it to two decimal places
a = float(input(f"Squared root of {x} to two decimal places: "))

if a == y:
    print(f"Correct answer of finding the squared-root. But your score is {m}.")
else:
    print(f"Game over! The answer should be {y}. No mark for you :(")
