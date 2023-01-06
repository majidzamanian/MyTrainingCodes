#importing what is necceserly
import random

#the words we want to find in this game
List_Of_Words = ["murderers", "rapists", "thiefs"]

#selecting a word from list by computer
word = random.choice(List_Of_Words)
print(word)
count = len(word)

#making a list for gussing by user by using the word choosed from list
list_of_the_word = ["-"] *  count


for i in range (2,-1,-1):
    # input a character by user
    choice = input("what is your character?")
    if not choice.isalpha() or len(choice) > 1 or word.find(choice) <0:
        # the amount of man life
        print(f"you have only {i} life left")

    #if there was no problem
    else:
        list_of_the_word[word.find(choice)] = choice
        choice = input("and ?")
        print(list_of_the_word)






