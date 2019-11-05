file=open("input13.txt","r")
result=0
for line in file:
    result+=int(line)
print(result)
print("first 10 digits= " + str(result)[:10])