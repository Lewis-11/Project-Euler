i=10
while True:
    if len(str(2*i))==len(str(6*i)):
        l2=sorted(str(2*i))
        l3=sorted(str(3*i))
        l4=sorted(str(4*i))
        l5=sorted(str(5*i))
        l6=sorted(str(6*i))
        if l2==l3 and l2==l4 and l2==l5 and l2==l6:
            print(i)
            break
    i+=1