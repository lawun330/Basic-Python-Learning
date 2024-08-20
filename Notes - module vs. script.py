'''This file explains the difference between a module and a script. It is not to be executed.'''

# module is a file to be used and imported
# script is a file that may use modules but its purpose is executing some outputs

### EXAMPLE
import math  # this is a module being imported

def function1():
	print(math.pi)

function1()

## the above code is a script that uses a module

# ADDITIONAL NOTES
##################
## when the file is used as a module (imported), its (module's) block of codes inside if __name__=='__main__': won't be executed
## this is convenient when the file itself is a script but can be used as a module too

### EXAMPLE 
## this block of codes is executed when the file is run directly (not imported, used as a script)
## this block of codes is not executed when the file is imported (used as a module)
if __name__=='__main__':
	x = 4  # if this is in a module, 'x' cannot be accessed from script.py
	print('This is just a script.')
