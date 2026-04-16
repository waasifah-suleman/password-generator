import secrets
import string

def generate_password(length=16):

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():

    print("\nPASSWORD GENERATOR")
    print("\nBoth passwords are 16 characters with uppercase, lowercase, numbers and symbols.\n")

    print(f"Password 1: {generate_password()}")
    print(f"Password 2: {generate_password()}\n")
    
if __name__ == "__main__":
    main()