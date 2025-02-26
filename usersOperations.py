from vaildations import *
import json
import bcrypt
import getpass

def register():
    print("Register")
    print("--------")
    print("Please submit your deatils below:")
    print("--------------------------------")
    username = input("Username: ")
    while username_exists(username):
        print("Username already exists. Please enter a different username.")
        username = input("Username: ")
    while not isValid_username(username):
        username = input("Username: ")

    password = getpass.getpass("Password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    while not isValid_password(password):
        password = getpass.getpass("Password: ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    email = input("Email: ")
    while email_exists(email):
        print("Email already exists. Please enter a different email.")
        email = input("Email: ")
    while not isValid_email(email):
        email = input("Email: ")

    phone = input("Phone: ")
    while not isValid_phone(phone):
        phone = input("Phone: ")
    print("--------------------------------")
    
    user = {
        
        "username": username,
        "password": hashed_password.decode('utf-8'),
        "email": email,
        "phone": phone
    }
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except:
        users_list = []
    
    user["user_id"] =  len(users_list) + 1,
    users_list.append(user)

    with open("users.json", "w") as file:
        json.dump(users_list, file)

    print("Done Submitting Details")
    print("--------------------------------")
    print("--------------------------------")
    print("Thank you for registering!")
    print("--------------------------------")
    print("--------------------------------")
    print("would you like to login now?")
    login_option = input("YES/NO...: " )
    if login_option == "YES" or login_option == "yes" or login_option == "y" or login_option == "Y":
        login()
    else:
        print("--------------------------------")
        print("Going back to Main Menu")
        print("--------------------------------")
    from app import app
    app()

def login():
    while True:
        print("--------------------------------")
        print("Login ")
        print("--------------------------------")
        print("Please enter your details below:")
        username = input("Enter username: ")
        password = getpass.getpass("Password: ")

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except:
            print("No users found!")
            return 

        for user in users:
            if user["username"] != username :
                continue  
            if check_password(password, user["password"]) :
                print("--------------------------------")
                print(f"Welcome, {user['username']} !")  
                user_id = user["user_id"]
                from userMenu import user_menu
                user_menu(user_id) 
                return user_id
            else :
                print("Incorrect password!")
                
        print("User not found!")
        
    