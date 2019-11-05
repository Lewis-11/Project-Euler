import math
possibleNumbers=[0,1,2,3,4,5,6,7,8,9]
lexicographicPosition=1000000
number=""

while len(possibleNumbers)>0:
    posibilities = math.factorial(len(possibleNumbers))
    groups = len(possibleNumbers)
    numsPerGroup = posibilities/groups

    digit=int((lexicographicPosition-1)/numsPerGroup)

    number=number+str(possibleNumbers[digit])

    del possibleNumbers[digit]

    lexicographicPosition=lexicographicPosition%numsPerGroup

print(number)
