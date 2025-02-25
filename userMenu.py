from ProjectsOperations import *
from usersOperations import login

def user_menu(user_id):
    print("-----------------------------------------------")
    print("Please select an option from the menu below:")
    print("-----------------------------------------------")
    print("-----------------------------------------------")

    print("1. Create a new project")
    print("2. View all projects")
    print("3. View a project")
    print("4. Update a project")
    print("5. Delete a project")
    print("6. Search a project")
    print("7. back")
    print("8. Exit")


    choice = input("Enter your choice: ")

    while True:
        if choice == "1":
            create_project(user_id)
        elif choice == "2":
            view_all_projects(user_id)
        elif choice == "3":
            view_project(user_id)
        elif choice == "4":
            update_project(user_id)
        elif choice == "5":
            delete_project(user_id)
        elif choice == "6":
            search_project(user_id)
        elif choice == "7":
            print("-----------------------------------------------")
            print("Going Back to Main Menu")
            print("-----------------------------------------------")
            from app import app
            app()
        elif choice == "8":
            print("-----------------------------------------------")
            print("Thank you for using the Fundraising Projects Console App!")
            print("-----------------------------------------------")
            exit()
        else:
            print("-----------------------------------------------")
            print("Invalid option. Please enter a number from 1 to 6.")
            print("-----------------------------------------------")
            return

