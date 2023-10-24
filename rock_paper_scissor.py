import random

options = ["rock", "paper", "scissor"]

running = True
while running:
    player = None
    while not(player == 'rock' or player == 'paper' or player == 'scissor'):
        player = input("\nEnter a choice [ rock | paper | scissor ] :").lower()

    computer = random.choice(options)

    print("\nYour choice: {}\nComputer's choice: {}".format(player, computer))

    if player == 'rock' and computer == 'scissor':
        print("You won!\n")
    elif player == 'paper' and computer == 'rock':
        print("You won!\n")
    elif player == 'scissor' and computer == 'paper':
        print("You won!\n")
    elif player == 'rock' and computer == 'paper':
        print("You loose!\n")
    elif player == 'paper' and computer == 'scissor':
        print("You loose!\n")
    elif player == 'scissor' and computer == 'rock':
        print("You loose!\n")
    else:
        print("Game Tie !!!\n")

    restart = None
    while not(restart == "y" or restart == "n"):
        restart = input("Do you wish to continue(Y/N)? :").lower()
        if restart == 'y':
            running = True
        elif restart == 'n':
            running = False
            print("Game Over! Bye")