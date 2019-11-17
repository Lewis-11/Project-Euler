f = open('EX_22_names.txt','r')
n = sorted(f.read().replace('"','').split(','))
sol = 0
for i in range(len(n)):
	x = 0
	for c in n[i]:
		x+= ord(c)-64
	sol += x*(i+1)
print(sol)
