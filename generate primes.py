'''This script prints prime numbers using different approaches. 
It also incorporates if, elif statements, break
and checks the condition with yield.'''

print("Prime number generator begins...\n")

# method 1 - generate prime numbers with a list
prime=[]

def prime_generator1():
        n = int(input("Upper limit number - "))
        global U # global variable to use in both prime functions
        U = n
        prime.append(2) # 2 is the first prime
        for num in range(2, n): # calculate each number between 2 to n
                for a in range(2, num): # find one number if it is prime
                        if num % a == 0:
                                break
                        else:
                                if a == num - 1:
                                        prime.append(num)
        print('method 1 generated primes=', prime)

# example
prime_generator1()

######################################################

# method 2 - generate prime numbers with 'yield'
def is_prime(a):
        for n in range(2, a):
                if a % n == 0:
                        return False
                else:
                        if n == a - 1:
                                return True

def prime_generator2(u):
        num = 2
        yield 2
        while num < u:
                if is_prime(num) == True:
                        yield num
                num += 1

# example
prime2 = list(prime_generator2(U))
print("method 2 generated primes=", prime2)

######################################################

print("\nPrime number checker begins...\n")

# check if a particular number is prime or not
def is_prime_display():
        num = int(input("Check a number:"))
        if num in prime:
                print(num, "is a prime.")
        elif num not in prime:
                print(num, "is not a prime.")

# example
is_prime_display()
