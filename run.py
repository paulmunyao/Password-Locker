import getpass

username = input("Enter user name: ")
password = input("Enter password: ")
confirm_username = input("Enter user name: ")
confirm_password = input("Enter password: ")

if username == confirm_username:
    print("Welcome.")

else:
     print("Try again")


if password == confirm_password:
        print("Welcome.")

else:
        print("Kindly enter your correct password")
# user = getpass.getpass()
# while True:
#     password = getpass.getpass("")
