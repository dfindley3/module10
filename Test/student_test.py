#!/usr/local/bin/python3

import unittest
from student import Student

class TestClass:
    """Test student class"""
    def setUp(self):
        self.student = Student("Jobs", "Steve,", "Computer Programming", 3.9)
    
    def tearDown(self):
        del self.student
    
    def test_object_created_required_attributes(self):
        test = Student("Wozniak", "Steve", "Programming", 4.0)

    def test_object_created_all_attributes(self):
        test = Student("Cook", "Tim", "Finance", 3.75)

    def test_student_str(self):
        print(str(self.student))

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(AttributeError):
            test = Student(123, "Cook")
    
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(AttributeError):
            test = Student("Tim", 123)

    def test_object_not_corrected_error_major(self):
        with self.assertRaises(AttributeError):
            test = Student("Programming", 123)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(AttributeError):
            test = Student(4.0)

if __name__ == "__main__":
    unittest.main()