from .dbconnect import store, fetch
from .encrypt import encrypt, decrypt
from .clipboard import copy_to_clipboard
from .pwgenerate import generate_password
from .creds import  default_username, default_master_password
import sys
# --------DB OPERATIONS---------

def inputs():
    application = input("Enter the application: ")
    username = input("Enter the username: ")
    return application, username

# actual operations to generate password and store in MongoDB.
def push(application, username, length=24):
    # Get master password
    master_password = default_master_password
    
    # If username is not provided, use default
    if not username:
        username = default_username
        
    # Generate password
    password = generate_password(length)

    # Encrypt password
    encrypted_password, salt = encrypt(password, master_password)

    # Create credentials dictionary
    credentials_dict = {
        "application": application,
        "username": username,
        "encrypted_password": encrypted_password,
        
    }
    salt_dict = {
        "application": application,
        "salt": salt
    }
    # Store credentials
    store(credentials_dict, salt_dict)

    print("\nProcess finished.")
    return password


# actual operation used to get the decrypted password in the clipboard
def pull():
    try:
        master_password = input("Enter the master password: ")
        application = input("Enter application: ")
        username, encrypted_password, salt = fetch(application)
        decrypted_password = decrypt(encrypted_password, salt, master_password)

        print("\n Your username is:", username)
        copy_to_clipboard(decrypted_password)

        # the entire decryption method fails if wrong master password 
    except Exception as e:
        print("Wrong master password", e)


if __name__ == "__main__":
    option = sys.argv[1]
    if option == "push":
        application, username = inputs()
        push(application, username)
    elif option == "pull":
        pull()
    else:
        print("Invalid option. Use 'push' or 'pull'.")
        sys.exit(1)