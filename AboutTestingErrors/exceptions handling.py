#exception handling or error jumping #useful for avoiding ERRORS

#keywords= try, except, finally, raise, assert
#try blocks should contain ERRORs to jump to except blocks
#except blocks are skipped if no ERROR results
#finally block is next linking to above executed blocks
#raise is used to raise ERROR as you desired (it can be used inside or outside the except block)
#assert is used for sanity check (check deeply to narrow part)[eg checking a single line]
#if the assert expression is false ERROR COMES OUT

a=0
try :
    b=0
    print("in try block")
    print(a%b)

except ZeroDivisionError: #selected single error
    print("JUMPED")
try :
    print("3"+3)

except (TypeError,ValueError): #selected multiple errors handling
    print("JUMPED AGAIN")

try :
    word='haha'
    print(word/2)

except :    #all errors avoiding
    print("All avoided")
    raise NameError("Actually it is raised") #raise TypeOfError("string to be printed")

finally :
    print("Reconnected part")
    assert (a>0),"0 is 0 you dumbasss"  #the following string is printed for assertion error
