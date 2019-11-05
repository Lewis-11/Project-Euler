def checkp(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        counter=3
        while(counter**2<=n):
            if n%counter==0:
                return False
            else:
                counter+=2
        return True

numprimes=1
n=1
while numprimes < 10001:
    n += 2
    if (checkp(n) is True):
        numprimes+=1