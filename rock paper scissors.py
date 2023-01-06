import random

box = ["rock", "paper", "scissors"]
y = random.choice(box)

curent_lvl = 2
Final_lvl = 4
your_score= 0
computer_score = 0




while curent_lvl <= Final_lvl:

    choose = str(input("what is your weapon? Rock, paper or scissors? "))
    if choose == y:
        print(f"tie! dont worry you have still {Final_lvl-curent_lvl} times more try")
    elif choose == ("paper") and y == ("rock"):
        print(f"you with {choose} won agenst computyer {y}\n  you have  {Final_lvl-curent_lvl} times more try" )
        curent_lvl += 1
        your_score +=1
    elif choose == ("paper") and y == ("scissors"):
        print(f"you with {choose} lost agenst computyer {y}\n you have  {Final_lvl-curent_lvl} times more try" )
        curent_lvl += 1
        computer_score += 1
    elif choose == ("rock") and y == ("scissors"):
        print(f"you with {choose} won agenst computyer {y}\n you have  {Final_lvl-curent_lvl} times more try" )
        curent_lvl += 1
        your_score += 1
    elif choose == ("rock") and y == ("paper"):
        print(f"you with {choose} won agenst computyer {y}\n you have  {Final_lvl-curent_lvl} times more try" )
        curent_lvl += 1
        your_score += 1
    elif choose != box:
        print(f"wrong vocabulary " )


if your_score > computer_score:
    print(f"congrate you won against computer with you {your_score} and computer {computer_score}")
elif your_score < computer_score:
    print(f"sorry you lost against computer with you {your_score} and computer {computer_score}")
elif your_score == computer_score:
    print(f"that was a tie with you {your_score} and computer {computer_score}. such a chance :) ")

print('Level Ends')



