import random
import math

#this game is about finding the number you did choose by cumputer

#your lower and higher number to make a list of numbers and then picking from one of them
lower = int(input("lower round? "))
higher = int(input("higher round? "))
count = 0
x = random.randint(lower,higher)
y = round(math.log(higher-lower))

while x > count:
    count += 1
    guess = random.randint(lower,higher)
    print(guess)
    answer = input(f"is the ok? or too high or too low ?")

    if answer == "ok":
        print("yes")
        break

    elif answer  == "too high":
        print('i will try harder')
        print("you can only ",y-count, "time to try")

    elif answer == "too low":
        print('i will try harder')
        print("you can only ",y-count, "time to try")

if count>= x:
    print("the number was ",x )
    print("\tBetter Luck Next time!")

