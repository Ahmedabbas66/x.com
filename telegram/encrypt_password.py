from cryptography.fernet import Fernet

# Load the encryption key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Prompt the user for a password
user_password = input("Enter the password to encrypt: ").encode()

# Encrypt the password
encrypted_password = cipher_suite.encrypt(user_password)
with open('password.bin', 'wb') as password_file:
    password_file.write(encrypted_password)

print("Password encrypted and saved to 'password.bin'")
