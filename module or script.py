#difference

#module is file to be used and imported
#script is the file that may use modules, its purpose is executing some outputs

import math #module imported example

def function1():
	print(math.pi)

function1()

#the above code is script

################

#when the file is used as module (if imported), the script codes inside if __name__=='__main__': won't executed
#Useful when the file itself is script but to be able to be imported too

if __name__=='__main__':
	x=4  #x cannot be accessed through importing module or script.py
	print('This is just script')

################