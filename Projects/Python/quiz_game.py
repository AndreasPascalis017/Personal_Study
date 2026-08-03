# In this game the user will be ask a couple o questions
# answer corectly will reward them with a score.
# Finally he program will show how many score they got.


print("Welcome participants to the quiz game!!!")

# we asked the user first whether they want to play or not.
play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Let's Begin")
score = 0  # declare score variable to count how much the player scored

answer = input("Who is Mario's brother? ").lower()
if answer == "luigi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("In rock, paper, scissor what beats rock? ").lower()
if answer == "paper":
    print("Correct")
    score += 1

else:
    print("Incorrect")

answer = input("What does NPC stands for? ").lower()
if answer == "non playable characters":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the main character in Hunter x Hunter? ").lower()
if answer == "gon":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Congratulations you've answered all questions")


# use format string to make it shorter
# the line below will show your score in percentage

print(f"Your final score is {score/5*100}%")
