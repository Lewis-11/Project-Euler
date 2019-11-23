string="."
for i in range(1,200000):
    string+=str(i)
print( int(string[1])*int(string[10])*int(string[100])*int(string[1000])*int(string[10000])*int(string[100000])*int(string[1000000]) )