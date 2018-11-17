class Student:
    """Create a class that stores an analyzes the report card of a student"""

    def __init__(self, name):
        self.name = name
        if name == '':
            raise Exception('Name cannot be an empty string.')

        self.grades_by_subject = {}

    def add_grade(self, subject, grade):
        if subject == '':
            raise Exception('Subject cannot be an empty string.')
        if grade < 0 or grade > 10:
            raise Exception('Grade must be between 0 and 10.')

        # Check if a key already exists in the dictionary before adding it
        if subject not in self.grades_by_subject:
            # Add new key and respective list of values
            self.grades_by_subject[subject] = [grade]
        else:
            # Add new value to respective key already in the dictionary
            subject_grades = self.grades_by_subject[subject]
            subject_grades.append(grade)
            # ---------list---------------).list method

        # subject_grades = self.grades_by_subject.get(subject, [])
        # subject_grades.append(grade)
        # self.grades_by_subject[subject] = subject_grades

    def get_subject_grades(self, subject):
        if subject not in self.grades_by_subject:
            raise Exception('There must be at least one subject.')
        list_grades = self.grades_by_subject[subject]
        return list_grades

    def get_subject_average(self, subject):
        if subject not in self.grades_by_subject:
            raise Exception('There must be at least one subject.')
        list_grades = self.grades_by_subject[subject]
        subject_average = sum(list_grades) / len(list_grades)
        return subject_average

    def get_grade_summary(self):
        grade_summary = {subject: self.get_subject_average(subject) for subject in self.grades_by_subject}
        return grade_summary
