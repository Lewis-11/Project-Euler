count=0
n=101
trow = [1]
y = [0]
for x in range(max(n,0)):
    for i in trow:
        if i>=1000000:
            count+=1
    trow=[l+r for l,r in zip(trow+y, y+trow)]
print(count)
