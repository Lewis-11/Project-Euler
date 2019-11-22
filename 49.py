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

def fourDigitPrimes():
    primes=[]
    for i in range(1002,10006,6):
        if isPrime(i+1):
            primes.append(i+1)
        
        if isPrime(i-1):
            primes.append(i-1)
    return primes

found=False
primes=fourDigitPrimes()
for i in range(1000,5000):
    for j in primes:
        if not (j==1487 and i==3330):
            if j+i in primes and j+i+i in primes:
                first=list(str(j))
                second=list(str(j+i))
                third=list(str(j+i+i))
                if (set(first) | set(second) | set(third)) == (set(first) & set(second) & set(third)):
                    found=True
                    print(str(j)+str(j+i)+str(j+i+i))
                    break
    if found:
        break