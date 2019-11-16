pen=[]
for n in range(1000,10000):
    pen.append(n*(3*n-1)/2)

for i in pen:
    for k in pen:
        if not i==k and k>i and k<1000*i:
            suma=k+i
            dif=k-i
            if dif<0:
                dif*=-1
            if (suma in pen) and (dif in pen):
                print(dif)
            