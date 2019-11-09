import math

def isPrime(n): #check if n is prime
    if n==0:
        return False
    if n==1:
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

def subPrimes(n):
    right=n
    while right>=10:                #right truncating
        a=10**(len(str(right))-1)               
        right=right%a
        if not isPrime(right): return False
    left=n  
    while left>=10:                 #left truncating
        left=int(left/10)
        if not isPrime(left): return False
    return True
         



solset=[]
i=6
while len(solset)<11:
    i+=6

    if isPrime(i+1):
        if subPrimes(i+1):
            solset.append(i+1)

    if isPrime(i-1):
        if subPrimes(i-1):  
            solset.append(i-1)

suma=0
for i in solset:
    suma+=i
print(suma)