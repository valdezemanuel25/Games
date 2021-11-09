import random

def play():
    user = input("Rock = r, Paper = p, Scissors = s\n")
    computer = random.choice(['r','p','s'])
   # print(f'{user} vs {computer}')
    if user == computer:
        return 'It\s a tie'
    if player_wins(user,computer):
        return 'You won'

    return 'You lost'

def player_wins(player,oppenent):
    #return true if player wins
    #r>s, s>p, p>r
    if(player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p')\
        or (player == 'p' and oppenent == 'r'):
        return True

print(play())