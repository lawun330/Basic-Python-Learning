#Calling function with several Arguments

def passwords(string,Trials=4,b='Try again\n'):
    while True:
        key=input(string)
        if key in ('www,zzz'):
            print("Unlocked!")
            return True
        else:
            print(b)
        Trials-=1
        if Trials<0:
            raise ValueError("Incorrect password")
        
'''uncomment any of these'''

passwords("Wanna check my password : ")
#passwords("Wanna check my password : ",2)
#passwords("Wanna check my password : ",2,'LOSER\n')

