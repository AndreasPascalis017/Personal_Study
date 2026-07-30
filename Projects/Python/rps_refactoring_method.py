# we'll be given three choieces (rock, paper, and scissor)
# if the user input an invalid choice
#   print error
# we will also let the computer to make a decision
# print the result
# determine who's the winner
# ask whether the user want to continue or not
# if yes
#   continue
# if not
#   terminate

import random

# below is what you call constant. this is called DRY (Don't Repeat Yourself) method. when coding it is beneficial to avoid keep repeating the same thing over and over which is how this method came.
# with DRY if in the future you want to change the value of one of your variable you can go to your constant and change your code once and all the program that needs the value of your new constant will automatically change by referencing the value within the constant instead of changing it one by one.

ROCK = "r"
PAPER = "p"
SCISSOR = 's'

emojis = {ROCK: "🥌", PAPER: "📄", SCISSOR: "✂"}
choices = (tuple(emojis.keys()))


# we start our breakdown by making a function to get our choice.
def get_player_choice():
    while True:
        player_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("invalid choices")


# next we breakdown a function to display our choices
# we need to input a parameter to prevent error after making commencing_game function because they are declare within
# that part but now that we turn them into a fucntion we no longer can reference them so now we need to inlcude a parameter inside the function

def display_choices(player_choice, opponent_choice):
    print(f"You chose {emojis[player_choice]}")
    print(f"opponent chose {emojis[opponent_choice]}")

# If you had difficulty or forget on what parameter you should add just look at your function and see
# each parameter you needed to make that function work.


def match_result(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        print("it's a tie")
    elif (
        (player_choice == ROCK and opponent_choice == SCISSOR) or
        (player_choice == PAPER and opponent_choice == ROCK) or
            (player_choice == SCISSOR and opponent_choice == PAPER)):  # in DRY instead of using r, p, s we just assign the constant into the line
        print("You win")
    else:
        print("You lose")


def commencing_game():
    while True:
        player_choice = get_player_choice()

        opponent_choice = random.choice(choices)

        display_choices(player_choice, opponent_choice)

        match_result(player_choice, opponent_choice)

        continue_choice = input("Continue? (y/n): ").lower()
        if continue_choice == "n":
            break


# remember that your entire program now is in function form. to run it you need to call the commencing_game()
# the purpose of modularization is to seperate the entire program to a smaller functions, this method
# will help you when you encounter some bugs or error within you code, by seperating them it make it easier to locate the error and easier to handle
# since you only need to analyst the error part instead of your entire code.

commencing_game()
