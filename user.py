class User:
    '''
    Class that generates new instances of User
    '''

user_list = []

def __init__(self, first_name, last_name, password):
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    '''
     __init__method that helps define properties for our objects.
     Args:
         first_name: first name of the user
         last_name : last name of the user
         passord : password of the user
    '''

def save_user(self):
        '''
        save_user method saves the user object into the database/user_list
        '''

        User.user_list.append(self)

    
