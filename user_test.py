import unittest
from user import User


class UserTest(unittest.TestCase):
    '''
    Test that defines test cases for the User class
    Args:
        unitest.Testcase: Testcase that helps in creating test cases for class User.
    '''


def setUp(self):
    '''
    Set up method to run before each test case
    '''
    self.new_user = User("Paul", "Munyao", "!@123")


def test__init(self):
    '''
    test__init__ test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name, "Paul")
    self.assertEqual(self.new_user.last_name, "Munyao")
    self.assertEqual(self.new_user.first_name, "!@123")
