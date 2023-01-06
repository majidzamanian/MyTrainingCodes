#importing what is necceserly
import random

#the words we want to find in this game
List_Of_Words = ["Navid Afkari", "Shahram Amiri", "Ayaz Marhoni","Mahmoud Asgari","Mahmoud Asgari","Mosleh Zamani","Hossein Soodmand","mahsa amini"]

#selecting a word from list by computer
word = random.choice(List_Of_Words).lower()
count = len(word)

#making a list for gussing by user by using the word choosed from list
list_of_the_word = ["-"] *  count

# the amount of man life
i=5
while count!=0:
    # input a character by user
    choice = input("what is your character?").lower()
    if not choice.isalpha() or len(choice) > 1 or word.find(choice) <0 :
        #lifes
        print(f"you have only {i} life left")
        i-=1
        if i ==0:
            print("game is over")
            break

    #if there was no problem
    else:
        list_of_the_word[word.find(choice)] = choice
        count -=1
        print(list_of_the_word)






