from dbconnect import store, fetch
from encrypt import encrypt, decrypt
from clipboard import copy_to_clipboard
from pwgenerate import generate_password

# --------DB OPERATIONS---------

def push(num_credentials=1, length=24):
    """Generate and store credentials in MongoDB."""
    generated_credentials = []
    generated_salt = []
    
    while len(generated_credentials) < num_credentials:
        application = input("Enter the application: ")
        username = input("Enter the username: ")
        master_password = input("Enter the master password: ")
        password = generate_password(length)

        encrypted_password, salt = encrypt(password, master_password)
        generated_credentials.append({"application": application, 
                                      "username": username, 
                                      "encrypted_password": encrypted_password
                                      })
        generated_salt.append({"application": application,
                               "salt": salt})
    print(generated_credentials)
    store(generated_credentials, generated_salt)

    print("Storage Successful.")
    return password

def pull():
    try:
        master_password = input("Enter the master password: ")
        application = input("Enter application: ")
        username, encrypted_password, salt = fetch(application)
        decrypted_password = decrypt(encrypted_password, salt, master_password)

        print("Your username is:", username)
        copy_to_clipboard(decrypted_password)
        
    except Exception as e:
        print("Wrong master password", e)

if __name__ == "__main__":
    # push()
    pull()