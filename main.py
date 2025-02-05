import sys
from PyQt5.QtWidgets import QApplication
from gui import ChatbotApp

def run_app():
    app = QApplication(sys.argv)
    chatbot_app = ChatbotApp()
    chatbot_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()