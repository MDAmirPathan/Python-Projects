import random

def dice_display(num):
    print(" --- ")
    print(f"| {num} |")
    print(" --- ")


def roll_dice():
    print("Press Enter to roll dice/Enter n or no to quit")
    while True:
        roll_dice = input("Do you wanna roll dice?")
        if roll_dice.lower() == "n" or  roll_dice.lower() == "no":
            print("Bye")
            break
        else:
            num_on_dice = random.randint(1,6)
            dice_display(num_on_dice)
            continue



if __name__ == "__main__":
    roll_dice()






