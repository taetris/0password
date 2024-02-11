from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(master_password.encode())
    print("key:", key)
    return base64.urlsafe_b64encode(key)

def encrypt_password(password, master_password):
    salt = 'some_salt_here'  # You can generate a random salt for each password
    
    key = derive_key(master_password, salt)
    cipher = Fernet(key)
    print("salt:", salt, "\n cipher:", cipher)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password, salt

def decrypt_password(encrypted_password, salt, master_password):
    key = derive_key(master_password, salt)
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password

# Example usage:
master_password = "my_master_password"
password_to_encrypt = "my_password"

encrypted_password, salt = encrypt_password(password_to_encrypt, master_password)
print("Encrypted password:", encrypted_password)

decrypted_password = decrypt_password(encrypted_password, salt, master_password)
print("Decrypted password:", decrypted_password)
