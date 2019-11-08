def isPalindrome(n):
    n=str(n)
    flag=True
    for i in range(int(len(n)/2)):
        if not n[i]==n[len(n)-1-i]:
            flag=False
    return flag

def decToBinary(n):
    binary=bin(n)
    return binary[2:]

count=0
for i in range(1000000):
    if isPalindrome(i) and isPalindrome(decToBinary(i)):
        count+=i

print (count)
    