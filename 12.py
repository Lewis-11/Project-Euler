import math
counter=1
divs=0  #starts at 1 and not 0 because it will always count the number but will only check until num/2
trinum=0
found=False
while not found:
    trinum+=counter
    for i in range(1,int(math.sqrt(trinum))):
        if trinum%i==0:
            divs+=2
            
    if divs>=500:
        found=True
    divs=0
    counter+=1
print(trinum)
