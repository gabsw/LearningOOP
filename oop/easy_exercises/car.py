class Car:
    """Create a class that models a car"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        description = self.brand + ' ' + self.model + ' ' + str(self.year)
        return description

    def get_odometer(self):
        return self.odometer

    def set_odometer(self, mileage):
        if self.odometer < mileage:
            self.odometer = mileage
        else:
            raise Exception('You cannot turn back an odometer.')

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer += miles
