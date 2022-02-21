class User:
    '''
    Class that generates new instances of User
    '''

    user_list = []

    def __init__(self, user_name, password):

        self.user_name = user_name
        self.password = password
        '''
            __init__method that helps define properties for our objects.
            Args:
                user_name: user name
                passord : password of the user
            '''

    def save_user(self):
        '''
        save_user method saves the user object into the database/user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes the user
        '''

        User.user_list.remove(self)
