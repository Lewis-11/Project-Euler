import math
number=600851475143
prime=True
for i in range(3, number, 2):
    if number%i==0:
        prime=True
        for j in range(3,int(math.sqrt(i))+1,2):
            if i%j==0:
                prime=False
        if prime==True:
           print(i)


