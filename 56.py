def digitsum(num):
    num=str(num)
    suma=0
    for i in num:
        suma+=int(i)
    return suma

maxval=0
for a in range(1,100):
    for b in range(1,100):
        maxval=max(maxval, digitsum(a**b))
print(maxval)
