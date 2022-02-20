import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test that defines test cases for the User class
    Args:
        unitest.Testcase: Testcase that helps in creating test cases for class User.
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user = User("Paul Munyao","123")

    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Paul Munyao")
        self.assertEqual(self.new_user.first_name, "123")

    def test__save_user(self):
        '''
        test to see if the user is saved
        '''


if __name__ == "__main__":
    unittest.main()
