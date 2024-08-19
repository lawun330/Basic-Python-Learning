'''This script is about a strange thing I found out about Python.'''

# define a function
def a():
    print("hi")

v = a() # v is None
print(v) # it should print None but it also calls the function
