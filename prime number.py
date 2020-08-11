#print prime numbers with range function, if, elif statements and break
Prime=[2]

def prime():
        x=1#x is initial, y is final, N is divided by previous Xs
        y=int(input("To which number - "))
        global u
        u=y
        for n in range(x,y): #this is not necessary
                for a in range(2,n):
                        if n%a==0:
                                break
                        else:
                                if a==n-1:
                                        p=n
                                        Prime.append(p)
        print('prime=',Prime)

def check_prime():
        num=int(input("Check :"))
        if num in Prime:
                print(num,"is in a prime")
        elif num not in Prime:
                print(num,"is not a prime")
                        
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

j=list(prime_generator(u))
print("prime=",j)