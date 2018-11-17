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
    print('\nWelcome to the blackjack table, ' + player_name + '! \n'
          'Whoever hits 21 or gets the closest, will win.\n'
          'Good luck!\n')


def initial_pool_prompt():
    while True:
        pool = int(input('How many euros do you bring to the table?\n'))
        if pool == '' or pool <= 0 or not str(pool).isnumeric():
            print('The value is invalid. Try again!\n')
            continue
        else:
            break
    return pool


def bet_prompt(current_pool):
    while True:
        bet = int(input('Place your bet.\n'))
        if bet == '' or not str(bet).isnumeric() or bet <= 0:
            print('The value is invalid. Try again!\n')
            continue
        elif bet > current_pool:
            print('You do not have enough money to bet. Try again with a lower amount!\n')
            continue
        else:
            break
    return bet


def quit_prompt(player_name, pool_after_play):
    while True:
        print(player_name + ', you have ' + str(pool_after_play) + ' euros in the table.')
        decision_quit = input('Do you want to continue this game? (y/n)\n')
        if decision_quit != 'y' and decision_quit != 'n':
            print('Your answer is invalid. Write y or n.\n')
            continue
        else:
            break
    return decision_quit


def end_results_prompt(player_name, player_result):
    print(player_name + ', you have left the table with ' + str(player_result) + ' euros.')


def another_turn_prompt(player_name, current_score):
    while True:
        print(player_name + ', you have a current score of ' + str(current_score) + '.\n')
        decision_turn = input('Do you want another card ? (y/n)\n')
        if decision_turn != 'y' and decision_turn != 'n':
            print('Your answer is invalid. Write y or n.\n')
            continue
        else:
            break
    return decision_turn


def final_turn_score_player_prompt(final_score):
    print('You have a final score for this turn of ' + str(final_score) + '.\n')


def final_turn_score_croupier_prompt(final_score):
    print('The croupier has a final score for this turn of ' + str(final_score) + '.\n')


def win_prompt(player_name, bet):
    print(player_name + ', you have won this turn. You will add ' + str(bet) + ' to your money pool.')


def draw_prompt(player_name):
    print(player_name + ', you have drawn this turn. You will not add anything to your money pool.')


def loss_prompt(player_name, bet):
    print(player_name + ', you have lost this turn. You have lost ' + str(bet) + ' to the casino.')


def show_card_player(card):
    print('You have selected the following card: ' + ' '.join(card) + '. \n')


def show_card_croupier(card):
    print('The croupier has selected the following card: ' + ' '.join(card) + '. \n')


def ace_prompt():
    while True:
        ace_decision = input('How much value does the ace have in this game? 1 or 11?\n')
        if ace_decision != '1' and ace_decision != '11':
            print('Your answer is invalid. Choose either 1 or 11.\n')
            continue
        else:
            break
    return int(ace_decision)


def lost_all_the_money_prompt(player_name):
    print(player_name + ', you lost all your money and will be kicked out of the table.')


def loss_player_bust_prompt(player_name, bet):
    print(player_name + ', you have busted and automatically lost the turn.\n' +
          'You have lost ' + str(bet) + ' euros to the casino.\n')


def win_croupier_bust_prompt(player_name, bet):
    print(player_name + ', the croupier has busted and you automatically won the turn.\n' +
          'You have won ' + str(bet) + ' euros.')


def player_blackjack_prompt(bet):
    print('Congrats, you have hit BLACKJACK!\n' + 'You have won ' + str(bet) + ' euros.\n')


def croupier_blackjack_prompt(bet):
    print('Tough luck, the casino has hit BLACKJACK!\n' + ' You have lost ' + str(bet) + ' euros.\n')