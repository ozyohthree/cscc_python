# FILE: rock_paper_scissors.py
# NAME: Play Rock Paper Scissors
# AUTHOR: Anthony Gimei
# DATE: 5/6/2018
# PURPOSE: Lets user play a game of Rock Paper Scissors vs Computer and displays winner

import random
random_low = 1
random_high = 3
continue_playing = True
your_score = 0
computer_score = 0
choices = ["ROCK", "PAPER", "SCISSORS"]

# rock beats scissors
# paper beats rock
# scissors beat paper
# a tie results in a do-over until a winner is declared

def play_rock_paper_scissors(user, comp):
    user = str(user)
    comp = str(comp)

    the_winner = ""
    if user == comp:
        the_winner = "tie"
    elif user == "1" and comp == "3":
        the_winner = "user"
    elif user == "3" and comp == "1":
        the_winner = "comp"
    elif user == "2" and comp == "1":
        the_winner = "user"
    elif user == "1" and comp == "2":
        the_winner = "comp"
    elif user == "3" and comp == "2":
        the_winner = "user"
    elif user == "2" and comp == "3":
        the_winner = "comp"

    return(the_winner)


while continue_playing:
    computer_choice = random.randint(random_low, random_high)
    # print(computer_choice)
    try:
        user_choice = input("Rock, Paper, Scissors? Enter 1, 2 or 3:\n")
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            # print("You played", choices[int(user_choice) - 1])
            winner = play_rock_paper_scissors(user_choice, computer_choice)
            # print(winner)
            if winner == "user":
                print("You played!", choices[int(user_choice) - 1])
                print("Computer played!", choices[int(computer_choice) - 1])
                print("You Win!")
                your_score += 1
            elif winner == "comp":
                print("You played!", choices[int(user_choice) - 1])
                print("Computer played!", choices[int(computer_choice) - 1])
                print("You Loose!")
                computer_score += 1
            elif winner == "tie":
                print("You played!", choices[int(user_choice) - 1])
                print("Computer played!", choices[int(computer_choice) - 1])
                print("Tie, Play again!")
                continue
            want_to_continue = input("Do you want to play again(Type 'y' or 'yes' to play again)?\n")
            if want_to_continue.lower() == "y" or want_to_continue == "yes":
                continue_playing = True
            else:
                print("Your Score:", your_score)
                print("Computer Score:", computer_score)
                continue_playing = False
        else:
            print("Invalid Choice")
            continue

    except ValueError:
        print("Please Enter Valid Input only... try again")
