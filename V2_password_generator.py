import random
import string

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

def main():
    while True:
        print("\n--- PASSWORD GENERATOR ---")
        print("1. Generate password")
        print("2. Save password")
        print("3. View saved passwords")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            length = int(input("Enter the desired length of your password: "))
            uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
            lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
            numbers = input("Include numbers? (y/n): ").lower() == "y"
            symbols = input("Include symbols? (y/n): ").lower() == "y"
            
            password = generate_password(length, uppercase, lowercase, numbers, symbols)
            if password:
                print("Your password is:", password)
        elif choice == "2":
            password = input("Enter the password you want to save: ")
            username = input("Enter the username (optional): ")
            site = input("Enter the site name (optional): ")
            save_password(password, username, site)
        elif choice == "3":
            view_passwords()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
