frac=[1,2]

def operation(fraction):
    fraction[0]=fraction[0]+2*fraction[1]
    newnum=fraction[1]
    newden=fraction[0]
    return [newnum, newden]

count=0
for i in range(1,1000):
    frac=operation(frac)
    finalFrac=[frac[0]+frac[1], frac[1]]
    if len(str(finalFrac[0]))>len(str(finalFrac[1])):
        count+=1
print(count)

