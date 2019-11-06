#Not even gonna comment I hate this particular problem

flag=True
prod=0
sol=[]
nums=[1,2,3,4,5,6,7,8,9]

for a in range(1,100):
    if not a%11==0:
        for b in range (100,2000):
            flag=True
            nums=[1,2,3,4,5,6,7,8,9]
            if int(str(a)[0]) in nums:
                nums.remove(int(str(a)[0]))
            if a>=10:
                if int(str(a)[1]) in nums:
                    nums.remove(int(str(a)[1]))
            flag=True
            for i in str(b):
                if int(i) in nums:
                    nums.remove(int(i))
                else:
                    flag=False
            if flag:
                prod=a*b
                for i in str(prod):
                    if int(i) in nums:
                        nums.remove(int(i))
                    else:
                        flag=False
            if flag and (not nums):
                sol.append(prod)
                print(str(a)+" * "+str(b)+" = "+str(prod))


solution=list( dict.fromkeys(sol)) #removes duplicates
suma=0
for i in solution:
    suma+=i
print(suma)