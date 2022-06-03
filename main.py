
import random


options = ["R","P","S"]
computer =random.choice(options)
while True: 
    player = input("Type an alphabet R for rock, P for paper or S for scissors?:").upper()

    if player not in options:
        print("Error, you inputed a wrong alphabet. try again")
    elif player == computer:
            print("player:",player)
            print("computer:",computer)
            print("Tie, try again")    
    elif player == "R":
        if computer == "P":
            print("player:",player)
            print("computer:",computer)
            print("You lose")
        if computer == "S" :
            print("player:",player)
            print("computer:",computer)
            print("You win")
        break   
    elif player == "S":
        if computer == "R":
            print("player:",player)
            print("computer:",computer)
            print("You lose")
        if computer == "P" :
            print("player:",player)
            print("computer:",computer)
            print("You win")
        break
    elif player == "P":
        if computer == "S":
            print("player:",player)
            print("computer:",computer)
            print("You lose")
        if computer == "R" :
            print("player:",player)
            print("computer:",computer)
            print("You win")
        break
