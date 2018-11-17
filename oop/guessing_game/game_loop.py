from oop.guessing_game.mechanics import GameMechanics

from oop.guessing_game.messages import *


def play_guessing_game():

    # Ask player for their name and store it
    player_name = player_name_prompt()

    # Create an instance for the class GameMechanics
    game = GameMechanics()

    # Launch the introductory text of the game
    introduction_prompt(player_name)

    while True:

        # Apply increment for number of tries
        game.increase_number_of_tries()

        # Store the number of tries
        tries = game.get_number_of_tries()

        # Ask player for their guess and store it
        player_guess = guess_prompt()

        # Check if answer is equal to guess
        # If the test is true, call win message
        if game.test_guess(player_guess):
            win_prompt(player_name, tries)
            break
        # If the test is false, analyze guess and call hint message
        else:
            hint = game.compute_hint(player_guess)
            hint_prompt(hint)
            attempts_prompt(tries)

        # Check if player has exceeded the limit of tries
        # If the test is true, call loss message
        if game.exceed_number_of_tries():
            loss_prompt(player_name, answer)
            break

        # If the test is false, repeat the game process


if __name__ == '__main__':
    print('game loop')
    play_guessing_game()
