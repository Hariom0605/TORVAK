from config.command import commands
from core.system_control import SystemControl
system = SystemControl()

class CommandRouter:

    def execute(self, command: str):

        command = command.lower().strip()

        # ---------------- Apps ----------------

        if "open chrome" in command:
            system.open_chrome()
            return "Opening Chrome"

        elif "open calculator" in command:
            system.open_calculator()
            return "Opening Calculator"

        elif "open notepad" in command:
            system.open_notepad()
            return "Opening Notepad"

        elif "open vscode" in command:
            system.open_vscode()
            return "Opening VS Code"

        elif "open downloads" in command:
            system.open_downloads()
            return "Opening Downloads"

        elif "open documents" in command:
            system.open_documents()
            return "Opening Documents"

        elif "open desktop" in command:
            system.open_desktop()
            return "Opening Desktop"

        # ---------------- Websites ----------------

        elif "open youtube" in command:
            system.open_youtube()
            return "Opening YouTube"

        elif "open google" in command:
            system.open_google()
            return "Opening Google"

        elif command.startswith("search google"):

            query = command.replace(
                "search google",
                ""
            ).strip()

            system.search_google(query)

            return f"Searching Google : {query}"

        elif command.startswith("search youtube"):

            query = command.replace(
                "search youtube",
                ""
            ).strip()

            system.search_youtube(query)

            return f"Searching YouTube : {query}"

        # ---------------- Screenshot ----------------

        elif "take screenshot" in command:
            system.screenshot()
            return "Screenshot Saved"

        # ---------------- Exit ----------------

        elif command == "exit":
            return "EXIT"

        return "Command Not Found"