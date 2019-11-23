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

def changeDigit(n,dupDigit,famDigit):
    stri=""
    for i in str(n):
        if int(i)==int(dupDigit):
            stri+=str(famDigit)
        else:
            stri+=str(i)
    if stri[0]=="0":
        return 1
    return int(stri)



primes=[2,3]
for i in range(1002,122000,6):
    if isPrime(i-1):
        primes.append(i-1)
    
    if isPrime(i+1):
        primes.append(i+1)

for i in primes:
    if not len(set(str(i)))==len(str(i)):       #get every number with at least one duplicated digit

        digits=[]
        dup=[]
        for j in str(i):                        #get which digits are actually duplicated
            if not j in digits:
                digits.append(j)
            else:
                if not j in dup:
                    dup.append(j)

        
        flag=False
        #check changing digits and counting primes
        for k in dup:
            count=0
            for j in range(10):            
                if isPrime(changeDigit(i,k,j)):
                    count+=1
            if count==8:
                print(i)
                flag=True
                break
        if flag:
            break

            
        
        
        

        
    