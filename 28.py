sidelen=2
diagonals=[1]
count=0
while sidelen+1<=1001:
    diagonals.append( diagonals[-1]+sidelen )
    count+=1
    if count==4:
        sidelen+=2
        count=0
tot=0
for i in range(len(diagonals)):
    tot+=diagonals[i]

print(tot)