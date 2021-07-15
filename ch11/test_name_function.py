"""First, create a class which inherits from unittest.Testcase"""
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like Paul Huber work?"""
        formatted_name = get_formatted_name('paul', 'huber')
        self.assertEqual(formatted_name, 'Paul Huber')


    def test_first_last_middle_name(self):
        """Do names like Kyle James Huber work?"""
        formatted_name = get_formatted_name('kyle', 'huber', 'james')
        self.assertEqual(formatted_name, 'Kyle James Huber')


if __name__ == '__main__':
    unittest.main()