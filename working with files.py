'''This script documents how to work with files in Python.'''

# OPENING AND CLOSING A FILE MANUALLY
## the file is running in the background
## we can open, read, write, and close the file manually

# example
# save the directory with some variable
file = open("C:\\Users\\user\\Desktop\\a.txt", "w") # manually open the file with 'w' mode 
file.close() # manually close the file

#########################################################################

# MODES

# The followings are choices (yes or no will be according to the order)
    # READ
    # WRITE
    # CREATE file if not existed
    # TRUNCATE file to zero length
    # CURSOR position

# these are file MODEs # example: open("dir\\filename.format","INSERT HERE")
    # "r"   -> yes no no no beginning
    # "r+"  -> yes yes no no beginning
    # "w"   -> no yes yes yes beginning
    # "w+"  -> yes yes yes yes beginning
    # "a"   -> no yes yes no end
    # "a+"  -> yes yes yes no end

    # "MODE" + "b" means binary mode for files with binary data (suitable for non-text files) (eg. images)
        # "wb" means write in binary mode
        # "rb" means read in binary mode

#########################################################################

# READING A FILE
## read() # READ A SINGLE LINE, ALWAYS READ FROM LAST POINT

file = open("C:\\Users\\user\\Desktop\\a.txt")
print(file.read(15)) # read only 15 bytes
print("!!limited bytes reached!!")
print(file.read(3)) # continue reading for next succeeding 3 bytes # file.read(-48) is the same as file.read()
print("//continued//")
a = file.read() # read the remaining whole file and store in a variable 'a'
print(a)
file.close()
print("'-----ENDED-----'")

#########################################################################

## readlines() # READ ALL LINES, ALWAYS READ FROM LAST POINT

file = open("C:\\Users\\user\\Desktop\\a.txt")
print(file.readlines()) # read all lines and stored as list
file.close()
print("'-----ENDED-----'")

#########################################################################

## USING FOR LOOP + READ

print("for loop + read >>>")
file = open("C:\\Users\\user\\Desktop\\a.txt")
for line in file :
    print(line) # print each line and separated by a new line because of print

#########################################################################

# WRITING A FILE  
## Using "w" mode overwrites the file

file = open("C:/Users/user/Desktop/b.txt", "w")
s = file.write("Watche me take a good thing and\nfucked it all up in one night.\n") # write strings # assign new variable
print("The BYTE is", s) # return byte # that byte is equal to len("written string")
file.close()

#########################################################################

# OPENING AND CLOSING A FILE AUTOMATICALLY WITH CONTEXT MANAGER 
## USING "with" AND "as" KEYWORDS AUTOMATICALLY CLOSES THE FILE

with open("C:/Users/user/Desktop/b.txt", "r+") as filo:  # auto close file after once it is outside the scope
    print(filo.read())
    filo.write("GOOD FOR A WHILE")
    print(filo.read())

#########################################################################

# SYNTAX

## VariableNamesForFile = open("dir\\filename.format", "MODE")

## AssignedVariable.read(number of bytes/number of characters)

## AssignedVariable.readlines()

## AssignedVariable.readline()
 
## AssignedVariable.write("The string to be written")

## with open("dir/filename.format") as VariableNamesForFile: AssignedVariable.read()

## AssignedVariable.close()

#########################################################################

# POSITION THE CURSOR

# return the cursor index position in the current file
print(file.tell())

# change the starting cursor position with 'x' as an index
x = 2
print(file.seek(x))

#########################################################################
