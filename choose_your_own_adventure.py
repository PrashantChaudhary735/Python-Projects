import random
name = input("Type your name: ")
print(f"Welcome, to this adventure! {name}")

answer = input("You are on a dirt road, it has come to an end  and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk or 'swim' to swim across: ").lower()
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back): ").lower()
    if answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? (yes/no): ").lower()
        if answer == 'yes':
            print("You talked to the stranger and they gave you gold. You WIN!")
        elif answer == "no":
            print("You ignored the strangers and they are offended. They killed you, you LOSE!")
        else:
            print("Not a valid option. You lose.")
    elif answer == "back":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")


