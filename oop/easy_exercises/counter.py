class Counter:
    """Create a class that simulates a simple counter"""

    def __init__(self, number=0):
        self.number = number
        if number < 0:
            raise Exception('You cannot enter a negative number')

    def current_value(self):
        return self.number

    def increase_counter(self, amount=1):
        if amount <= 0:
            pass
        else:
            self.number += amount

    def decrease_counter(self, amount=1):
        if amount <= 0:
            pass
        else:
            self.number -= amount



