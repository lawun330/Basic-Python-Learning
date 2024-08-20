'''This script converts a permission in octal format into a string format of linux style.
It uses a function to convert the octal format to a string format.'''

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # iterate over each of the digits in octal
    for digit_val in [int(n) for n in str(octal)]:
        # check for each of the permissions values
        for value, letter in value_letters:
            if digit_val >= value:
                result += letter
                digit_val -= value
            else:
                result+='-'
    return result

# example
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

