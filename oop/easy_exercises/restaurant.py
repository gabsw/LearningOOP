class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        if self.restaurant_name == '' or self.cuisine_type == '':
            raise Exception('You cannot enter an empty string')
        # Setting a default value for a new attribute
        self.costumers_served = 0

    def describe_restaurant(self):
        """Returns a description of the restaurant using the attributes"""
        return self.restaurant_name + ' specializes in ' + self.cuisine_type + ' cuisine.'

    def set_costumers_served(self, costumers_served=0):
        """Sets the number of costumers that have been served"""
        self.costumers_served = costumers_served
        if costumers_served < 0:
            raise Exception('Costumers_served cannot be a negative number')

    def get_costumers_served(self):
        """Returns costumers_served"""
        return self.costumers_served

    def increase_costumers_served(self, amount):
        """Increases the costumers_served"""
        if amount > 0:
            self.costumers_served += amount

    def reset_costumers_served(self):
        """Resets the costumers_served"""
        self.costumers_served = 0

# a = Restaurant('a', 'b')
# a.costumers_served = -1

# class Foo:
#     def __init__(self):
#         self._x = 0
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, x):
#         if x < 0:
#             print('x cant be negative')
#         else:
#             self._x = x
