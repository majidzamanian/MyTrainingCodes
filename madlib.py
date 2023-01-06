# Mad libs generator is a fun game that is usually played by kids. In this python game user has to enter substitutes for blanks in the story without knowing the story. It will be fun to read aloud the stories after filling the blanks.
answer = input(f"do you wanna hear a story about your self? ")
if answer == "yes":
    name = input(f"what is yout name? ")
    future = input(f"what do u want the most to do and learn? ")
    country = input(f"what country do u whant to go? ")
    story = f"{name} in the year 2023 will learn {future} and will earn money form it. he/she may be do {future} in the {country} country"
    interest = input(f"what do you intrest in? ")
    do = input(f'what wo you want to do with your interest? ')
    story_2 = f"you are interested in {interest} and want to do {do} with your pation. "

    print("story number one: " + story)
    print("story number two: " + story_2)
elif answer == "no":
    print("ok")