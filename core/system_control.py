import os
import subprocess
import webbrowser
import pyautogui
from pathlib import Path


class SystemControl:

    def open_chrome(self):
        subprocess.Popen("start chrome", shell=True)

    def open_calculator(self):
        subprocess.Popen("calc", shell=True)

    def open_notepad(self):
        subprocess.Popen("notepad", shell=True)

    def open_vscode(self):
        subprocess.Popen("code", shell=True)

    def open_downloads(self):
        os.startfile(str(Path.home() / "Downloads"))

    def open_documents(self):
        os.startfile(str(Path.home() / "Documents"))

    def open_desktop(self):
        os.startfile(str(Path.home() / "Desktop"))

    def open_youtube(self):
        webbrowser.open("https://youtube.com")

    def open_google(self):
        webbrowser.open("https://google.com")

    def search_google(self, query):
        webbrowser.open(f"https://www.google.com/search?q={query}")

    def search_youtube(self, query):
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

    def screenshot(self):

        os.makedirs("screenshots", exist_ok=True)

        image = pyautogui.screenshot()

        image.save("screenshots/screenshot.png")