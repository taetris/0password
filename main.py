import random
import string

def generate_password(length=24):
    """Generate a unique password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

def check_unique(password, existing_passwords):
    """Check if the generated password is unique."""
    return password not in existing_passwords

def main(num_credentials=1, length=24):
    """Generate and store credentials in MongoDB."""
    existing_passwords = set()
    generated_credentials = []
    
    while len(generated_credentials) < num_credentials:
        application = input("Enter the application: ")
        username = input("Enter the username: ")
        password = generate_password(length)
        if check_unique(password, existing_passwords):
            existing_passwords.add(password)
            generated_credentials.append({"application": application, "username": username, "password": password})
    print(generated_credentials)
    # store_in_mongodb(generated_credentials)
    print("Credentials stored in MongoDB.")

if __name__ == "__main__":
    main()