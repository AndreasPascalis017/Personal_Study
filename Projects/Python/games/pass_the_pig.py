# This is a turn based dice game. Where a player will roll a die and see how much they got
# When you hit a number that's not 1 you get to accumulate your total point and reroll your die.
# however the moment you got 1 you will lose all your current point. which means you have to know how many times you want to roll and know when to stop.
# the winner is decided with whoever manage to reach a certain points first.

# The general step will be:
#   allowing player to roll a die with random chance to get 1 to 6.
#   ask them if they want to reroll
#       if they do we'll take their total point add them and stop their turn
#           check if their total point has exceeed the total point and declare them winner
#   start other player turn.

import random


def die_roll():
    min_die_value = 1
    max_die_value = 6
    # randint as the name suggest will give random integer value based on your set parameter (1 - 6)
    die_roll = random.randint(min_die_value, max_die_value)

    # Remember, return value is similar to print in essence you will get the result of your function.
    return die_roll


# For example the line below is how you call a function
# value = die_roll()
# print(value)

while True:
    players = input("Enter number of participants (2 - 5): ")
    if players.isdigit():
        # we use int here to convert that we input above which is a string to an integer.
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            # This else is used when you enter a number yet exceeding your declared limit.
            print("The players must be between 2 - 5")
    else:
        # This else is used when you don't enter a valid number.
        print("Invalid input. Please enter a valid number (2-5).")


winning_score = 30

# this [] is a list used to set each player score. this loop essentially will set a 0 score value based on how many players participating
# if the number of players is 3 that means this list will run a loop 3 times and setting each player's initial score so it becomes [0, 0, 0]
# underscore (_) is python conventional way to show that the name of the variable use in loop is not important. you can fill it if you want but you can use _ if the variable is not important enough to be assign a name.


player_scores = [0 for _ in range(players)]

# print(player_scores)
# For example if i enter 5 players:
#   Enter number of participants (2 - 5): 5
#   [0, 0, 0, 0, 0]

while max(player_scores) < winning_score:

    for player_id in range(players):
        print(f"\nPlayer {player_id + 1} turn.")
        print(f"Your total score is: {player_scores[player_id]}\n")
        current_score = 0
        # the loop below works by asking whether you want to roll. as long you don't roll a 1 the loop will continue and your score will keep being added
        # the moment you roll 1 your turn is over and it will be the next player turn.
        while True:
            # if you respond with y it'll roll the die, other than that it means you are ending your turn.
            roll_start = input("Would you like to roll (y) ? ")
            if roll_start.lower() != "y":
                break

            value = die_roll()
            if value == 1:
                print("You just rolled a 1! Your turn over")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")

            # here your cummulative score will be shown
            print(f"Your current score is: {current_score}")

        player_scores[player_id] += current_score
        # the moment you end your turn it'll break through the current loop and show your total score
        # then it'll re enter the loop for the next player's turn
        print(f"Your total score is: {player_scores[player_id]}")

winner_score = max(player_scores)
winner_id = player_scores.index(winner_score)
print(f"Player {winner_id + 1} with a score of {winner_score} is the winner!!!")
