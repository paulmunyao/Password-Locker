class credentials:
    '''
    Class that generates new instances of credentials
    '''

    credentials_list = []

    def __init__(self, user_name, password):

        self.user_name = user_name
        self.password = password
        '''
            __init__method that helps define properties for our objects.
            Args:
                user_name: user name
                passord : password of the user
            '''

    def save_credentials(self):
        '''
        save_credentials method saves the user object into the database/user_list
        '''

        credentials.user_list.append(self)