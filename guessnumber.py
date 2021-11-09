import random
#This program lets you guess a number between 1 and 10
def guess(x):
    # this sets the random # to a random integer between 1 and x
    random_number = random.randint(1,x)
    # guess is 0 becuase we need something outside the range to jump into the while loop
    guess = 0

    while guess!=random_number:
        # convert the string input to an integer to compare a number with a number
        guess = int(input(f'Guess a number betwwen 1 and {x}\n'))
        if guess > random_number:
            print("Guess lower")
        elif guess < random_number:
            print("Guess higher")
    print(f'Correct you guessed {random_number}')

# this calls the function of guess and passes 10 as the x parameter
guess(10)
