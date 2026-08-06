# we'll try to make a slot machine simulation.
# the program will take the user deposit amount and allow them to bet on 1, 2 or 3 line of the slot
# if they succeed we then multiply it by the value of their bet and then add them to their balance

# We used random to simulate the slot machine
# We also need to decide how many items within the machine and how many each line is.

import random

MAX_BET = 10000  # Here we use constant to make a more dynamic and more consistent program
MIN_BET = 10
MAX_LINES = 3

ROWS = 3  # ROW AND COL stand for number of row and number of column.
COLS = 3

# Here we make what items we want to be in the slot machine.
# symbol_count is a dictionary in which we assign a certain value to each emojis (it can be anything)
symbol_count = {
    "💎": 2,
    "💘": 4,
    "🍆": 6,
    "🍒": 8
}

# we use 3 parameters that we'll take form the argument above.


def get_slot_spine(rows, cols, symbols):
    pass


def deposit():
    while True:
        amount = input("Please enter your deposit? $")
        if amount.isdigit():
            # we change the string from the input above into an int.
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be more than 0")
        else:
            print("Please enter a number")

    return amount


# this function is used to pick the amount of lines you are betting on. the principle is almost identitcal to the deposit.
def line_number_pick():
    while True:
        slot_lines = input(
            f"Enter the number of lines you want to bet on (1-{MAX_LINES}): ")
        if slot_lines.isdigit():
            slot_lines = int(slot_lines)
            if 1 <= slot_lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines ")
        else:
            print("Please enter a number")

    return slot_lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must be between {MIN_BET} to {MAX_BET}")
        else:
            print("Please enter a number")

    return amount


def main():
    balance = deposit()
    slot_lines = line_number_pick()

    while True:
        bet = get_bet()
        total_bet_amount = bet*slot_lines

        # We need to check first whether the amount of balance you have actually enough to make the bet.
        if total_bet_amount > balance:
            print(
                f"Your balance is not sufficient to make this bet, your current balance is : ${balance}")
        else:
            break

    print(
        f"You're betting ${bet} on {slot_lines} line(s). Your total betting amount is ${total_bet_amount}")


main()
