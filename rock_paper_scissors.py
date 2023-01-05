import random

box = ["rock", "paper", "scissors"]
y = random.choice(box)
choose = str(input("lets play Rock, paper, scissors. we only have 1 rounds. lets go. what is your weapon? Rock, paper or scissors? "))

if choose == y:
    print("tie!")
elif choose == ("paper") and y == ("rock"):
    print(f"you with {choose} won agenst computyer {y}" )
elif choose == ("paper") and y == ("scissors"):
    print(f"you with {choose} lost agenst computyer {y}" )
elif choose == ("rock") and y == ("scissors"):
    print(f"you with {choose} won agenst computyer {y}" )
elif choose == ("rock") and y == ("paper"):
    print(f"you with {choose} won agenst computyer {y}" )
elif choose != box:
    print(f"wrong vocabulary " )




