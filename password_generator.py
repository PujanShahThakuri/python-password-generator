import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password_chars = []

    if use_lower:
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))

    if length < len(password_chars):
        return f"Error: Password length too short for selected character types. Minimum required: {len(password_chars)}"

    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    random.shuffle(password_chars)

    return ''.join(password_chars)


# Step 1: Ask which character types to include
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

min_length = sum([use_lower, use_upper, use_digits, use_symbols])

if min_length == 0:
    print("Error: You must select at least one character type.")
else:
    # Step 2: Ask for length with the correct minimum
    while True:
        try:
            length = int(input(f"Enter password length (min {max(4, min_length)}): "))
            if length < max(4, min_length):
                print(f"Password length should be at least {max(4, min_length)}. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for length.")

    # Step 3: Generate and print password
    result = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print("Generated password:", result)
