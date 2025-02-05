import csv
from cryptography.fernet import Fernet

# Load the encryption key
KEY_FILE = "encryption_key.key"
try:
    with open(KEY_FILE, "rb") as key_file:
        cipher = Fernet(key_file.read())
except Exception as e:
    print(f"Error loading encryption key: {e}")
    exit()

# File containing the encrypted logs
file_name = "chatbot_log.csv"

# Function to decrypt a value
def decrypt_value(encrypted_value):
    try:
        return cipher.decrypt(encrypted_value.encode()).decode()
    except Exception as e:
        return f"Error decrypting: {e}"

# Read and decrypt the log file
def read_and_decrypt_log():
    try:
        with open(file_name, mode="r") as file:
            reader = csv.DictReader(file)
            print("Decrypted Log:")
            for row in reader:
                decrypted_row = {}
                for key, value in row.items():
                    if key == "Timestamp":  # Skip decryption for the timestamp
                        decrypted_row[key] = value
                    else:
                        decrypted_row[key] = decrypt_value(value)
                print(decrypted_row)
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except Exception as e:
        print(f"Error reading or decrypting log: {e}")

# Run the decryption function
if __name__ == "__main__":
    read_and_decrypt_log()
