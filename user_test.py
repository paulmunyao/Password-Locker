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
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        '''
        Test to see if we can find user in the database
        '''

        self.new_user.save_user()
        test_user = User("Test", "123")
        test_user.save_user()

        found_user = User.find_username("Paul")

        self.assertEqual(found_user, test_user)

    @classmethod
    def find_username(cls,username):
        '''
        Method that takes in a username and returns a name that matches that username. 
        Args:
            username: the username
        Returns:
                Username of that person
        '''

        for user in cls.user_list:
            if user.username == username:
                return user

    def test_user_exists(self):
            '''
            Test to see if we can return a Boolean
            '''
            self.new_user.save_user()
            test_user = User("Test", "123")
            test_user.save_user()

            user_exists = User.user_exists("Paul")

            self.assertTrue(user_exists)

    @classmethod
    def user_exists(cls,username):
        '''
        Method that checks if a username exists in the user list
        Args:
            username: The name of the user to search if it exists
        Returns:
               Boolean: True or flase depending if the contact exists 
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    def test_display_all_users(self):
        '''
        Method that displays a list of all users saved
        '''  
        self.assertEqual(User.display_all_users(),User.user_list)

    @classmethod      
    def display_all_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list

    












if __name__ == "__main__":
    unittest.main()
