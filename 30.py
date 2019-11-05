upperBound=355000
start=2
selected=[]
for i in range(start,upperBound):
    number=str(i)
    tot=0
    for digit in number:
        tot+=(int(digit)**5)
    if tot==i:
        selected.append(i)

print(selected)
output=0
for i in selected:
    output+=i
print(output)