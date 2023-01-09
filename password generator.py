import string
import random

#defining the passwrd materials
keys = []
s = string.printable
for i in s :
    keys.append(i)

#the main questions


s = "yes"

#ask user if its over or not

def generator():
    lengh = int(input("how long do u want your password be? "))
    for g in range(0, lengh):
        print(random.choice(keys), end='')



while s == "yes":
    generator()
    if input("\nwanna another password? ") == "no":
        input("\nPress enter to close program")
        break



