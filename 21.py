import math

def sumOfDivs(n):
    sum=1
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            sum+=i+int((n/i))
    return sum

sum=0

for i in range(1,10000):
    Da=sumOfDivs(i)
    if (not (Da==i)) and (sumOfDivs(Da)==i):
        sum+=i
print(sum)

