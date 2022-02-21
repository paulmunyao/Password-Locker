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
        self.new_user = User("Paul", "123")

    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Paul")
        self.assertEqual(self.new_user.password, "123")

    def test__save_user(self):
        '''
        test to see if the user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        tear down method to run after each test case
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        Test to check if we can save multiple users
        '''
        self.new_user.save_user()
        test_user = User("Test", "user")
        test_user .save_user()
        self.assertEqual(len(User.user_list), 2)

    def test__delete_user(self):
        '''
        test to see if the user is deleted
        '''
        self.new_user.save_user()
        test_user = User("Test","user")
        self.assertEqual(User.user_list.remove(self))


if __name__ == "__main__":
    unittest.main()
