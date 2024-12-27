import random
import string

def generate_password(length=12):
    if length < 4:  # Minimum length to include all character types
        raise ValueError("Password length must be at least 4 characters.")
    
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensuring the password includes at least one of each type
    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Input for password length
try:
    user_input = input("Enter the desired password length (minimum 4): ")
    length = int(user_input)
    print("Generated Password:", generate_password(length))
except ValueError:
    if not user_input.isdigit():
        print("Error: Please enter a valid number.")
    else:
        print("Error: Password length must be at least 4.")
