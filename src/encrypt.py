from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import secrets 

# Note to self: this code does not allow changing the master password later on since that is used for encryption


# higher level decrypt function that is actually called
def decrypt(encrypted_password, salt, master_password):
    key = derive_key(master_password, salt)
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password

# higher level decrypt function that is actually called
def encrypt(password_to_encrypt, master_password):
    encrypted_password, salt = encrypt_password(password_to_encrypt, master_password)
    return encrypted_password, salt

# -----------------------------------------------------------

# makes a key from the master password and salt to encrypt (SHA256)
def derive_key(master_password, salt):
    #  Password-Based Key Derivation Function 2 (PBKDF2)  
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(master_password.encode())
    
    return base64.urlsafe_b64encode(key)

# encrypts using the master password
def encrypt_password(password, master_password):
    # salt_length =16
    # salt = str(secrets.token_bytes(salt_length))
    
    salt = "some_salt_here"
    key = derive_key(master_password, salt)
    cipher = Fernet(key)
    
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password, salt
