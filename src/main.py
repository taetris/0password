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
def push(num_credentials=1, length=24):
    # application, username = inputs()

    generated_credentials = []
    generated_salt = []
    
    while len(generated_credentials) < num_credentials:

        master_password = default_master_password

        if not username:
            username = default_username
        
        password = generate_password(length)

        encrypted_password, salt = encrypt(password, master_password)
        generated_credentials.append({"application": application, 
                                      "username": username, 
                                      "encrypted_password": encrypted_password
                                      })remove
        generated_salt.append({"application": application,
                               "salt": salt})
    print(generated_credentials)
    store(generated_credentials, generated_salt)

    print("\nStorage Successful.")
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
        push()
    elif option == "pull":
        pull()
    else:
        print("Invalid option. Use 'push' or 'pull'.")
        sys.exit(1)