import unittest

from oop.easy_exercises.counter import Counter


class TestCounter(unittest.TestCase):
    """Tests for class Counter"""

    def setUp(self):
        self.counter1 = Counter(1)

    def test_invalid_number(self):
        """Check if entering a negative number will raise an exception"""
        self.assertRaises(Exception, Counter, -3)

    def test_valid_number(self):
        """Check if entering a valid number will return correctly"""
        self.assertEqual(self.counter1.number, 1)

    def test_current_value(self):
        """Check if current_value returns the expected number"""
        self.assertEqual(self.counter1.current_value(), 1)

    def test_increase_counter(self):
        """Check if increase_counter is doing the correct sum operation"""
        self.counter1.increase_counter(5)
        self.assertEqual(self.counter1.number, 6)
        self.counter1.increase_counter()
        self.assertEqual(self.counter1.number, 7)

    def test_decrease_counter(self):
        """Check if decrease_counter is doing the correct subtraction operation"""
        self.counter1.decrease_counter()
        self.assertEqual(self.counter1.number, 0)
        self.counter1.decrease_counter(5)
        self.assertEqual(self.counter1.number, -5)





