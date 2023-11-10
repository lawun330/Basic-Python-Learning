#random function in python
#importing(extract) module(random) and variables(pi) or function "from" module
#modules are  .py files
#newbie code

import random
from math import pi, sqrt as square_root #sqrt is an function /import multiple objects /change func name 'as' keyword

m=0
s=round(pi,2)
a=float(input("Enter pi to two decimals to play : "))

if a==s :
    print("The game has started!")
    for i in range(10):
        x=random.randint(1,3)  #(start,end)
        a=int(input("Guess the number between 1 and 3 : "))
        if a==x :
            m+=1
            print("HUhh!")
        else : print("Random number is ",x)

print()
x=random.randint(1,100)
y=round(square_root(x),2) #sqrt(m)
print('Compute the following to know your score.')        
print('x:',x)
a=float(input("Squared root of 'x' to two decimal places: "))
if a==y:
    print("Your score is {}.".format(m))
    print("The squared root of {} is {}.".format(x,y))
    print("Congratulation! You've won the game!!!")
else:
    print("Game over! The answer should be {}".format(y))