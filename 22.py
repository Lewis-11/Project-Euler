file=open("names.txt", "r")
names=sorted(file.read().replace('\"', '').split(','))
sum=0
for i in range(1,len(names)+1):
    nameVal=0
    for j in range(len(names[i-1])):
        nameVal+=(ord(names[i-1][j])-64)
    sum+=(i*nameVal)
print(sum)