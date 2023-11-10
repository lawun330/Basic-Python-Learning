#(background running in) file open, read and write with python 
#eg >>
file=open("C:\\Users\\user\\Desktop\\a.txt", "w") #State open to do what #save the directory and state with some variable
file.close() #close from that file


#-----------------------------------------------------------------------
#The followings are choices /yes or no will be according to the order
#-READ  
#-WRITE
#-CREATE file if not existed
#-TRUNCATE file to zero length
#-CURSOR position

#these are file MODEs  >  open("dir\\filename.format","MODE")
#--"r" yes no no no beginning
#--"r+" yes yes no no beginning
#--"w" no yes yes yes beginning
#--"w+" yes yes yes yes beginning
#--"a" no yes yes no end
#--"a+" yes yes yes no end

#--** "MODE" + "b" means binary mode for files with binary data (eg. images)
#--**  "wb" means write in binary mode(suitable  for non-text files)/ "rb" means read in binary
#------------------------------------------------------------------------


#ReadFunction  #ALWAYS READ FROM LAST POINT
#=============================================
file=open("C:\\Users\\user\\Desktop\\a.txt", "r") 
print(file.read(15)) #read only 15 bytes
print("!!!!limited bytes reached!!!!")
print(file.read(3))#continue reading for next succeeding 3 bytes #file.read(-48) acts as file.read()
print("///continued///")
a=file.read() #read the remaining whole file  #stored in a variable 'a'
print(a)
file.close()

print("________restart_______")
file=open("C:\\Users\\user\\Desktop\\a.txt", "r") 
print(file.readlines()) # read all lines and stored as list 
# print(file.read()) # read a single line
file.close()
print("'-----ENDED-----'")


#for loop + read
print("for loop + read >>>");
file=open("C:\\Users\\user\\Desktop\\a.txt", "r") 
for line in file :
    print(line)#print each line and separated by blank because of print


#Write function  #using "w" ALWAYS RESET the STRING
#===============================================
file=open("C:/Users/user/Desktop/b.txt","w")
s=file.write("Watche me take a good thing and\nfucked it all up in one night.\n") #write strings #assign new variable
print("The BYTE is",s) #return byte #that byte is equal to len("written string")
file.close()

#>>with<<< Keyword and >>as<< (known as "context manager")
#============================
with open("C:/Users/user/Desktop/b.txt","r+") as filo:  #auto close file after done
    print(filo.read())
    filo.write("GOOD FOR A WHILE")
    print(filo.read())



#THE COMPLETE FORMS-
#**********VariableNamesForFile=open("dir\\filename.format","MODE")
#**********AssignedVariable.read(number of bytes/number of characters)
#**********AssignedVariable.readlines()
#**********AssignedVariable.readline()
#**********AssignedVariable.write("The string to be written")
#**********with open("dir/filename.format")as VariableNamesForFile: AssignedVariable.read()   
#**********AssignedVariable.close()


# return the index position in the current file
# f.tell() 

# change the starting position with 'x' as an index
# f.seek(x) 