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

# we use list to make a cleaner shorter code instead of using != three times
# one weakness of list however is that it can be modified
# choices = ["r", "p", "s"] can be modifed using choices.modified
# another method we can use is to use tuple instead becaue tuple is a read only list

# This version or rock, paper, scissor we tried to implement a method called modularization
# Which essentially we try to break down a big code into smaller code without changing its functionality
import random

# this is how you assign them to dictionary refer to line 33
# variable = {"types": "assign_type"} to make dictionary
emojis = {"r": "🥌", "p": "📄", "s": "✂"}
choices = ("r", "p", "s")


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
        (player_choice == "r" and opponent_choice == "s") or
        (player_choice == "p" and opponent_choice == "r") or
            (player_choice == "s" and opponent_choice == "p")):
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
