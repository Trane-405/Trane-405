
from PyQt6.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QPushButton,QLabel
from database.connection import get_connection

class LoginWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.user=None

        layout=QVBoxLayout()

        self.user_input=QLineEdit()
        self.user_input.setPlaceholderText("Usuario")

        self.pass_input=QLineEdit()
        self.pass_input.setPlaceholderText("Password")

        btn=QPushButton("Login")
        btn.clicked.connect(self.login)

        layout.addWidget(QLabel("POS Login"))
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(btn)

        self.setLayout(layout)

    def login(self):
        conn=get_connection()
        cur=conn.cursor()

        cur.execute(
        "SELECT username FROM users WHERE username=? AND password=?",
        (self.user_input.text(),self.pass_input.text())
        )

        row=cur.fetchone()
        conn.close()

        if row:
            self.user=row[0]
            self.accept()
