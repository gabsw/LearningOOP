def player_name_prompt():
    while True:
        player_name = input('Write your name down before starting the game.\n')
        if player_name == '':
            # raise Exception('Your name cannot be blank. Try again!')
            print('Your name cannot be blank. Try again!\n')
            continue
        else:
            break
    return player_name


def introduction_prompt(player_name):
    print('\nWelcome to the Guessing Game, ' + player_name + '! \n'
          'You will have to figure out a sequence of 4 random numbers to win.\n'
          'You only have 10 tries to do it, after exceeding those, you will lose.\n'
          'Good luck!\n')


def guess_prompt():
    while True:
        player_guess = input('Guess 4 numbers. \nWrite them down without whitespace space.\n')
        if player_guess.isnumeric() and len(player_guess) == 4:
            guess = [int(i) for i in list(player_guess)]
            break
        else:
            print('Your guess is invalid. Try again.\n')
    return guess


def hint_prompt(hint):
    print('You have found ' + str(hint[0]) + ' correct numbers in the right position. \n' 
          'You have found ' + str(hint[1]) + ' correct numbers in the wrong position. \n' 
          'Try again.\n')


def win_prompt(player_name, tries):
    print('\nCongratulations, ' + player_name + '! \n' 
          'You have won the game in ' + str(tries) + ' tries.')


def loss_prompt(player_name, answer):
    print('\nGame over, ' + player_name + '! \n'
          'You have exceeded 10 tries and lost the game.\n' 
          'The correct answer is ' + "".join(str(x) for x in answer) + '.')


def attempts_prompt(tries):
    if tries < 9:
        print('\nYou still have ' + str(10 - tries) + ' more attempts left.')
    else:
        print('This will be your last attempt!')
