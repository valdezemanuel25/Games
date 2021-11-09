import random

player_choice = input("Rock, Paper, Scissors\n")
possible_actions = ["r" , "p", "s"]
computer_play = random.choice(possible_actions)
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
