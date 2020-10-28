import random
from prettytable import PrettyTable

rock = ("👊", "rock")
paper = ("✋", "paper")
scissors = ("✌️", "scissors")

playerPoints, computerPoints = 0, 0

rounds = int(input("How many rounds do you want to play? "))

for _ in range(rounds):
    player = ""
    while player not in ["rock", "paper", "scissors"]:
        player = input("rock, paper, scissors? ").lower()

    computer = random.choice([rock, paper, scissors])
    print(computer[0])

    if player == computer[1]:
        print("draw")
    elif (player, computer[1]) in [("rock", "paper"), ("paper", "scissors"), ("scissors", "rock")]:
        computerPoints += 1
        print("you lose")
    else:
        playerPoints += 1
        print("you win")

results = PrettyTable(["player score", "computer score", "draws"])
results.add_row([playerPoints, computerPoints, rounds - playerPoints - computerPoints])
print(results)
