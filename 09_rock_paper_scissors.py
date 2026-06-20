import random
print("------------ Rock Paper Scissors Game ------------")
options = ["rock" , "paper" , "scissors"]
repeat = "y"
while repeat == "y":
 random_choice = random.choice(options)
 choice = input("enter your choice: ").lower()
 if choice in options:
    if random_choice == "rock":
        if choice == "scissors":
            print("computer choice: rock")
            print("oops you lost")
        elif choice == "rock":
            print("computer choice: rock")
            print("draw !")
        else:
            print("computer choice: rock")
            print("you won !!")
    if random_choice == "scissors":
        if choice == "scissors":
            print("computer choice: scissors")
            print("draw!")
        elif choice == "rock":
            print("computer choice: scissors")
            print("you won !!")
        else:
            print("computer choice: scissors")
            print("oops you lost")
    if random_choice == "paper":
        if choice == "scissors":
            print("computer choice: paper")
            print("you won !!")
        elif choice == "rock":
            print("computer choice: scissors")
            print("oops you lost")
        else:
            print("computer choice: scissors")
            print("draw!")
    
    repeat = input("enter 'y' to repeat 'n' to quit: ").lower()
    if repeat != "y" and repeat != "n":
        print("you didn't enter a valid choice")
        break
 
 else:
     print("oops you didn't enter a valid choice")
print("thanks for playing!")


