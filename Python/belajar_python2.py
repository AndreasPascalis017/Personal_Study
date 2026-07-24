# THIS IS CALLED COMPARISON OPERATORS
# numbers comparison
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10 == 10)
print(10 == "10")
print(10 != "10")

# strings comparison
print("new section")
print("bag" > "apple")

# if sections
print("\nNEW SECTION")
print("new section")
temperature = 35
if temperature > 50:  # when using if always remember to include :
    print("true")
    print(f"the temperature is {temperature} which is colder")
elif temperature > 20:
    print(f"The temperature is {temperature} It's nice")
else:
    print("false")
    print(f"the temperature is {temperature} which is lower")
print("Done")

# THIS IS CLEAN CODE SECTION
# though by default the code below is true there is a way to make it cleaner
print("\nNEW SECTION")
age = 22
if age >= 18:
    message = "Eligigble"
else:
    message = "Not eligible"
print(message)

# Example of cleaner code or ternary operator
message = "Eligible" if age >= 18 else "not eligible"
# Some print experiment
print(f"the user's age is {age} which make them {message}")

# LOGICAL OPERATOR SECTION (and, or, not)
print("\nNEW SECTION")
high_income = True
good_credit = False
student = False
# you don't need to declare True because you already did it first
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# the not operator reverse condition
if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# SHORT CIRCUIT SECTION
# It can happen when python interpreted your first condition to be false and terminate the entire operation
# for example with the first condition being high_income the moment its value is False the entire
# operation will be stopped because it already see that the condition is not met
print("\nNEW SECTION")
if high_income and good_credit and not student:
    print("Eligible")

if high_income or good_credit or not student:
    print("Eligible employee")

# CHAINING COMPARISON OPERATOR SECTION
# Age should be between 18 and 65
print("\nNEW SECTION")
age = 22
if 18 <= age < 65:
    print("Eligible age")

# strings to strings comparison are determined by which came first during sort. the one that came later means bigger
if "bag" > "apple":
    print("yes")

# FOR LOOPING SECTION
print("\nNEW SECTION")
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# another way to implement the code
for number in range(1, 4):
    print("Attempt", number, number * ".")

# another implementation (here we started from 1 to 10 with increment 2)
for number in range(1, 10, 2):
    print("Attempt", number, number*".")

# FOR ELSE SECTION
# For example if the a code keep running without meeting the break condition.
print("\nNEW SECTION")
succesful = False
for number in range(4):
    print("Attempt")
    if succesful:
        print("Succesful")
        break
else:
    print(f"you have attempted {number} times and failed")

# NESTED LOOP SECTION
# WE PUT A LOOP INSIDE ANOTHER LOOP
# In neste loop remember that the program will finish the inner loop first before moving to
# first loop so in this case x will start at 0 while y loop will keep on repeating until 2 (0, 1, 2) before x becomes 1.
print("\nNEW SECTION")
for x in range(5):  # this part is called outer loop
    for y in range(3):  # this part is called inner loop
        for z in range(2):  # fun try out
            print(f"({x}, {y}, {z})")

# LITERABLES
print("\nNEW SECTION")
print(type(5))
print(type(range(5)))  # range is one of the complex types

# These types are iterable which mean we can iterate in a for loop
# for x in range(5):  iterable means within the program x can be different value everytime

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:  # this square racket is called list.
    print(x)

# for item in shopping_cart: shopping-cart is a custom object that we created per our need.

# WHILE LOOP
print("\nNEW SECTION")
number = 100
while number < 200:
    print(number)
    # you have re declared the new value to stop the loop otherwise it can cause infinite loop
    number = number + 10

number = 100
while number > 0:
    print(number)
    number = number//2  # or you can use number//=2

# this is a poor way but not a wrong way
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)
# By using command.lower the operator will compare your input intu a lower case so you
# even if you input an upper case QUIT it will be convert into quit finishing the loop
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# INFINITE LOOP
print("\nNEW SECTION")
command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# Personal quiz
a = 0
j = 0
for x in range(1, 10):
    a += 1
    if a % 2 == 0:
        print(a)
        j += 1
print(f"There are {j} even numbers")
# on my solution i chose to make a new variable a = 0 which can be simplify by simply using number
# which is an integer by default reducing the steps required.

# Solution
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"There are {count} even numbers")

# FUNCTIONS SECTION
print("\nNEW SECTION")

# when typing a function give at least 2 spaces for cleaner code

# first_name and last_name are called parameters which is the input


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# print take an input while functions doesn't
# while "Andreas" and "Pascalis" are arguments which you used as the value within your functions
greet("Andreas", "Pascalis")
greet("Val", "Rus")

# there are 2 types of functions
# 1 - that perform a task
# 2 - that return a value


def get_greeting(name):
    print(f"Hi {name}")
    return "..."


# None is the return value that signifying an absent of value
print(get_greeting("Andreas"))

# KEYWORD ARGUMENT
print("\nNEW SECTION")


def increment(number, by):
    return number + by


result = increment(2, 1)
# return can only be used within a function
print(result)
# or you can also use
print(increment(2, 1))
# you can give your argument name to make it easier to read
print(increment(number=2, by=1))

# DEFAULT ARGUMENT
# we can give an argument a default value to fix its value everytime we use it
# but by doing that we must do it after the required parameter which mean default can only be make last


def increment(number, by=1):
    return number + by


# this will still give you the same result as the above.
print(increment(2))

# XARGS
# we usually use this when we wanted to make a functions with multiple arguments
print("\nNEW SECTION")


# we add * in front of the argument
# we use [] for list and () for tuples (tuples is a fix list that cannot be change)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(number)
print(multiply(5, 3, 6, 4))
