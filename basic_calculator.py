'''This script implements a basic calculator with +,-,*,/,%,**, and **root.
It uses loops, functions, error handling, and sys.exit() functionalities.
Sometimes, the program may not work as expected due to nested loops.'''

import sys

# function to calculate the answer based on the chosen operation
def calculate(first_val, sec_val, operation_input):
    o = operation_input
    ans = 0
    remainder = 0
    
    if o == 'A': ans = first_val + sec_val
    elif o == 'S': ans = first_val - sec_val
    elif o == 'M': ans = first_val * sec_val
    elif o == 'D':
        # the denominator must not be zero
        if sec_val == 0:
            print("The denominator must not be zero.\n")
            loop()  # Restart the entire program

        t = input("(I: Integer, D: Decimal) You typed : ").upper()
        
        # print the integer value
        if t == 'I':
            ans = int(first_val / sec_val)
            remainder = first_val % sec_val
        
        # print the decimal value to three places
        elif t == 'D':
            ans = round((first_val / sec_val), 3)

        else:
            print("Unexpected input entered. The input is outside of operations.\n")
            loop()
    
    elif o == 'P': ans = first_val ** sec_val
    elif o == 'R': ans = first_val ** (1 / sec_val)

    if ans == 0 : # solving return 0 error
        ans = '0'
    return ans, remainder


# function to ask for two numbers and the operation to be performed
def askInputs():
    operations = ['A', 'S', 'M', 'D', 'P', 'R', 'Q']
    d = 0
    r = 0

    # get first number
    try: a = float(input("First number : "))
    except :
        print("Unexpected input entered. The input must be number.\n")
        loop()  # Restart the entire program

    # get operation
    try:
        c = str(input("Operation : ").split()[0][0]).upper() # the input string is spilt as list and take the first character in uppercase
        if c == "Q": # quit the program
            print("Thank you for using my calculator. Quitting...\n")
            sys.exit(0)
        if c not in operations:
            print("Unexpected input entered. The input is outside of operations.\n")
            loop()  # Restart the entire program
    except:
        print("No operation input entered.\n")
        loop()  # Restart the entire program

    # get second number
    try: b = float(input("Second number : "))
    except :
        print("Unexpected input entered. The input must be number.\n")
        loop()  # Restart the entire program

    d, r = calculate(a, b, c) # call the function to calculate

    print('\t')
    print(f'The answer is {d}.')
    if r != 0: print(f'The remainder is {r}.')
    
    key = input("Press 'C' to calculate again or any other key to quit. You typed : ").upper()
    print("")

    if key == 'C':
        loop()
    else:
        print("Thank you for using my calculator. Quitting...\n")
        sys.exit(0)


# function that puts everything to be looped
def loop(): 
    print('Q : exit the program')
    print('A : addition')
    print('S : subtraction')
    print('M : multiplication')
    print('D : division')
    print('P : X power Y')
    print('R : X root of Y\n')
    askInputs()


# the main program
if __name__ == "__main__":
    print("Welcome!")

    key = input("Enter 'S' to start : ").upper()
    print('\t')

    if key == 'S':
        loop()
    else:
        print("Unexpected input entered. Quitting...\n")
