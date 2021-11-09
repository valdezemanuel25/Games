import random

# this is a function becuase is started as def and has a set of instructions
def play():
    # get user input to start the game
    user = input("Rock = r, Paper = p, Scissors = s\n")
    # set a list and random.choice tells pycharm to get a random letter from the list
    computer = random.choice(['r','p','s'])

    print(f'{user} vs {computer}')
    # the == compares two variables
    if user == computer:
        return 'It\s a tie'
    # this calls the function player_wins() and passes user&computer has parameters
    if player_wins(user,computer):
        return 'You won'
    # this is outside the if staements becuase if neither are true then the player lost
    return 'You lost'

# a function that needs parameters to work
def player_wins(player,oppenent):
    #return true if player wins
    #r>s, s>p, p>r these are the choices for the player to win
    # it will run thru every scenario if one is true then it will return true otherwise returns false
    if(player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p')\
        or (player == 'p' and oppenent == 'r'):
        return True

# if we used functions we need to call them in order for python to execute the steps we coded so we type..
print(play())