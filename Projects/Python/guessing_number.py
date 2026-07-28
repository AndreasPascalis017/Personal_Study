# The program will generate a random number within a certain range
# the general structure of the program would be like this
# loop
# the goal of the user is to guess what the correct number is
# if the user give an input that is not a number
#   the program will print error
# if the user give a number
# the program will give a response depending how close the guess is
# if number < guess
#   print your're too cold
# if number > guess
#   print you're too hot
# else
#   print congratulation your guess is correct!

import random

# always remember to use meaningful name for your varables
number_generator = random.randint(1, 100)

# store the user input in another varaible
# to prevent error from inputing an invalid value we are going to use try
while True:
    try:
        guess = int(input("Guess the number between 1 - 100: "))
        if guess < number_generator:
            print("You're too cold")
        elif guess > number_generator:
            print("You're too hot")
        else:
            print("congratulation your guess is correct !")
            break  # don't forget to add break to terminate the process
    except ValueError:
        print("Please enter a number")
