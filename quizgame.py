print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

# 1st Question:
answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# 2nd Question:

answer = input("What does GPU stands for? ")

if answer.lower() == "graphical processing unit":
    print("Correct!")
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ")

if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ")

if answer.lower() == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")



