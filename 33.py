import math

def getDivs(n):
    divs=[]
    for i in range(1, int(math.sqrt(n))):
        if n%i==0:
            divs.append(i)
            divs.append(int(n/i))
    return divs

nums=[]
dens=[]
for den in range (10,100):
    
    for num in range(10,100):
        if num<den:
            flag=False
            commondigit=0
            for i in str(den):
                if i in str(num):
                    flag=True
                    commondigit=i

                    
            if flag:
                origresult=num/den
                if commondigit==str(num)[0]:
                    newnum=num%10
                    control=1
                else:
                    newnum=int(num/10)
                    control=0

                if commondigit==str(den)[0]:
                    newden=den%10
                    control+=1
                else:
                    newden=int(den/10)
                if newden!=0 and control==1:
                    newresult=int(newnum)/int(newden)
                    if origresult==newresult:
                        dens.append(newden)
                        nums.append(newnum)
finalnum=1
finalden=1

for i in range(len(nums)):
    finalnum=finalnum*nums[i]
    finalden=finalden*dens[i]
numdivs=getDivs(finalnum)
dendivs=getDivs(finalden)
print(finalden/max(set(numdivs) & set(dendivs)))


