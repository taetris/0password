import random
import string
from dbconnect import store_in_mongodb, fetch_from_mongodb
from encrypt import encrypt, decrypt

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

def push(num_credentials=1, length=24):
    """Generate and store credentials in MongoDB."""
    generated_credentials = []
    
    while len(generated_credentials) < num_credentials:
        application = input("Enter the application: ")
        username = input("Enter the username: ")
        master_password = input("Enter the master password: ")
        password = generate_password(length)

        encrypted_password, salt = encrypt(password, master_password)
        generated_credentials.append({"application": application, 
                                      "username": username, 
                                      "encrypted_password": encrypted_password, 
                                      "salt": salt})
    print(generated_credentials)
    store_in_mongodb(generated_credentials)
    print("Credentials stored in MongoDB.")

def fetch():
    try:
        master_password = input("Enter the master password: ")
        
        username, encrypted_password, salt = fetch_from_mongodb("gitmap")
        decrypted_password = decrypt(encrypted_password, salt, master_password)
        print("Your password is:", decrypted_password)
    except Exception as e:
        print("Wrong master password", e)

if __name__ == "__main__":
    # push()
    fetch()