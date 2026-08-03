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
import random

# this is how you assign them to dictionary refer to line 33
# variable = {"types": "assign_type"} to make dictionary
emojis = {"r": "🥌", "p": "📄", "s": "✂"}
choices = ("r", "p", "s")

while True:
    player_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
    if player_choice not in choices:
        print("invalid choices")
        continue  # we call continue to prevent error by not inputing choices that is not within the dictionary

    # this part is to allowed the computer can pick a random selection within choices variable
    opponent_choice = random.choice(choices)  # in this we use random.choice

    # here i want to try assigning each choice to their respective emoji
    # from what i learned we can do that using dictionary to map them.

    print(f"You chose {emojis[player_choice]}")
    print(f"opponent chose {emojis[opponent_choice]}")

    if player_choice == opponent_choice:
        print("it's a tie")
    elif (
        (player_choice == "r" and opponent_choice == "s") or
        (player_choice == "p" and opponent_choice == "r") or
            (player_choice == "s" and opponent_choice == "p")):
        print("You win")
    else:
        print("You lose")

    continue_choice = input("Continue? (y/n): ").lower()
    if continue_choice == "n":
        break
