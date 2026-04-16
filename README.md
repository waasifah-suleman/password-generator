# Password Generator

## Overview
A secure command-line password generator built with Python. It creates strong, random passwords using cryptographic randomness and ensures each password contains a mix of uppercase letters, lowercase letters, digits, and symbols.

The project focuses on clean structure, reliability, and practical use of Python's standard library.

## Getting Started
```bash
git clone https://github.com/waasifah-suleman/password-generator.git
cd password-generator
python generator.py
```

## Features
- Generates secure 16-character passwords
- Uses Python's `secrets` module for cryptographic randomness
- Guarantees inclusion of uppercase letters, lowercase letters, numbers and special characters
- Outputs two password options per run
- Simple command-line interface

## How It Works
1. Selects at least one character from each required category
2. Fills the remaining length with random characters
3. Shuffles the final result to remove predictability

This guarantees complexity without relying on repeated generation attempts.

## Example Output
```
PASSWORD GENERATOR

Both passwords are 16 characters with uppercase, lowercase, numbers and symbols.

Password 1: X#9aK!2pLz@1QwE$
Password 2: mT&7dZ!qP3@rY8%L
```

## Technologies
- Python 3
- `secrets` — cryptographic randomness
- `string` — character sets

## Future Improvements
- User interface integration for improved usability
- Customizable password length and character types
- Secure password storage with encryption