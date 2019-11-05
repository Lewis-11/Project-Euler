import math
num=str(math.factorial(100))
sum=0
for digit in num:
    sum+=int(digit)
print(sum)