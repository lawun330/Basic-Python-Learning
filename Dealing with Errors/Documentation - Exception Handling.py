''' This script documents features in exception handling.
When an error is encountered, a program usually halts. 
However, we can program the script to handle errors and continue execution.
This is done using exception handling.

Keywords:
- try: Contains code that might raise an error.
- except: Executes this block if an error is found.
- finally: Executes this block no matter what, typically for cleanup.
- raise: Raises a specified error (can be inside or outside the except block).
- assert: Performs a sanity check; raises an error if the assert expression is false.
'''

########################################################################################

# HANDLING ONE TYPE OF ERROR
try:
    print(0 / 0)
except ZeroDivisionError:
    print("One type of error found!")
print()


# HANDLING MULTIPLE TYPES OF ERROR
try:
    print("3" + 3)
except (TypeError, ValueError):
    print("Multiple types of error found!")
print()


# HANDLING ALL TYPES OF ERROR
try:
    print('a string' / 2)
except:
    print("All errors are avoided!")
print()


# RAISING AN EXISTING ERROR
    ## raise error_type("string to be displayed")
## may create confusion as arbitary error (might be totally unrelated with the actual error) can be raised
try:
    print(a)
except:
    raise TypeError("Actually this error is raised :P")


# ASSERTION FOR SANITY CHECK
    ## assert (expression), "string to be displayed"
## string is printed if an assertion is false
finally:
    print("FINALLY PART")
    assert (0 > 0), "0 is 0"  
