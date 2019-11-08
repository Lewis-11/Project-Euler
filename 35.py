import math

def isBorbon(n): #check if n is prime
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

def isCircularPrime(n):
    if n<10: return isBorbon(n)
    else:
        original=n
        a=10**( len(str(n)) -1 )        #rotating digits
        gone=n%10                       #rotating digits
        n=int(n/10)                     #rotating digits
        n=n+(gone*a)                    #rotating digits
        flag=isBorbon(n)
        while not n==original:
            gone=n%10
            n=int(n/10)
            n=n+(gone*a)
            flag=flag and isBorbon(n)
        return flag


count=2 #prime 2 and prime 3
for i in range(6,1000000,6):    #patterns that follows every prime number greater than 3

    if isBorbon(i+1):
        
        if isCircularPrime(i+1):
            count+=1

    if isBorbon(i-1):
        
        if isCircularPrime(i-1):
            count+=1
        
print(count)
        

