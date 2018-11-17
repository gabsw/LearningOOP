import json

import random


class GameMechanics:
    """Creates a class that models the hangman game."""

    def __init__(self):
        """Initializes answer"""
        self.answer = self._generate_answer()
        self.tries = 0
        self.guess_template = ['_' for _ in range(len(self.answer))]
        # self.guess_template = ['_'] * len(self.answer)

    def _generate_answer(self):
        """Import a dictionary file and select a word randomly for the answer"""
        file_path = 'C:\\Users\gabri\Documents\Prog\Python\words_dictionary.json'
        with open(file_path) as file_obj:
            words_dictionary = json.load(file_obj)

        answer = list(random.choice([key for key in words_dictionary]))
        return answer

    def decrease_number_of_tries(self, guess):
        """Create a counter for the number of tries"""
        if self.test_guess(guess):
            self.tries = self.tries
        else:
            self.tries += 1

    def get_number_of_tries(self):
        """Return number of tries"""
        return self.tries

    def exceed_number_of_tries(self):
        """Signals when the user reaches the limit of tries"""
        return self.tries == 5

    def test_guess(self, guess):
        """Check if guess from the user is part of the answer answer"""
        if guess in self.answer:
            return True

    def compute_hint_before_guess(self):
        """Return the number of letters of answer"""
        hint_before_guess = len(self.answer)
        return hint_before_guess

    def update_guess_template(self, guess):
        """Create a list where the correct input from the user will be inserted"""
        for i in range(len(self.answer)):
            if self.answer[i] == guess:
                self.guess_template[i] = guess

        return self.guess_template

    def compute_hint_after_guess(self):
        """Return the correct letters in place and show the wrong letters as underscores"""
        return " ".join(str(x) for x in self.guess_template)

    def win_condition(self):
        """Checks if guess_template is equal to answer"""
        if self.guess_template == self.answer:
            return True
