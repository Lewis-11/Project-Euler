import itertools
searchedDivs=[2,3,5,7,11,13,17]
suma=0
pandigitals=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
ints=[]
for i in pandigitals:
    string=""
    for j in range(0,10):
        string+=str(i[j])
    ints.append(string)

for i in ints:
    flag=True
    for j in range(7):
        if not (int(i[j+1:j+4]) % searchedDivs[j] ==0):
            flag=False
            break
    if flag:
        suma+=int(i)
print(suma)
    

    