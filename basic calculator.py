#basic calculator design with +,-,*,/,%,**
#the script where inputs are important
#the loop, the reset, the error avoid

def calculate(first_val, sec_val, operation_input):
    o = operation_input
    ans = 0
    remainder = 0

    if o== 'Q' : return 0
    elif o=='A': ans=first_val+sec_val
    elif o=='S': ans=first_val-sec_val
    elif o=='M': ans=first_val*sec_val
    elif o=='D':

        #the denominator must not be zero
        if sec_val<=0:
            raise Exception("The denominator must not be zero.")
            main()
           
        t=input("(I: Integer, D: Decimal) You typed:").upper()
        #print the integer value
        if t=='I':
            ans=int(first_val/sec_val)
            remainder=first_val%sec_val
        #print the decimal value to three places
        elif t=='D':
            ans=round((first_val/sec_val),3) 

        else:
            print("Unexpected input entered. The input is out of availability.\n")
            main()
    elif o=='P' : ans=first_val**sec_val
    elif o=='R' : ans=first_val**(1/sec_val)

    if ans==0 : #solving return 0 error
        ans='0'
    return ans,remainder


def func1():

    operation = ['A','S','M','D','P','R','Q']
    d=0
    r=0

    while d==0:

        #first number
        try: a=float(input("First number : "))
        except :
            print("Unexpected input entered. The input must be number.\n")
            main()

        #operation
        try:
            c=str(input("Operation :").split()[0][0]).upper() #the input string is spilt as list and take the first character in uppercase
            if c not in operation:
                print("Unexpected input entered.The input is out of availability.\n")
                main()
            if c == 'Q': #quit the program
                return 0
        except:
            print("No operation input entered.\n")
            main()

        #second number
        try: b=float(input("Second number : "))
        except :
            print("Unexpected input entered. The input must be number.\n")
            main()

        d,r = calculate(a,b,c)
        # except: 
        #     print("ERROR!") 
        #     main()

    print('\t')       
    print('The answer is {}.'.format(d))
    if r!=0:print('The remainder is {}.'.format(r))
    key=input("press 'C' to calculate again.\n").upper()
    print('\n')
    
    if key=='C':
        main()
    elif key!='C': 
        return 0 

def main():
    print('Q: exit the program')
    print('A : addition')
    print('S : subtraction')
    print('M : multiplication')
    print('D : division')
    print('P : X power Y')
    print('R : X root of Y\n')
    func1()
            
#d=math.sqrt(x) for RootMeanSquare of x     # math.sqrt(obj) is a method (not function since dot is included)
    
import math
print("Welcome!")
key=input("Enter 'S' to start\n").upper()
print('\t')
if key=='S':
    main()
else: 
    print("Unexpected input entered. Quitting...")