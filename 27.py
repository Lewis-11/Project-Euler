import math

def isPrime(n):
    if n<=0:
        return False
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(4,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True




maximum=0
aValue=0
bValue=0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n=0
        flag=True
        while flag:
            val=n**2+ a*n+b
            if isPrime(val):
                n+=1
            else:
                if n-1 > maximum:
                    maximum=n-1
                    aValue=a
                    bValue=b
                flag=False
        


print(aValue)
print(bValue)
print(maximum)