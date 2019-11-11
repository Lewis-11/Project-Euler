import math
def isPrime(n): #check if n is prime
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True



#we can omit 8-pandigital and 9-panfigital as they are all divisible by 9.
for i in range(7654321,1234567,-1):
    digits=[1,2,3,4,5,6,7]
    flag=True
    for j in str(i):
        if int(j) in digits:
            digits.remove(int(j))
        else:
            flag=False
            break
    if flag:
        if isPrime(i):
            print(i)
            break