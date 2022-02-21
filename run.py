from user import User



def create_user(username, password):
    '''
    function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_users(user):
    '''
    function to save the users
    '''


def delete_user(user):
    '''
    Function to delete the user
    '''


def find_user(username):
    '''
    Function to find the user by their name
    '''


def check_existing_user(username):
    '''
    Function to check if the user exists by using their username
    '''


def display_users():
    '''
    Function to display the users
    '''


def main():
    print("Hello welcome.What is your name ?")
    user_name = input()

    print(f"Hello {user_name}. What do you want to do ?")
    print("\n")

    while True:
        print("Use these short codes :cu - create a new user, du - display user, fu - find user, ex - exit user list")
        shortcode = input().lower()

        if shortcode == "cu":
            print("Create a new user")
            print("")

            print("Create your password ")
            p_password = input()

            save_users(create_user(p_password))
            print("\n")