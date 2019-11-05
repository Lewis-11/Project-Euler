import math
list=[2]
i=3
prime=True
while True:
    print(i)
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            prime=False
    if prime:
        list.append(i)
    i+=2
    prime=True
    if len(list)==10001:
        break
print('final' + str(list[10000]))