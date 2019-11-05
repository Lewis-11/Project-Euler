for a in range(1,333):
    for b in range(a,666):
        for c in range(b,1000):
            if (a+b+c==1000):
                if ((a**2)+(b**2))==(c**2):
                    print('a: ' + str(a) + ', b: ' + str(b) + ', c: ' + str(c))
                    print(a*b*c)