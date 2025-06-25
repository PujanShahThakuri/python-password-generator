Password Generator
A secure, customizable password generator written in Python. This program allows users to create strong passwords by selecting which types of characters to include (lowercase, uppercase, digits, symbols) and specifying the desired password length.

Features
User chooses which character sets to include:

Lowercase letters

Uppercase letters

Digits

Symbols

Ensures the password contains at least one character from each selected category.

Validates user inputs with friendly prompts and error messages.

Guarantees password length is sufficient based on user selections.

Generates randomized passwords with shuffled characters for added security.

How to Use
Clone or download this repository.

Navigate to the project folder:

Open your terminal or command prompt.

Change directory to where the file is located. For example:

bash
Copy
Edit
cd path/to/your/project/folder
Run the script:

bash
Copy
Edit
python password_generator.py
Follow the on-screen prompts:

Choose which character types to include (y or n).

Enter the desired password length (must be at least 4 and not less than the number of selected character types).

The program will then generate and display your secure password.

Example Usage
pgsql
Copy
Edit
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include digits? (y/n): n
Include symbols? (y/n): y
Enter password length (min 4): 8
Generated password: aB#dF$hQ
File Location on GitHub
The main script file is:

Copy
Edit
password_generator.py
You can find it in the root directory of this repository.

Requirements
Python 3.x

No additional libraries required (uses only built-in modules: random and string)

About
This project was developed to demonstrate skills in Python programming, including:

User input validation

Conditional statements

String manipulation

Randomization techniques

Writing reusable functions

It is ideal for beginners learning Python or anyone needing a quick and customizable password generator.

License
This project is licensed under the MIT License.
