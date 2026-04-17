import secrets
import string

ALLOWED_SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

def generate_password(length: int = 16) -> str:

    """
    Generate a cryptographically secure random password.

    Args:
        length: Total password length (minimum 4).

    Returns:
        A password string containing at least one uppercase letter,
        one lowercase letter, one digit, and one symbol.

    Raises:
       ValueError: If length is less than 4.
    """

    if length < 4:
        raise ValueError(f"Password length must be at least 4, got {length}")
    
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + ALLOWED_SYMBOLS

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(ALLOWED_SYMBOLS),
        *[secrets.choice(all_chars) for _ in range(length - 4)]
    ]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main(count: int = 2, length: int = 16) -> None:
    print("\nPASSWORD GENERATOR")
    print(f"Generating {count} password(s), each {length} characters long.\n")

    for i in range(count):
        print(f"Password {i + 1}: {generate_password(length)}")
        
    print()

if __name__ == "__main__":
    main()