import getpass

username = input("Enter user name: ")
lastname = input("Enter last name: ")
password = input("Enter password: ")

user = getpass.getpass()
while True:
    password = getpass.getpass("")