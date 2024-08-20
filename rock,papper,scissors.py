import random

game = True

while game:
    options = ["rock","papper","scissors"]
    human = None
    computer = random.choice(options)
    while human not in options:
        human = input("Choice between (rock, papper,scissors) ")

    if human == computer :
        print("computer have choiced ",computer)
        print("you have choiced",human)
        print("Its a Tie!!!")
    elif human == "rock":
        if computer == "paper":
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("computer won!!!")
        if computer == "scissors" :
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("you won!!!")
    elif human == "papper":
        if computer == "scissors":
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("computer won!!!")
        if computer == "rock" :
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("you won!!!")
    elif human == "scissors":
        if computer == "rock":
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("computer won!!!")
        if computer == "papper" :
            print("computer have choiced ",computer)
            print("you have choiced",human)
            print("you won!!!")
    
    play = input("You want to play again(yes/no)").lower()

    if play =="yes":
        pass
    else:
        game= False
        print("The game has ended")