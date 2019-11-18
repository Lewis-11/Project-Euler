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



for i in range(7,10000,2):
    flag=False
    if not isPrime(i):
        for j in range(1,int(math.sqrt(i))):
            dif=i-2*(j**2)
            if isPrime(dif):
                flag=True
                break
        if not flag:
            print(i)
            break