n=140
hexa=[]
pen=[]
while True:
    hexa.append(n*(2*n-1))
    pen.append( int(n*(3*n-1)/2 ))
    hmmm= int(n*(n+1)/2)
    if hmmm in hexa and hmmm in pen:
        if not hmmm==40755:
            print(hmmm)
            break
    n+=1