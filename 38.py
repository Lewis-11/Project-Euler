limit=10001
maximum=0
for i in range(limit):
    if int(i/10**(len(str(i))-1))==9:
        digits=[1,2,3,4,5,6,7,8,9]
        concat=str(i)
        count=2
        while len(concat)<9:
            concat=concat+str(i*count)
            count+=1
        flag=True
        for j in concat:
            if int(j) in digits:
                digits.remove(int(j))
            else:
                flag=False
        if flag:
            maximum=max(maximum, int(concat))
print(maximum)
            