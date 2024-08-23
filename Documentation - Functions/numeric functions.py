'''This script documents the built-in numeric functions in Python.'''

num = (6, 7, 3, -376, 673, 67)

# FUNCTION max()
## return the maximum number or character
## work with the same data type only
    ## max() don't know if "string" > number ?
print("maximium: ", max(num)) 


# FUNCTION min()
## return the minimum number or character
print("minimum: ", min(num))


# FUNCTION abs()
## return the absolute value of that number (count from zero)
print("absolute value: ", abs(num[3]))


# FUNCTION sum()
## return the sum of all numbers
print("sum is", sum(num))


# FUNCTION all()
## return True if condition is true for all arguments
if all(i >= 0 for i in num):
    print("All numbers are positive")


# FUNCTION any()
## return True if at least one argument is met with condition
if any(i < 0 for i in num):
    print("There is at least one negative number")
