"""This script calculates the Fibonacii sequence up to 'n'.""" # this is called the docstrings (documentation strings)

def fibonacii(n):
    a, b = 0, 1 # this is called tuple packing # this line is equal to two statements: a = 0; and b = 1;
    Set = []
    while a < n:
        Set.append(a)
        a, b = b, a+b # this line is equal to two statements: a = b; and b = a + b;
    return Set

# example
x = fibonacii(100)
print(x)
