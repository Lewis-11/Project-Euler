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

def primeDivs(n):   #return list of prime divisors
    num=n
    divs=[]
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:

            if isPrime(i):
                num=num/i
                append=i
                while num%i==0:
                    num=num/i
                    append*=i
                divs.append(append)
            
            elif isPrime(int(num/i)):
                num=int(num/(num/i))
                append=int(num/i)
                while num%(int(num/i))==0:
                    num=int(num/(num/i))
                    append*=int(num/i)
                divs.append(append)
    if isPrime(num):
        divs.append(num)
            
    return divs


for i in range(10000,1000000):
    firstdivs=primeDivs(i)
    if len(firstdivs)==4:
        second=primeDivs(i+1)
        if len(second)==4:
            third=primeDivs(i+2)
            if len(third)==4:
                fourth=primeDivs(i+3)
                if len(fourth)==4:
                    if not ( set(firstdivs) & set(second) & set(third) & set(fourth) ):
                        print(i)
                        break



                





        
