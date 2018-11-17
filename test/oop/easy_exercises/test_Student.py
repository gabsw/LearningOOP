import unittest

from oop.easy_exercises.student import Student


class TestStudent(unittest.TestCase):
    """Tests for class Student"""

    def setUp(self):
        self.john = Student('John')

    def test_name_invalid(self):
        self.assertRaises(Exception, Student, '')

    def test_name_valid(self):
        self.assertEqual(self.john.name, 'John')

    def test_add_grade_invalid(self):
        self.assertRaises(Exception, self.john.add_grade, '', 3)
        self.assertRaises(Exception, self.john.add_grade, 'Math', 13)
        self.assertRaises(Exception, self.john.add_grade, '', 13)

    def test_add_grade_valid(self):
        self.john.add_grade('Math', 8)
        self.john.add_grade('Math', 4)
        self.assertEqual(self.john.get_subject_grades('Math'), [8, 4])

    def test_get_subject_average(self):
        self.john.add_grade('Chemistry', 4)
        self.john.add_grade('Chemistry', 5)
        self.john.add_grade('Chemistry', 6)
        self.assertEqual(self.john.get_subject_average('Chemistry'), 5)

    def test_get_grade_summary(self):
        self.john.add_grade('Math', 8)
        self.john.add_grade('Math', 4)
        self.john.add_grade('Chemistry', 4)
        self.john.add_grade('Chemistry', 5)
        self.john.add_grade('Chemistry', 6)
        self.assertEqual(self.john.get_grade_summary(), {'Math': 6, 'Chemistry': 5})






