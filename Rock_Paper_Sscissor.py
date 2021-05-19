
import random
import os
import re

os.system('cls')
print("Enter exit to stop playing")

while True:
    print("\n")
    print("Rock paper scissor- shoot!")
    user_choice = input("Choose a weapon [R]ock [P]aper or [S]cissor:")
    if user_choice.lower() == "exit":
        print("Bye")
        break
    if not re.match("[SsPpRr]",user_choice):
        print("choose a valid weapon")
        print(" [R]ock [P]aper or [S]cissor")
        continue

    print(f"Your choice:{user_choice}")

    choices = [ "R" , "P" , "S"]
    comp_choice = random.choice(choices)
    print(f"Computer choice:{comp_choice}")

    if comp_choice == user_choice.upper():
        print("Tie!")
    elif comp_choice == "R" and user_choice.upper() =="S":
        print("Rock beats scissor:Computer Win!")
        continue

    elif comp_choice == "P" and user_choice.upper() =="R":
        print("Paper beats rock :Computer Win!")
        continue

    elif comp_choice == "S" and user_choice.upper() =="P":
        print("Scissor beats paper :Computer Win!")
        continue
    else:
        print("You win!")
        continue



