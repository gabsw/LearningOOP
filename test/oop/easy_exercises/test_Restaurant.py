import unittest

from oop.easy_exercises.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    """Tests for the class Restaurant"""

    def setUp(self):
        self.rest1 = Restaurant('Wang Yu', 'Chinese')

    def test_invalid_init(self):
        """Checks if choosing an empty string will cause and exception"""
        self.assertRaises(Exception, Restaurant, '', 'Chinese')
        self.assertRaises(Exception, Restaurant, '', '')
        self.assertRaises(Exception, Restaurant, 'Wang Yu', '')

    def test_restaurant_name_valid(self):
        """Checks if choosing a valid string for restaurant_name will be accepted"""
        self.assertEqual(self.rest1.restaurant_name, 'Wang Yu')

    def test_cuisine_type_valid(self):
        """Checks if choosing a valid string for cuisine_type will be accepted"""
        self.assertEqual(self.rest1.cuisine_type, 'Chinese')

    def test_describe_restaurant(self):
        """Checks if describe_restaurant returns the expected sentence"""
        expected_sentence = 'Wang Yu specializes in Chinese cuisine.'
        self.assertEqual(self.rest1.describe_restaurant(), expected_sentence)

    def test_set_costumers_served_invalid(self):
        """Checks if using a negative input will cause an exception"""
        self.assertRaises(Exception, self.rest1.set_costumers_served, -2)

    def test_set_costumers_served_valid(self):
        """Check if using a positive input will return the numbers of costumers served correctly"""
        self.rest1.set_costumers_served(10)
        self.assertEqual(self.rest1.get_costumers_served(), 10)

    def test_increase_costumers_served(self):
        """Checks if the counter is working correctly"""
        self.rest1.set_costumers_served()
        self.rest1.increase_costumers_served(25)
        self.assertEqual(self.rest1.get_costumers_served(), 25)

    def test_reset_costumers_served(self):
        """Checks if 0 costumers are returned after the reset"""
        self.rest1.set_costumers_served(30)
        self.rest1.reset_costumers_served()
        self.assertEqual(self.rest1.get_costumers_served(), 0)
