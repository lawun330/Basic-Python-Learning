#!/usr/bin/env python3

'''This script shows the use of eval() function.
The eval() function is used to evaluate the string like a Python expression.'''

number = input("Put some maths like 1+2 :  ")

# this treats like a string
print(number)

# this treats like an operation or expression
print(eval(number))
