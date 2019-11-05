sumofsquares=0
squareofthesum=0
for i in range(101):
    sumofsquares+=(i*i)
    squareofthesum+=i
squareofthesum=squareofthesum*squareofthesum
print(squareofthesum-sumofsquares)