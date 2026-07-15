import json
import os


class MemoryEngine:

    def __init__(self):
        self.path = "memory/memory.json"

        os.makedirs("memory", exist_ok=True)

        if not os.path.exists(self.path):
            self._create_memory()

    def _create_memory(self):
        data = {
            "profile": {},
            "preferences": {},
            "facts": [],
            "projects": [],
            "tasks": [],
            "goals": [],
            "conversation": []
        }

        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------- PROFILE ---------------- #

    def save_profile(self, key, value):
        data = self.load()
        data["profile"][key] = value
        self.save(data)

    def get_profile(self, key):
        return self.load()["profile"].get(key)

    # ---------------- PREFERENCES ---------------- #

    def save_preference(self, key, value):
        data = self.load()
        data["preferences"][key] = value
        self.save(data)

    def get_preferences(self):
        return self.load()["preferences"]

    # ---------------- FACTS ---------------- #

    def add_fact(self, fact):
        data = self.load()

        if fact not in data["facts"]:
            data["facts"].append(fact)

        self.save(data)

    def get_facts(self):
        return self.load()["facts"]

    # ---------------- PROJECTS ---------------- #

    def add_project(self, project):
        data = self.load()

        if project not in data["projects"]:
            data["projects"].append(project)

        self.save(data)

    def get_projects(self):
        return self.load()["projects"]

    # ---------------- TASKS ---------------- #

    def add_task(self, task):
        data = self.load()

        if task not in data["tasks"]:
            data["tasks"].append(task)

        self.save(data)

    def get_tasks(self):
        return self.load()["tasks"]

    # ---------------- GOALS ---------------- #

    def add_goal(self, goal):
        data = self.load()

        if goal not in data["goals"]:
            data["goals"].append(goal)

        self.save(data)

    def get_goals(self):
        return self.load()["goals"]