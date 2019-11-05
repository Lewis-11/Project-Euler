from decimal import *
getcontext().prec=4000
greater=0
maxlength=0
for i in range(1,1000):
    if not i%2==0:
        foundreminders=[]
        flag=True
        rem=1%7
        foundreminders.append(rem)
        while len(foundreminders)<1000 and flag:
            rem=(10*rem)%i
            if rem==foundreminders[0]:
                if len(foundreminders)>=maxlength:
                    maxlength=len(foundreminders)
                    greater=i
                flag=False
            else:
                foundreminders.append(rem)
print(maxlength)
print(greater)