#fibonacii sequence and heading(docstrings) under the defined function with one argument
#list and return

def fib(n):
    """Fibonacii sequence up to n""" #this is docstrings or documentation strings
    a,b=0,1
    Set=[]
    while a<n:
        Set.append(a)
        a,b=b,a+b
#The above line is meaning that a=b and b=a+b not 3 statments with commas
    return Set

x=fib(100)
print(x)

