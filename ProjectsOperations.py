#create_project, view_all_projects, view_project, update_project, delete_project, search_project
from vaildations import *
import json
from datetime import datetime

def create_project(user_id):
    print("Create a new project")
    print("--------------------")
    print("Please submit your project details below:")
    print("------------------------------------------")
    project_name = input("Enter project name: ")
    while project_name_exists(project_name):
        project_name = input("Enter project name: ")
    while not isValid_project_name(project_name):
        project_name = input("Enter project name: ")

    project_description = input("Enter project description: ")
    while not isValid_project_description(project_description):
        project_description = input("Enter project description: ")

    project_target = input("Enter project goal: ")
    while not isValid_target(project_target):
        project_target = input("Enter project goal: ")
    project_target = int(project_target)

    project_start_date = input("Enter project start date: ")
    project_end_date = input("Enter project end date: ")
    while not isvalid_project_dates(project_start_date, project_end_date):
        project_start_date = input("Enter project start date: ")
        project_end_date = input("Enter project end date: ")


    project = {
        "project_name": project_name,
        "project_description": project_description,
        "project_target": project_target,
        "project_start_date": project_start_date,
        "project_end_date": project_end_date,
        "user_id": user_id
    }

    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []

    project["project_id"] = len(projects_list) + 1
    projects_list.append(project)
    with open("projects.json", "w") as file:
        json.dump(projects_list, file)

    print("-----------------------------------------------")
    print("Project created successfully.")
    print("-----------------------------------------------")

    from userMenu import user_menu
    user_menu(user_id)

def view_my_projects(user_id):
        try:
            with open("projects.json", "r") as file:
                projects_list = json.load(file)
        except:
            projects_list = []

        user_projects = [project for project in projects_list if project["user_id"] == user_id]
        if user_projects == []:
                print("No projects found!")
                print("--------------------------------")
                print("Going back to your Menu")
                print("--------------------------------")
                from userMenu import user_menu
                user_menu(user_id)

        else :
            for project in user_projects:
                print("\nExisting Projects:\n")
                print("-----------------------------------------------------------------------------------")
                print(f"-----------------------Project ID: {project['project_id']}------------------------")
                print(f"Project Name: {project['project_name']}")
                print(f"Project Description: {project['project_description']}")
                print(f"Project Target: {project['project_target']}")
                print(f"Project Start Date: {project['project_start_date']}")
                print(f"Project End Date: {project['project_end_date']}")
                print("-----------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------")
            print("would you like to go back to menu now?")
            login_option = input("YES/NO...: " )
            if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
                print("--------------------------------")
                print("Going back to your Menu")
                print("--------------------------------")
                from userMenu import user_menu
                user_menu(user_id)
            else:
                pass

def view_all_projects(user_id):
    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []

    for project in projects_list:
        print("\nExisting Projects:\n")
        print("-----------------------------------------------------------------------------------")
        print(f"-----------------------Project ID: {project['project_id']}------------------------")
        print(f"Project Name: {project['project_name']}")
        print(f"Project Description: {project['project_description']}")
        print(f"Project Target: {project['project_target']}")
        print(f"Project Start Date: {project['project_start_date']}")
        print(f"Project End Date: {project['project_end_date']}")
        print("-----------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------")
    print("would you like to go back to menu now?")
    login_option = input("YES/NO...: " )
    if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
        print("--------------------------------")
        print("Going back to your Menu")
        print("--------------------------------")
        from userMenu import user_menu
        user_menu(user_id)
    else:
        pass    

def view_project(user_id):
    project_name = input("Enter project name: ")
    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []
    
    project = next((project for project in projects_list if project["project_name"] == project_name and project["user_id"] == user_id), None)
    if project :
            print("\n Your Project\n")
            print("-----------------------------------------------------------------------------------")
            print(f"-----------------------Project ID: {project['project_id']}------------------------")
            print(f"Project Name: {project['project_name']}")
            print(f"Project Description: {project['project_description']}")
            print(f"Project Target: {project['project_target']}")
            print(f"Project Start Date: {project['project_start_date']}")
            print(f"Project End Date: {project['project_end_date']}")
            print("-----------------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------------")
            print("would you like to go back to menu now?")
            login_option = input("YES/NO...: " )
            if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
                print("--------------------------------")
                print("Going back to your Menu")
                print("--------------------------------")
                from userMenu import user_menu
                user_menu(user_id)
            else:
                pass
    else:
        print("Project not found!")
        return

def update_project(user_id):
    project_name = input("Enter project name: ")
    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []

    project = next((project for project in projects_list if project["project_name"] == project_name and project["user_id"] == user_id), None)
    if project :
        print("Update Project")
        print("--------------")
        print("---------------------------------------------------")
        print("1. Update project name")
        print("2. Update project description")
        print("3. Update project target")
        print("4. Update project start date")
        print("5. Update project end date")
        print("---------------------------------------------------")
        option = input("Enter your choice: ")
        print("---------------------------------------------------")
        if option == "1":
                new_name = input("Enter new project name: ")
                while project_name_exists(new_name): 
                    new_name = input("Project name already exists. Please enter a different name: ")
                while not isValid_project_name(new_name):  
                    new_name = input("Invalid project name. Please enter a valid name: ")
                project["project_name"] = new_name
                print(f"Project name updated to: {new_name}")
            
        elif option == "2":
                new_description = input("Enter new project description: ")
                while not isValid_project_description(new_description):  
                    new_description = input("Invalid project description. Please enter a valid description: ")
                project["project_description"] = new_description
                print(f"Project description updated to: {new_description}")
            
        elif option == "3":
                new_target = input("Enter new project target: ")
                while not isValid_target(new_target):  # Validate project target
                    new_target = input("Invalid project target. Please enter a valid target: ")
                project["project_target"] = int(new_target)
                print(f"Project target updated to: {new_target}")
            
        elif option == "4":
                new_start_date = input("Enter new project start date (YYYY-MM-DD): ")
                while not isvalid_project_dates(new_start_date, project["project_end_date"]):  # Validate start date
                    new_start_date = input("Invalid start date. Please enter a valid start date: ")
                project["project_start_date"] = new_start_date
                print(f"Project start date updated to: {new_start_date}")
            
        elif option == "5":
                new_end_date = input("Enter new project end date (YYYY-MM-DD): ")
                while not isvalid_project_dates(project["project_start_date"], new_end_date):  # Validate end date
                    new_end_date = input("Invalid end date. Please enter a valid end date: ")
                project["project_end_date"] = new_end_date
                print(f"Project end date updated to: {new_end_date}")
            
        else:
                print("Invalid option. No updates were made.")
                return
            
        with open("projects.json", "w") as file:
                json.dump(projects_list, file)

        print("-----------------------------------------------")
        print("Project updated successfully.")
        print("-----------------------------------------------")
        print("would you like to go back to menu now?")
        login_option = input("YES/NO...: " )
        if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
            print("--------------------------------")
            print("Going back to your Menu")
            print("--------------------------------")
            from userMenu import user_menu
            user_menu(user_id)
        else:
            pass
    else:
        print("Project not found!")
        return
    
def delete_project(user_id):
    project_name = input("Enter project name: ")
    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []

    project = next((project for project in projects_list if project["project_name"] == project_name and project["user_id"] == user_id), None)
    if project :
        projects_list.remove(project)
        with open("projects.json", "w") as file:
            json.dump(projects_list, file)

        print("-----------------------------------------------")
        print("Project deleted successfully.")
        print("-----------------------------------------------")
        print("would you like to go back to menu now?")
        login_option = input("YES/NO...: " )
        if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
            print("--------------------------------")
            print("Going back to your Menu")
            print("--------------------------------")
            from userMenu import user_menu
            user_menu(user_id)
        else:
            pass
    else:
        print("Project not found!")
        return
    

def search_project(user_id):
    project_date= input("Enter project date: ")#stting
    while not isValid_date(project_date):
        project_date = input("Enter project date: ")

    try:
        with open("projects.json", "r") as file:
            projects_list = json.load(file)
    except:
        projects_list = []
    search_res = [
        project for project in projects_list
        if project["user_id"] == user_id
        and datetime.strptime(project["project_start_date"],"%d/%m/%Y" ) <= datetime.strptime(project["project_end_date"],"%d/%m/%Y" )
    ]
    
    if search_res == []:
            print("No projects found!")
            return
    else :
        for project in search_res:
                print("-----------------------------------------------------------------------------------")
                print(f"-----------------------Project ID: {project['project_id']}------------------------")
                print(f"Project Name: {project['project_name']}")
                print(f"Project Description: {project['project_description']}")
                print(f"Project Target: {project['project_target']}")
                print(f"Project Start Date: {project['project_start_date']}")
                print(f"Project End Date: {project['project_end_date']}")
                print("-----------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------")
        print("would you like to go back to menu now?")
        login_option = input("YES/NO...: " )
        if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
                print("--------------------------------")
                print("Going back to your Menu")
                print("--------------------------------")
                from userMenu import user_menu
                user_menu(user_id)
        else:
            pass