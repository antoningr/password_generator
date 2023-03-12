import random
import string
import hashlib
import getpass
import os

def generate_password(length, uppercase, lowercase, numbers, symbols):
    """
    Generates a random password based on user preferences.
    """
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    
    if not chars:
        print("Error: No character types selected!")
        return None
    
    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    return password

def save_password(password, username=None, site=None):
    """
    Saves the generated password to a file.
    """
    with open("passwords.txt", "a") as f:
        if username and site:
            f.write(f"{username} - {site}: {password}\n")
        elif username:
            f.write(f"{username}: {password}\n")
        else:
            f.write(f"{password}\n")
    
    print("Password saved to passwords.txt")

def view_passwords():
    """
    Displays the contents of the password file.
    """
    try:
        with open("passwords.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No passwords saved yet!")

def hash_password(password):
    """
    Hashes the given password using SHA-256.
    """
    salt = os.urandom(32) # Generate a random salt
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key.hex()

def verify_password(password, hashed_password):
    """
    Verifies that the given password matches the given hashed password.
    """
    salt = bytes.fromhex(hashed_password)[:32]
    key_to_check = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key_to_check.hex() == hashed_password

def create_account():
    """
    Creates a new account with a username and password.
    """
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hash_password(password)
    with open("accounts.txt", "a") as f:
        f.write(f"{username}:{hashed_password}\n")
    print("Account created successfully.")

def login():
    """
    Allows the user to log in with a username and password.
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    with open("accounts.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(":")
            if parts[0] == username:
                hashed_password = parts[1]
                if verify_password(password, hashed_password):
                    print("Login successful!")
                    return
                else:
                    print("Incorrect password.")
                    return
        print("Username not found.")

def main():
    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Generate password")
        print("2. Save password")
        print("3. View saved passwords")
        print("4. Create account")
        print("5. Login")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            length = int(input("Enter the desired length of your password: "))
            uppercase = input("Include uppercase letters? (y/n): ")
            lowercase = input("Include lowercase letters? (y/n): ")
            numbers = input("Include numbers? (y/n): ")
            symbols = input("Include symbols? (y/n): ")

            password = generate_password(length, uppercase=="y" or uppercase=="Y", lowercase=="y" or lowercase=="Y", numbers=="y" or numbers=="Y", symbols=="y" or symbols=="Y")
            if password:
                print(f"Your password is: {password}")
        elif choice == "2":
            password = input("Enter the password to save: ")
            username = input("Enter the username associated with this password (press enter if none): ")
            site = input("Enter the website or service associated with this password (press enter if none): ")
            save_password(password, username, site)
        elif choice == "3":
            view_passwords()
        elif choice == "4":
            create_account()
        elif choice == "5":
            login()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
