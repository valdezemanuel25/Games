import random
# This program lets the computer guess what number you are thinking between 1 and 10
def computer_guess(x):
    # this is the range of our guessing numbers
    low = 1
    high =x
    feedback = ''

    # while the computer guess is not correct then it will jump into this loop
    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'IS {guess} too high [H], too low [L], or correct [C]\n').lower()
        while feedback != 'h' and feedback !='l' and feedback!='c':
            feedback = input("Please enter H for too High, L for too low or C for correct\n")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1


    print(f"Computer has guessed {guess} ")

# this calls the function of computer guess and passes 10 as the x parameter
computer_guess(10 )
