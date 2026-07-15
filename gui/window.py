from PySide6.QtWidgets import QWidget, QVBoxLayout

from core.assistant import Assistant
from gui.orbital_widget import OrbitalWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.assistant = Assistant()

        self.setWindowTitle("TORVAK AI OS")
        self.resize(1000, 700)

        self.orbital = OrbitalWidget(on_submit=self.execute_command)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.orbital)
        self.setLayout(layout)

    def execute_command(self, cmd: str):

        if cmd == "":
            return

        response = self.assistant.process(cmd)

        if response == "EXIT":
            self.close()
            return

        # Route the response to the orbital UI instead of a chat log.
        # Swap "System" for whichever module actually handled the command
        # once command_router exposes that info (e.g. via a return tuple).
        module = self._guess_module(cmd)
        self.orbital.set_active_module(module)
        self.orbital.push_event(module, response[:40])

    def _guess_module(self, cmd: str) -> str:
        """Temporary heuristic until command_router reports which module ran.
        Replace this with a real lookup from CommandRouter/AIRouter."""
        text = cmd.lower()
        if any(k in text for k in ["remember", "memory", "recall", "name"]):
            return "Memory"
        if any(k in text for k in ["code", "script", "python", "bug", "function"]):
            return "Coding"
        if any(k in text for k in ["search", "web", "google", "browse"]):
            return "Web"
        if any(k in text for k in ["listen", "speak", "voice", "say"]):
            return "Voice"
        if any(k in text for k in ["see", "camera", "screen", "look"]):
            return "Vision"
        return "System"