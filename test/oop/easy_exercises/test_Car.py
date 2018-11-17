import unittest

from oop.easy_exercises.car import Car


class TestCar(unittest.TestCase):
    """Tests for the class Car"""

    def setUp(self):
        self.car1 = Car('Seat', 'Ibiza', 2002)

    def test_get_descriptive_name(self):
        expected_output = 'Seat Ibiza 2002'
        self.assertEqual(self.car1.get_descriptive_name(), expected_output)

    def test_set_odometer(self):
        self.assertEqual(self.car1.get_odometer(), 0)
        self.car1.set_odometer(200)
        self.assertEqual(self.car1.get_odometer(), 200)
        self.assertRaises(Exception, self.car1.set_odometer, 100)

    def test_increment_odometer(self):
        self.car1.set_odometer(200)
        self.car1.increment_odometer(10)
        self.assertEqual(self.car1.get_odometer(), 210)

