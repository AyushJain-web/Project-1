import random

game = ["rock","paper","scissors"]

while True:

    computer = random.choice(game)
    user = input("Choose from rock, paper and scissors: ").lower()


    if user == computer:
        print("Computer selected: " + computer)
        print("User selected: " + user)
        print("It's a Tie!")

    elif user == "rock":
        if computer == "paper":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You are defeated!")
        elif computer == "scissors":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You WON!")

    elif user == "paper":
        if computer == "rock":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You WON!")
        elif computer == "scissors":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You are defeated!")

    elif user == "scissors":
        if computer == "rock":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You are defeated!")
        elif computer == "paper":
            print("Computer selected: " + computer)
            print("User selected: " + user)
            print("You WON!")

    else:
        print("Encountered an Error!!! :(\nPlease choose/type correctly!")


    again = input("Want to play again (Yes/No): ").lower()

    if again == "yes":
        continue
    else:
        break

print("Bye Buddy!")

