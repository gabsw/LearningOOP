class Dog:
    """Creates a class that represents a dog and its behavior"""

    def __init__(self, name, age):
        """Initializes attributes name and age"""
        self.name = name
        if name == '':
            raise Exception('Dog needs a name.')

        self.age = age
        if age < 0:
            raise Exception('Age cannot be below 0.')

    def sit(self):
        """Simulate a dog sitting"""
        return self.name + ' is now sitting.'

    def roll_over(self):
        """Simulate a dog rolling over"""
        return self.name + ' is now rolling over.'
