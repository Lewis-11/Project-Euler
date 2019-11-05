file=open("input18.txt","r")
data=[]
for line in file:
    data.append(line)
for i in range(len(data)):
    data[i]=data[i].split()
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])

#Now that we have our numbers in a matrix we can start selecting the appropiate rout
for i in range(len(data)-2, -1,-1):
    for j in range(len(data[i])):
        data[i][j]=data[i][j]+max(data[i+1][j], data[i+1][j+1])
print(data[0][0]) 

    
    


