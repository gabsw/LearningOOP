from random import randint


class GameMechanics:
    """Creates a class that models a guessing game. The game consists of 4 hidden
numbers, ranging from 0 to 9, and the player must guess all the numbers in the correct position
in 10 tries. If the player fails to guess the correct digits, you should print how many numbers he
guessed in the correct position and how many numbers he guessed in the wrong position (that is,
the number is part of the answer, but should be at a different position)."""

    def __init__(self):
        """Initializes answer"""
        self.answer = self._generate_answer()
        self.tries = 0

    def _generate_answer(self):
        """Generates 4 random numbers from 0 to 9"""
        self.answer = [randint(0, 9) for _ in range(4)]
        return self.answer

    def get_answer(self):
        """Return answer"""
        return self.answer

    def increase_number_of_tries(self):
        """Create a counter for the number of tries"""
        self.tries += 1

    def get_number_of_tries(self):
        """Return number of tries"""
        return self.tries

    def exceed_number_of_tries(self):
        """Signals when the user reaches the limit of tries"""
        return self.tries == 10

    def test_guess(self, guess):
        """Check if guess from the user is the same as answer"""
        return guess == self.answer

    def compute_hint(self, guess):
        """Return how many correct numbers are in the right place and in the wrong place"""
        counter_right = 0
        counter_in_answer = 0

        for i in range(4):
            if guess[i] == self.answer[i]:
                counter_right += 1
            elif self.answer[i] in guess:
                counter_in_answer += 1

        return counter_right, counter_in_answer
