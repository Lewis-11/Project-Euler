file=open("42.txt", "r")
words=sorted(file.read().replace('\"', '').split(','))
val=[]
for i in words:
    suma=0
    for j in i:
        suma+=ord(j)-64
    val.append(suma)
limit=max(val)
count=0
for n in range(1,limit):
    oper=n*(n+1)/2
    if oper>limit:
        break
    while oper in val:
        val.remove(oper)
        count+=1
print(count)