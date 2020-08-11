#random function in python
#importing(extract) module(random) and variables(pi) or function "from" module
#modules are  .py files

import random
from math import pi, sqrt as haha #sqrt is an function /import multiple objects /change func name 'as' keyword

m=0
s=round(pi,2)
a=float(input("Enter pi to two decimals : "))

if a==s :
    for i in range(10):
        x=random.randint(1,3)  #(start,end)
        a=int(input("Guess the number : "))
        if a==x :
            m+=1
            print("HUhh!")
        else : print("Random number is ",x)
        
y=haha(m) #sqrt(m)
print("Your score is ",m)
print(m,"squared root is",y)
