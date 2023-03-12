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

def main():
    length = int(input("Enter the desired length of your password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"
    
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    if password:
        print("Your password is:", password)

if __name__ == "__main__":
    main()
