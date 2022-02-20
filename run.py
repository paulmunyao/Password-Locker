import getpass

username = input("Enter user name: ")
password = input("Enter password: ")

user = getpass.getpass()
while True:
    password = getpass.getpass("")