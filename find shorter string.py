'''This script demonstrates the use of the len() function to find the shortest string among two strings.'''

def shorterString(x, y):
    print('the shorter string is >>>')
    if len(x) < len(y):
        return x
    elif len(x) == len(y):
        return 'both strings are equal'
    else :
        return y

# example
print(shorterString('hello', 'hi'))
