maxn=0
final=0
for i in range(1,1000000):
    n=i
    counter=1
    while not n==1:
        if n%2==0:
            counter+=1
            n=int(n/2)
        else:
            counter+=1
            n=3*n+1
    if counter>maxn:
        maxn=counter
        final=i
print(final)