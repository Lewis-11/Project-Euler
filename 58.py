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


sidelen=2
diagonals=[1]
primes=[]
count=0
while sidelen+1<=10000000:
    if isPrime(diagonals[-1]+sidelen):
        primes.append( diagonals[-1]+sidelen)
    diagonals.append( diagonals[-1]+sidelen )
    count+=1
    if count==4:
        if len(primes)/len(diagonals) < 0.1:
            print(sidelen+1)
            break
        sidelen+=2
        count=0

        tot=0


