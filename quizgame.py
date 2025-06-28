print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

# 1st Question:
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

# 2nd Question:

answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "% of questions correct!")







