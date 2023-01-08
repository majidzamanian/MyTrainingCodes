import string
import random
keys = []
s = string.printable
for i in s :
    keys.append(i)

lengh= int(input("how long do u want your password be? " ))

for g in range (0,lengh):
    print(random.choice(keys),end = '')