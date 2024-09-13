import json
import hashlib
import os

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump({}, file)
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_users(users):
    try:
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)
    except IOError as e:
        print(f"Error saving users: {e}")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def sign_up(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    users[username] = {"password": hash_password(password)}
    save_users(users)
    return True, "Sign-up successful."


def login(username, password):
    users = load_users()
    hashed_password = hash_password(password)
    if username in users and users[username]["password"] == hashed_password:
        return True, "Login successful."
    return False, "Invalid credentials."
