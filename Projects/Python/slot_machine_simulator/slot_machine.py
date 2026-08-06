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

# symbol_value act as a multiplier when you do get that symbol, the rarer it is the bigger the multiplier will be.
symbol_value = {
    "💎": 5,
    "💘": 4,
    "🍆": 3,
    "🍒": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    # we loop through every line or row depending on how many the user input
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        # This loop through the entire column on the current line
        for column in columns:
            # We see whether there's any different symbol within that line in which if there is we break.
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # if they got the same symbol for an entire line they win. They then get the final value multiply by their symbol multiplier.
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
    # we use 3 parameters that we'll take form the argument above.


def get_slot_spin(rows, cols, symbols):
    # All ssymbol can be seen as the reel of the slot machine where it'll spin every symbol available.
    all_symbols = []
    # symbol is the key "💘", while symbol_count is the value each symbol have.
    # symbol.item() is used to get both the key of the symbol "💘" and the value associated with the dictionary.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            # the way this loop work is as follow
            # get the symbol "💘" -> check the value "2" -> it will loop 2 times -> and add the symbol to the list -> within that list 2 spaces are reserved for "💘"
            all_symbols.append(symbol)

    columns = []  # we define our column list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # This part is to prevent the machine from picking the symbol again
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Please enter your deposit $")
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


def spin(balance):
    slot_lines = line_number_pick()

    while True:
        bet = get_bet()
        total_bet_amount = bet * slot_lines

        # We need to check first whether the amount of balance you have actually enough to make the bet.
        if total_bet_amount > balance:
            print(
                f"Your balance is not sufficient to make this bet, your current balance is : ${balance}")
        else:
            break

    print(
        f"You're betting ${bet} on {slot_lines} line(s). Your total betting amount is ${total_bet_amount}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(
        slots, slot_lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_line)
    return winnings - total_bet_amount


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        start = input("Press x to spin (q to quit)")
        if start == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
