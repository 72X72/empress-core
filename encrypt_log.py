from cryptography.fernet import Fernet
import os

key = os.environ['EMPRESS_KEY']
cipher = Fernet(key)

mutation_dir = os.path.expanduser("~/empress/mutations")
for file in os.listdir(mutation_dir):
    if file.endswith(".log"):
        with open(f"{mutation_dir}/{file}", "rb") as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(f"{mutation_dir}/{file}.enc", "wb") as f:
            f.write(encrypted)
