#print prime numbers with range function, if, elif statements and break
#newbie code
Prime=[]

def prime():
        n=int(input("Upper limit number - "))
        global U #to use in both prime functions
        U=n
        Prime.append(2) #2 is a first prime 
        for num in range(2,n): # to calculate each number between 2 to n
                for a in range(2,num): #to find one number if it is prime
                        if num%a==0:
                                break
                        else:
                                if a==num-1:
                                        Prime.append(num)
        print('prime=',Prime)

def check_prime():
        num=int(input("Check :"))
        if num in Prime:
                print(num,"is in a prime.")
        elif num not in Prime:
                print(num,"is not a prime.")
                        
prime()
check_prime()

######################################################
#a new prime number function using yield
def is_prime(a):
        for n in range(2,a):
                if a%n==0:
                        return False
                else: 
                        if n==a-1:
                                return True

def prime_generator(u):
        num=2
        yield 2
        while num<u:
                is_prime(num)
                if is_prime(num)==True:
                        yield num
                num+=1

j=list(prime_generator(U))
print("prime=",j)