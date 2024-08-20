'''This script sets an example of a function using multiple parameters.
The function takes a string input to compare it with the password.
It also raises an error if the password entered is incorrect for defined attempts.
Parameters are pre-defined with default arguments, but they can be overwritten.'''

def checkPassword(string, attempts = 3, message = 'Try again\n'): # attempts and message are parameters with pre-defined arguments
    while True:
        key = input(string)
        if key in ('www, zzz'): # correct passwords entered
            print("Unlocked!")
            break
        else:
            print(message)
        attempts -= 1
        if attempts < 0:
            raise ValueError("Incorrect password")

# example
# checkPassword("Wanna check my password : ") # using pre-defined arguments
# checkPassword("Wanna check my password : ", 2) # overwritting one argument
checkPassword("Wanna check my password : ", 2, 'LOSER\n') # overwritting two arguments
