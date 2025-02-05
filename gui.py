from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget, QMessageBox)
import os
import csv
from encryption import cipher
from chatbot import chatbot_response, log_communication

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Chatbot GUI")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.layout.addWidget(self.chat_area)

        self.user_input = QLineEdit(self)
        self.user_input.returnPressed.connect(self.handle_send)
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_send)
        self.layout.addWidget(self.send_button)

        self.log_button = QPushButton("View Logs", self)
        self.log_button.clicked.connect(self.view_logs)
        self.layout.addWidget(self.log_button)

        self.delete_button = QPushButton("Delete Logs", self)
        self.delete_button.clicked.connect(self.delete_logs)
        self.layout.addWidget(self.delete_button)

        self.chat_area.append("Chatbot: Hello! I am here to assist you. Type 'bye' to exit.")

    def handle_send(self):
        user_input = self.user_input.text()
        if user_input.strip():
            bot_response = chatbot_response(user_input)
            self.chat_area.append(f"You: {user_input}")
            self.chat_area.append(f"Bot: {bot_response}")
            log_communication(user_input, bot_response)
        self.user_input.clear()

    def view_logs(self):
        file_name = "chatbot_log.csv"
        if not os.path.exists(file_name):
            QMessageBox.information(self, "Logs", "No log file found.")
            return

        try:
            with open(file_name, mode="r") as file:
                reader = csv.DictReader(file)
                decrypted_logs = []
                for row in reader:
                    decrypted_row = {}
                    for key, value in row.items():
                        if key == "Timestamp":
                            decrypted_row[key] = value
                        else:
                            decrypted_row[key] = cipher.decrypt(value.encode()).decode()
                    decrypted_logs.append(decrypted_row)

                logs_text = "\n".join([str(log) for log in decrypted_logs])
                QMessageBox.information(self, "Decrypted Logs", logs_text)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to read or decrypt logs: {e}")

    def delete_logs(self):
        file_name = "chatbot_log.csv"
        if os.path.exists(file_name):
            os.remove(file_name)
            QMessageBox.information(self, "Delete Logs", "All user data has been deleted.")
        else:
            QMessageBox.information(self, "Delete Logs", "No log file found to delete.")
