final=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        prod=i*j
        if prod>=100000:
            prod=str(prod)
            a, b, c, d, e, f = prod
            if (a==f) & (b==e) & (c==d):
                print( str(i*j) + '=' + str(i) + '*' + str(j) )
                final=max(final, (i*j))
                
        else:
            prod=str(prod)
            a, b, c, d, e = prod
            if (a==e) & (b==d):
                print( str(i*j) + '=' + str(i) + '*' + str(j) )
                final=max(final, (i*j))
print('MAXIMUM NUMBER: '+ str(final))
