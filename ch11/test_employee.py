import unittest
from employee import Employee


class TestEmployeeRaise(unittest.TestCase):
    """
    Test cases for default raise and user-specified value
    """

    def setUp(self):
        """Create an employee instance for use in ALL test cases"""
        first_name = "Kyle"
        last_name = "Huber"
        default_starting_sal = 30_000
        self.my_employee = Employee(
            first_name, last_name, default_starting_sal
        )
        self.default_increment = ""
        self.custom_increment = ""

    def test_give_default(self):
        """Variable names might get confusing..I did my best. But essentially,
        the way I had the functions set up, I needed to init default_increment as an empty string and
        then down here I assign it to the function call with NO parameters passed to that it increments by
        5,000 and asserts equal"""
        self.default_increment = self.my_employee.give_raise()
        self.assertEqual(self.default_increment, 35_000)

    def test_give_custom_raise(self):
        """Essentially the same concept here, except I'm simulating a custom value from user input,
        and reassigning the empty string for 'self.custom_increment' to a value of my choosing"""
        self.custom_increment = self.my_employee.give_raise(70_000)
        self.assertEqual(self.custom_increment, 100_000)


if __name__ == "__main__":
    unittest.main()
