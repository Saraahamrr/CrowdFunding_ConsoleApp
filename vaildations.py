import re
import json
import bcrypt

def isValid_email(email):
    if email.count("@") != 1 or not email.endswith(".com"):
        print("invalid email")
        return False
    else:
        return True
def email_exists(email):
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except:
        return False
    for user in users_list:
        if user["email"] == email:
            return True
    return False

def isValid_phone(phone):

    if re.match(r"^01[0-9]{9}$", phone):      
        return True
    else:
        print("Invalid phone number. Please enter a valid phone number.")
    return False

def isValid_password(password):
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
        return True
    else:
        print("Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, and one number.")
    return False

def check_password(entered_password, stored_hashed_password):
    if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        return True  
    else:
        return False  
    
def isValid_username(username):
    if re.match(r"^[a-zA-Z0-9_]{5,}$", username):
        return True
    else:
        print("Username must contain at least 5 characters.")
    return False
def username_exists(username):
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except:
        return False
    for user in users_list:
        if user["username"] == username:
            return True
    return False
def isValid_project_name(project_name):
    if re.match(r"^[a-zA-Z0-9_]{5,}$", project_name):
        return True
    else:
        print("Project name must contain at least 5 characters.")
    return False
