#basic calculator design with +,-,*,/,%,**

def func1():
    d=0
    r=0
    while d==0:
        a=float(input("First number : "))
        c=input("Operation :")
        b=float(input("Second number : "))
        if c=='A' : d=a+b
        elif c=='S': d=a-b
        elif c=='M': d=a*b
        elif c=='D':
            if b<a:
                t=input("(I)nteger,(D)ecimal?  You typed:")
                if t=='I':
                    d=int(a/b)
                    r=int(a%b)
                elif t=='D':
                    d=(a/b)
            else:
                print("ERROR!!!")
                print('returning...')
                print('\n')
                main()
        elif c=='P' : d=a**b
        elif c=='R' : d=a**(1/b)
    print('\t')       
    print('The answer is', round(d,3))
    if r!=0:print('The remainder is',r)
    key=input("press Q to reset\n")
    print('\n')
    if key=='Q':main()

def main():
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
key=input("Enter 'S' to start\n")
print('\t')
if key=='S':
    main()

