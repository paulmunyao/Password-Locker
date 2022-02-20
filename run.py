import getpass

username = input("Enter user name: ")
password = input("Enter password: ")
confirm_username = input("Enter user name: ")
confirm_password = input("Enter password: ")


if username == confirm_username:
    print("Welcome.")

else:
     print("Username doesn't match")


if password == confirm_password:
        print("Welcome.")

else:
        print("Kindly enter your correct password")
# user = getpass.getpass()
# while True:
#     password = getpass.getpass("")
