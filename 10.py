import math


def isPrime(n):
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(4,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

sum=2+3
for i in range(6,2000000,6):

    if isPrime(i+1):
        sum+=(i+1)

    if isPrime(i-1):
        sum+=i-1
print(sum)