# SecurePasswordGenerator 

## Introduction
The three projects present different password generators, each with an increasing level of complexity and functionality.

### Password generator (V1)
The first project contains a "generate_password" function that takes into account the length and types of characters that the user wants to include in the password. The character types can be upper and lower case letters, numbers and punctuation symbols. The program then creates a random password based on the user's preferences.

To use the program, simply run it and follow the prompts to enter your password preferences. The program will generate a random password based on your preferences and print it to the console. stringNote that this program uses Python randomp modules and integrations to generate passwords.

### Password Generator (V2)
The second project is an extension of the first and adds features to save the generated passwords to a file and to display all saved passwords. The program also provides a menu for the user to choose between generating passwords, saving passwords, displaying saved passwords and exiting the program.

This program adds the following features:
- The ability to save generated passwords to a file, along with optional username and site information.
- The ability to display the saved passwords from the file.
- A menu interface that allows the user to choose from several options.

To use the program, simply launch it and follow the menu instructions. Note that this program also saves passwords in a file called "passwords.txt" in the same directory as the program. If the file does not exist, it will be created automatically.

### Password Generator (V3)
The third project is also an extension of the second one and adds extra security by hashing the passwords before saving them to the file. The program uses the hashlib library to hash the passwords and the getpass function to ask the user for a master password before allowing access to the main menu. The program also clears the console history after the user enters the master password to prevent anyone from seeing the password entered.

This program adds the following features:
- The ability to create an account with a username and hashed password stored in a file.
- The ability to log in to an existing account with a username and hashed password verified against those stored in the account file.
- Generated passwords can now be saved with a username and an associated site, stored in a file.
- Saved passwords can be displayed to the user.
- Passwords are now hashed with SHA-256 for added security.

To use the program, simply launch it and follow the instructions in the menu. Note that this program allows you to generate random passwords, save them to a file, view the saved passwords, create a user account with username and password and log in to an existing account. In addition, this program uses the SHA-256 hash function to store passwords securely.


## Project information
- Project contributor: Antonin
- Date of last update: March 12, 2023

## Project on Git
The project is available on the site [Github](https://github.com/) on the link : [https://github.com/antoningr/password_generator](https://github.com/antoningr/password_generator). 


## Downloading the project
- Open your terminal or command prompt.
- Go to the directory where you want to save the project.
- Type the following command to clone the project from the Git repository:
```
git clone https://github.com/antoningr/password_generator.git
```
- Press "Enter" to run the command. Git will then download the project to the current directory.


