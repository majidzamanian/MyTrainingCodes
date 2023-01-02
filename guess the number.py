import random
import math

lower = int(input("what is your lower bond? "))
higher = int(input('what is your higher bond? '))
x = random.randint(lower,higher)
y = round(math.log(higher-lower))

print("you have only",y ,"chance to guess the number")

count = 0

while count < y:
    count+= 1

    guess = int(input("guess the number? "))
    if guess == x :
        print("well down! the number was ",x)
        break
    elif guess > x:
        print("too high!")
        print("you can only ",y- count ,"time to try")
    elif guess < x:
        print("too small")
        print("you can only ",y-count, "time to try")

if count>= y:
    print("the number was ",x )
    print("\tBetter Luck Next time!")
