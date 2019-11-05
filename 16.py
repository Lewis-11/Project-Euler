list=[int(a) for a in str(2**1000)]
big=list[0]
for i in range(1, len(list)):
    big+=list[i]
print(big)