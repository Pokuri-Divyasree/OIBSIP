# Random Password Generator (Python)

A simple command-line tool that generates strong random passwords.
Created as part of the Oasis Infobyte Python Programming Internship (Task 3, Beginner Tier).

## Features
- User chooses the password length (minimum 8 characters)
- User chooses character types: uppercase, lowercase, numbers, symbols (at least 2 required)
- Password always contains at least one character from each chosen type
- Input validation: rejects text, short lengths and fewer than 2 character types
- Option to generate another password without restarting the program

## How to Run
1. Install Python 3
2. Open a terminal in this folder
3. Run: `python password_generator.py`
4. Follow the questions on the screen

## Example Output
```
=== Random Password Generator ===
Enter password length (minimum 8): 12

Choose which character types to include (select at least 2):
Uppercase letters (A-Z)? (yes/no): yes
Lowercase letters (a-z)? (yes/no): yes
Numbers (0-9)? (yes/no): yes
Symbols (!@#$...)? (yes/no): yes

Your password: k7#Qm2!vRz9x

Generate another password? (yes/no): no
Thank you! Keep your passwords safe.
```

## Tech Used
- Python 3
- `random` and `string` modules

## Author
Pokuri Divya Sumana Sree
Oasis Infobyte - Python Programming Internship