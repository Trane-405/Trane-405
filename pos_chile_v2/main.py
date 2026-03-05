
import sys
from PyQt6.QtWidgets import QApplication
from gui.login import LoginWindow
from gui.main_window import MainWindow
from database.init_db import init_db

def main():
    init_db()
    app = QApplication(sys.argv)

    login = LoginWindow()
    if login.exec():
        window = MainWindow(login.user)
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
