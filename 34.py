import math

def digitFactorial(n):
    sum=0
    while n>=10:
        sum+=math.factorial(n%10)
        n=int(n/10)
    sum+=math.factorial(n)
    return sum

sol=[]
for i in range(10,10000000):
    if i == digitFactorial(i):
        sol.append(i)

final=0
for i in sol:
    final+=i
print(final)