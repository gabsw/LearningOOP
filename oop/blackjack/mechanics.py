import itertools

import random


class GameMechanics:
    """Creates a class that models the blackjack game."""

    def __init__(self, money_pool):
        self.money_pool = money_pool
        self.deck = self._generate_deck()
        self.hand = []
        self.score = 0
        self.bet = 0

    def _generate_deck(self):
        """The game is typically played with 4 52-card decks"""
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']*4
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']*4

        deck = list(itertools.product(values, suits))
        random.shuffle(deck)
        return deck

    def get_next_card(self):
        """One card will be chosen randomly from the deck"""
        card = self.deck.pop()
        return card

    def deck_low_on_cards(self, other_player):
        """Check if deck has few cards and generate a new one automatically to keep the game going"""
        if len(self.deck) <= 60:  # The value ranges between 60 to 75 to block card-counting
            self.deck = self._generate_deck()
            other_player.deck = self.deck

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def get_hand(self):
        """List with all the cards chosen throughout the play"""
        return self.hand

    def count_score(self, ace=11):
        """Count the values of the cards in the hand"""
        face_cards = {'jack', 'queen', 'king'}

        card = self.hand[-1]
        if card[0] == 'ace':
            self.score += ace
        elif card[0] in face_cards:
            self.score += 10
        else:
            self.score += int(card[0])

        return self.score

    def win_condition(self, player_score, croupier_score):
        return player_score > croupier_score

    def loss_condition(self, player_score, croupier_score):
        return player_score < croupier_score

    def draw_condition(self, player_score, croupier_score):
        return player_score == croupier_score

    def set_bet(self, bet_amount):
        self.bet = bet_amount

    def player_ran_out_of_money(self):
        if self.money_pool == 0:
            raise Exception('You have lost all your money, you will be kicked out of the table.')

    def collect_bet(self, player_score, croupier_score):
        if croupier_score > 21 or player_score == 21:
            self.money_pool += self.bet
            return

        if player_score > 21 or croupier_score == 21:
            self.money_pool -= self.bet
            return

        if self.win_condition(player_score, croupier_score):
            self.money_pool += self.bet
        elif self.loss_condition(player_score, croupier_score):
            self.money_pool -= self.bet

    def update_money_pool(self):
        return self.money_pool












