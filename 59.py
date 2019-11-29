from collections import Counter

encoded_text = list(map(int, open('59.txt').read().split(',')))
#identifyes most common ascii of each of the three groups of the cyphertext
#the xor of this most common ascii woth space ascii(32) should give us the key
key = [Counter(encoded_text[i::3]).most_common(1)[0][0] ^ 32 for i in range(3)]

suma=0
for i in range(len(encoded_text)):
    suma+= (encoded_text[i] ^ key[i%3])

print(suma)