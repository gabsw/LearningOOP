import unittest

from oop.easy_exercises.dog import Dog


class TestDog(unittest.TestCase):
    """Tests for the class Dog"""

    def setUp(self):
        self.dog1 = Dog('Billy', 7)

    def test_name_empty(self):
        """Checks if choosing an empty string for a name will cause and exception"""
        self.assertRaises(Exception, Dog, '')  # Dog('')

    def test_name_valid(self):
        """Checks if choosing a valid string for a name will be accepted"""
        dog2 = Dog('Jo', 2)
        self.assertEqual(dog2.name, 'Jo')
        self.assertEqual(self.dog1.name, 'Billy')

    def test_age_invalid(self):
        """Checks if choosing a negative number for age will cause and exception"""
        self.assertRaises(Exception, Dog, -2)

    def test_age_valid(self):
        """Checks if choosing a valid number for age will be accepted"""
        dog2 = Dog('Jo', 2)
        self.assertEqual(dog2.age, 2)
        self.assertEqual(self.dog1.age, 7)

    def test_sit(self):
        """Checks if sit returns the expected sentence"""
        sentence_expected = 'Billy is now sitting.'
        self.assertEqual(self.dog1.sit(), sentence_expected)

    def test_roll_over(self):
        """Checks if roll_over returns the expected sentence"""
        sentence_expected = 'Billy is now rolling over.'
        self.assertEqual(self.dog1.roll_over(), sentence_expected)

