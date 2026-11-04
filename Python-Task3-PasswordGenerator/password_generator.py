# Random Password Generator (Beginner Tier)
# Oasis Infobyte - Python Programming Internship

import random
import string

MIN_LENGTH = 8


def get_length():
    """Asks for password length until a valid number (minimum 8) is entered."""
    while True:
        try:
            length = int(input(f"Enter password length (minimum {MIN_LENGTH}): "))
            if length < MIN_LENGTH:
                print(f"Error: Length must be at least {MIN_LENGTH}.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a whole number (example: 12).")


def ask_yes_no(question):
    """Asks a yes/no question and returns True or False."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please type yes or no.")


def get_character_types():
    """Lets the user choose character types. At least 2 types are required."""
    while True:
        print("\nChoose which character types to include (select at least 2):")
        pools = []

        if ask_yes_no("Uppercase letters (A-Z)?"):
            pools.append(string.ascii_uppercase)
        if ask_yes_no("Lowercase letters (a-z)?"):
            pools.append(string.ascii_lowercase)
        if ask_yes_no("Numbers (0-9)?"):
            pools.append(string.digits)
        if ask_yes_no("Symbols (!@#$...)?"):
            pools.append(string.punctuation)

        if len(pools) >= 2:
            return pools
        print("Error: Please select at least 2 character types. Try again.")


def generate_password(length, pools):
    """Builds a random password that has at least one character from each chosen type."""
    # Step 1: take one character from every chosen type
    password = [random.choice(pool) for pool in pools]

    # Step 2: fill the remaining length with random characters from all chosen types
    all_characters = "".join(pools)
    password += random.choices(all_characters, k=length - len(password))

    # Step 3: shuffle so the first characters are not predictable
    random.shuffle(password)
    return "".join(password)


def main():
    print("=== Random Password Generator ===")

    length = get_length()
    pools = get_character_types()

    while True:
        password = generate_password(length, pools)
        print(f"\nYour password: {password}\n")

        if not ask_yes_no("Generate another password?"):
            print("Thank you! Keep your passwords safe.")
            break


if __name__ == "__main__":
    main()