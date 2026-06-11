from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
)

from core.command_router import CommandRouter
from core.assistant import Assistant

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.assistant = Assistant()

        self.setWindowTitle("TORVAK AI OS")
        self.resize(1000, 700)

        layout = QVBoxLayout()

        title = QLabel("🤖 TORVAK")
        title.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
            color:white;
        """)

        self.status = QLabel("Status : Online")
        self.status.setStyleSheet("color:white;font-size:16px;")

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter command...")

        button = QPushButton("Execute")
        button.clicked.connect(self.execute_command)

        layout.addWidget(title)
        layout.addWidget(self.status)
        layout.addWidget(self.chat)
        layout.addWidget(self.input)
        layout.addWidget(button)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background:#181818;
            }

            QTextEdit{
                background:#202020;
                color:white;
                font-size:15px;
            }

            QLineEdit{
                background:#303030;
                color:white;
                font-size:15px;
            }

            QPushButton{
                background:#0078D7;
                color:white;
                font-size:16px;
                height:40px;
            }
        """)

    def execute_command(self):

        cmd = self.input.text()

        if cmd == "":
            return

        self.chat.append(f"You : {cmd}")

        response = self.assistant.process(cmd)

        if response == "EXIT":
            self.close()
            return

        self.chat.append(f"TORVAK : {response}")
        self.chat.append("")

        self.input.clear()