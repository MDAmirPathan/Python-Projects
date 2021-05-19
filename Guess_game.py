import random

attempts_list = []
def show_score():
    if len(attempts_list)<=0:
        print("There is currently no high score,it's your for taking")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))


def start_game():
    random_num = random.randint(1,10)
    print("Hello, welcome to game of guesses")
    player_name = input("What is your name?")
    wanna_play = input("Hi , {} , would you like to play a game of guess?(Enter yes/no)".format(player_name))
    if wanna_play.lower() == "yes":
        show_score()
    attempts = 0   
    while wanna_play.lower() =="yes":
        try:
            guess_num = int(input("Pick a number 1-10:"))
            if guess_num<1 or guess_num >10:
                raise ValueError("please enter a value in range")

            if guess_num==random_num:
                print("Nice! you got it!")
                attempts += 1
                print("It took {} attempts".format(attempts))
                attempts_list.append(attempts)
                show_score()
                play_again = input("Do you wanna play again?(Enter yes/no)")
                random_num = random.randint(1,10)
                attempts = 0
                if play_again.lower() == "no":
                    print("Bye")
                    break
            
            elif guess_num > random_num:
                print("It's lower")
                attempts += 1
            elif guess_num<random_num:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("invalid input")
            print("({})".format(err))
    else:
        print("Bye")


if __name__ =="__main__":
    start_game()