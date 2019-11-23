import math

def isPrime(n): #check if n is prime
    if n==1 or n==0 or n<0:
        return False
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

last=0
primes=[]
for i in range(6,1000000,6):
    if isPrime(i-1):
        primes.append(i-1)
    
    if isPrime(i+1):
        primes.append(i+1)


suma=0
for i in primes:
    suma+=i
    if suma>=1000000:
        suma-=i
        break

if isPrime(suma):
    print(suma)
else:
    for i in primes:
        suma-=i
        if isPrime(suma):
            print(suma)
            break
    
            