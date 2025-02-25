from usersOperations import *

def app():
        print("-----------------------------------------------")
        print("Welcome to the Fundraising Projects Console App!")
        print("-----------------------------------------------")
        print("Please select an option from the menu below:")
        print("-----------------------------------------------")
        print("-----------------------------------------------")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Enter your choice: ")

        while True:
            if option == "1":
                register()
            elif option == "2":
                login()
            elif option == "3":
                print("-----------------------------------------------")
                print("Thank you for using the Fundraising Projects Console App!")
                print("-----------------------------------------------")
                exit()
            else:
                print("-----------------------------------------------")
                print("Invalid option. Please enter a number from 1 to 3.")
                print("-----------------------------------------------")
                continue
app()

