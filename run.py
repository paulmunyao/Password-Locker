import getpass

username = input("Enter user name: ")
password = input("Enter password: ")
confirm_username = input("Enter user name: ")
confirm_password = input("Enter password: ")

if username == confirm_username:
    print("Kindly enter your  correct username.")

else:
    print("Try again")
# user = getpass.getpass()
# while True:
#     password = getpass.getpass("")
