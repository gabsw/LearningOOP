from oop.blackjack.mechanics import GameMechanics

from oop.blackjack.messages import *


def play_blackjack():

    # Ask player for their name and store it
    player_name = player_name_prompt()

    # Ask player for amount of money in the pool
    player_pool = initial_pool_prompt()

    # Create two instances for the class GameMechanics
    game_player = GameMechanics(player_pool)
    game_croupier = GameMechanics(0)
    game_croupier.deck = game_player.deck

    # Launch the introductory text of the game
    introduction_prompt(player_name)

    # Select the value of ace
    ace_value = ace_prompt()

    while True:
        game_player.score = 0
        game_croupier.score = 0
        game_player.hand = []
        game_croupier.hand = []

        # Update money in the player pool
        current_pool = game_player.update_money_pool()
        # Player must place bet
        bet = bet_prompt(current_pool)
        game_player.set_bet(bet)

        # Player turn
        bust_player = False
        blackjack_player = False
        current_score_croupier = 0
        while True:
            game_player.deck_low_on_cards(game_croupier)
            card_player = game_player.get_next_card()
            show_card_player(card_player)
            game_player.add_card_to_hand(card_player)
            current_score_player = game_player.count_score(ace_value)
            if current_score_player > 21:
                bust_player = True
                break
            if current_score_player == 21:
                blackjack_player = True
                break
            question_turn = another_turn_prompt(player_name, current_score_player)
            if question_turn == 'y':
                continue
            else:
                final_turn_score_player_prompt(current_score_player)
                break

        if bust_player:
            loss_player_bust_prompt(player_name, bet)
        elif blackjack_player:
            player_blackjack_prompt(bet)
        else:
            # Croupier turn
            bust_croupier = False
            blackjack_croupier = False
            while True:
                game_croupier.deck_low_on_cards(game_player)
                card_croupier = game_croupier.get_next_card()
                show_card_croupier(card_croupier)
                game_croupier.add_card_to_hand(card_croupier)
                game_croupier.get_hand()
                current_score_croupier = game_croupier.count_score(ace_value)
                if current_score_croupier < 17:
                    continue
                elif current_score_croupier > 21:
                    bust_croupier = True
                    break
                elif current_score_croupier == 21:
                    blackjack_croupier = True
                    break
                else:
                    final_turn_score_croupier_prompt(current_score_croupier)
                    break

            if bust_croupier:
                win_croupier_bust_prompt(player_name, bet)
            elif blackjack_croupier:
                croupier_blackjack_prompt(bet)
            else:

                # Test result of the game if there wasn't a bust
                if game_player.win_condition(current_score_player, current_score_croupier):
                    win_prompt(player_name, bet)
                elif game_player.draw_condition(current_score_player, current_score_croupier):
                    draw_prompt(player_name)
                else:
                    loss_prompt(player_name, bet)

        # Bet collection
        game_player.collect_bet(current_score_player, current_score_croupier)
        pool_after_play = game_player.update_money_pool()

        # Game exit by losing all the money
        if pool_after_play == 0:
            lost_all_the_money_prompt(player_name)
            break

        # Question the player if they want to exit the game
        decision = quit_prompt(player_name, pool_after_play)

        # Game exit by decision
        if decision == 'n':
            # Show how much money they have by the end of the game
            end_results_prompt(player_name, pool_after_play)
            break
