from oop.hangman_game.mechanics import GameMechanics

from oop.hangman_game.messages import *


def play_hangman_game():

    # Ask player for their name and store it
    player_name = player_name_prompt()

    # Create an instance for the class GameMechanics
    game = GameMechanics()

    # Launch the introductory text of the game
    introduction_prompt(player_name)

    # Generate hint of number of letters
    hint_before_guess = game.compute_hint_before_guess()
    hint_before_answer_prompt(hint_before_guess)

    while True:

        # Ask player for their guess and store it
        player_guess = guess_prompt()

        # Create guess_template, where the correct guesses are stored to form a word
        game.update_guess_template(player_guess)

        # Check if answer is equal to guess_template
        # If the test is true, call win message
        if game.win_condition():
            win_prompt(player_name)
            break

        # If the test is false, analyze guess and call hint message
        else:
            hint_after_guess = game.compute_hint_after_guess()
            hint_after_answer_prompt(hint_after_guess)

            # Apply increment for number of tries
            game.decrease_number_of_tries(player_guess)

            # Store the number of tries
            tries = game.get_number_of_tries()

            # Display the number of tries left
            attempts_prompt(tries)

        # Check if player has exceeded the limit of tries
        # If the test is true, call loss message
        if game.exceed_number_of_tries():
            loss_prompt(player_name, game.answer)
            break

        # If the test is false, repeat the game process
