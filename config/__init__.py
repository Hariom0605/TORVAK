def _ensure_structure(self):
    data = self.load()

    defaults = {
        "profile": {},
        "preferences": {},
        "facts": [],
        "projects": [],
        "tasks": [],
        "goals": [],
        "conversation": []
    }

    changed = False

    for key, value in defaults.items():
        if key not in data:
            data[key] = value
            changed = True

    if changed:
        self.save(data)
        