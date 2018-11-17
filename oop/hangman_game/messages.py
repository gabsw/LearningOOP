def player_name_prompt():
    while True:
        player_name = input('Write your name down before starting the game.\n')
        if player_name == '':
            print('Your name cannot be blank. Try again!\n')
            continue
        else:
            break
    return player_name


def introduction_prompt(player_name):
    print('\nWelcome to the Hangman Game, ' + player_name + '! \n'
          'You will have to figure out a random word to win.\n'
          'You only have 5 tries to do it, after exceeding those, you will lose.\n'
          'Good luck!\n')


def guess_prompt():
    while True:
        player_guess = input('Guess a letter. \n')
        if player_guess.isalpha() and len(player_guess) == 1:
            guess = player_guess
            break
        else:
            print('Your guess is invalid. Try again.\n')
    return guess


def hint_before_answer_prompt(hint_before_guess):
    print('The word has ' + str(hint_before_guess) + ' letters.')


def hint_after_answer_prompt(hint_after_guess):
    print(hint_after_guess)


def win_prompt(player_name):
    print('\nCongratulations, ' + player_name + '!')


def loss_prompt(player_name, answer):
    print('\nGame over, ' + player_name + '! \n'
          'You have exceeded 5 tries and lost the game.\n' 
          'The correct answer is ' + "".join(str(x) for x in answer) + '.')


def attempts_prompt(tries):
    if tries < 4:
        print('\nYou still have ' + str(5 - tries) + ' more attempts left.')
    else:
        print('This will be your last attempt!')