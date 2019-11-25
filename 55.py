def isPalindrome(num):
    return str(num)==str(num)[::-1]

def isLychrel(num):
    testnum=num
    for i in range(1,50):
        testnum+=int(str(testnum)[::-1])
        if isPalindrome(testnum):
            return False
        
    return True

count=0
for i in range(10,10000):
    if isLychrel(i):
        count+=1
print(count)
