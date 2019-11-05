import math

limit = 28123
current=1
abundant=[]
while current <= limit :
    divs=[]
    for i in range(1, int(math.sqrt(current))+1):
        if current%i==0:
            divs.append(i)
            if ( i!= current/i and current/i!= current):
                divs.append(current/i)
            

    sum=0
    for i in range(len(divs)):
        sum+=divs[i]

    
    if sum>current:
        abundant.append(current)
    
    current+=1

abundantsum=[]
for i in abundant:
    for j in abundant:
        abundantsum.append(i+j)

mainlist= list(set(range(limit)) - set(abundantsum))
total=0
for i in mainlist:
    total+=i

print(total)



