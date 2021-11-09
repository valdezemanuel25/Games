import random

# get inpute from the user
player_choice = input("Rock, Paper, Scissors\n")

# create list of choices for the computer to pick
possible_actions = ["r" , "p", "s"]

# random choice picks a random letter from the list
computer_play = random.choice(possible_actions)

# this prints the player's' choice and the computers choice
print(f"{player_choice} vs {computer_play}")

if player_choice == computer_play:
    print("Tie")
elif player_choice == "r":
    if computer_play == "p":
        print("lost")
    else:
        print("you won")
elif player_choice == "p":
    if computer_play == "r":
        print("you won")
    else:
        print("you lost")
elif player_choice == "s":
    if computer_play == "p":
        print("you won")
    else:
        print("you lost ")
