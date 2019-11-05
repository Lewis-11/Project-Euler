fibonacciSequence=[1,1]
n1=1
n2=1
Sum=0
while len(str(Sum))<1000:
    Sum=n1+n2
    n1=n2
    n2=Sum
    fibonacciSequence.append(Sum)
print(Sum)
print(len(fibonacciSequence))