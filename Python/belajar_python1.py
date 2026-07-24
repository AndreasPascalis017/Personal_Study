import math  # math is considered an object
print("Hello World")

student_count = 1000  # Numbers (integer)
rating = 4.99  # Float (decimal)
is_publish = False  # Boolean (yes or no)
course_name = "Python Programming"  # Strings (words using " ")
print(student_count)

# things to note
# use meaningful name for your variables
# use lowercase to name your variables
# use underscore to seperate multiple words (andreas_pascalis)
# use space or format it to have seperate space between the " = "

# you can use double or single quote to use string
# triple quote can be use to write a message


# Strings sections
course = "Python Programming lesson"
print(len(course))
print(course[0])  # 0 is the beginning of the strings
print(course[-1])  # -1 means you will start from the end of the strings
# this means your output will be the first letter to the 3rd
print(course[0:3])
print(course[0:])  # it wil output the entire strings
print(course[:3])  # python will put 0 at default

# Escape sequence
print("THIS IS THE ESCAPE SEQUENCE")
# This is a scenario where you want to put to double quote
course = "Python Programming \'Lesson"
# \n use to make a new line within your strings
print(course)
course = "Python Programming \nLesson"
print(course)

# Formatted Strings
print("THIS IS FORMATTED STRINGS")
first = "Andreas"
middle = "Pascalis"
last = "Tristan"
full = first + " " + middle + " " + last
print(full)
# when normally used do not forget to add " " as a spacing between the strings
# but on formatted strings you will build a structure that will determine how it will be shown first
full = f"{first} {middle} {last}"
# you essentially build a function on how to display it. it's called a prefix
print(full)

full = f"{len(first)} {len(middle)} {len(last)}"
full = f"{len(first)} {2 + 4}"
# in formatted strings you can put any input to be shown
print(full)

# THIS IS STRINGS METHOD
course = "Python Programming Lesson"
# THIS IS CALLED METHOD
# for example this method below is how to print strings in uppercase.
course_capital = course.upper()
print(course.upper())
print(course.lower())
print(course_capital)
print(course)

# strip is to use to remove a white spaces that might be included in your input
name = "  Andreas Pascalis Tristan"
print(name)
print(name.strip())
# find is used to search the index of your choice (remember that python is case sensitive so you have to type it exactly how you typed it)
print(course.find("gram"))
# replace is used to replace a letter with another one
print(name.replace("A", "n"))
# this section is a boolean to determine whether the statement is true or false
print("And" in name)
print("Pyth" not in course)


# THIS IS NUMBERS SECTION
x = 1  # this is integer
x = 1.1  # this is float
x = 1 + 2j  # a + bi this is complex numbers (in python we usually use j)
print(10 + 1)
print(10 - 1)
print(10 * 3)
print(10 / 2)
print(10 // 3)  # to make an integer
print(10 % 3)  # module means returning the remainder of a division
print(10 ** 3)  # to make exponent

x = 10
x = x + 3

# this is how you make augmented
x += 3


print(round(2.9))  # to round a number
print(abs(-2.4))
print(math.ceil(4.1))  # will show you the upper number of the input

# THIS IS INPUT SECTION

x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# this is two different type one is string while one is integer or number
# "1" + 1

# list Falsy
# ""
# 0
# None
print(bool(0))
