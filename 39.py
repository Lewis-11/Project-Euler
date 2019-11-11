import math
maxi=0
per=0
for i in range(1,1001):
    count=0
    for j in range(1,int(i/2)):
        a=j
        for k in range(1,int(i/2)):
            b=k
            c=math.sqrt((a**2) + (b**2))
            if a+b+c==i:
                count+=1
    
    if count>maxi:
        maxi=count
        per=i
print(per)