import os
import csv
from datetime import datetime
from cryptography.fernet import Fernet

KEY_FILE = "encryption_key.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as key_file:
    cipher = Fernet(key_file.read())

def sanitize_input(user_input):
    return user_input.replace("@", "[at]").replace("+", "[plus]")

def log_communication(user_input, bot_response):
    sanitized_input = sanitize_input(user_input)
    log_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User Input": sanitized_input,
        "Bot Response": bot_response
    }
    file_name = "chatbot_log.csv"
    try:
        file_exists = os.path.exists(file_name)
        with open(file_name, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Timestamp", "User Input", "Bot Response"])
            if not file_exists:
                writer.writeheader()
            encrypted_entry = {key: cipher.encrypt(value.encode()).decode() for key, value in log_entry.items()}
            writer.writerow(encrypted_entry)
    except Exception as e:
        print(f"Error logging communication: {e}")
