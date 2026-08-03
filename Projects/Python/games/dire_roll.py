# In this game the program will ask you whether you want to roll a dice or no
# you will have 2 choices y/n (yes/no)
# If you choose y the program will:
#   generate two random dice number (from 1 - 6)
#   and show the result to you
# If you choose n the program will:
#   print a game over message
#   and end the process/ terminate
# Else (neither of the two)
#   the program will show invalid message
#   and letting ou to retry

import random  # we use random to generate a random integer value
# This play variable is used to keep the program going as long you still choose y.
play = True

while play == True:
    # we used str.lower allow user to enter Y without having error with the condition
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        # This will return a random value between 1 to 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}), ({dice2})")
    elif choice == "n":
        print("Game Over, thank you for playing")
        break
    else:
        print("Invalid choice!")
