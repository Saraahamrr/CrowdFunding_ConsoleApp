#create_project, view_all_projects, view_project, update_project, delete_project, search_project
from vaildations import *
import json
from datetime import datetime

def create_project():
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
    user_menu()

def view_all_projects():
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
        user_menu()
    else:
        pass
  



