
def user_menu():
    print("User LoggedIn Successfully!")
    print("-----------------------------------------------")
    print("Please select an option from the menu below:")
    print("-----------------------------------------------")
    print("-----------------------------------------------")

    print("1. Create a new project")
    print("2. View all projects")
    print("3. View a project")
    print("4. Update a project")
    print("5. Delete a project")
    print("5. Search a project")
    print("6. back")
    print("7. Exit")


    option = input("Enter your choice: ")

while True:
    if option == "1":
        create_project()
    elif option == "2":
        view_all_projects()
    elif option == "3":
        view_project()
    elif option == "4":
        update_project()
    elif option == "5":
        delete_project()
    elif option == "6":
        search_project()
    elif option == "7":
        break
    elif option == "8":
        print("Thank you for using the Fundraising Projects Console App!")
        exit()
    else:
        print("Invalid option. Please enter a number from 1 to 6.")
        continue

user_menu()

