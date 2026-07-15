class ContextMemory:

    def __init__(self):

        self.history = []

    def add(self, role, message):

        self.history.append({
            "role": role,
            "content": message
        })

        # Sirf last 10 messages rakho
        if len(self.history) > 10:
            self.history.pop(0)

    def get(self):

        return self.history

    def clear(self):

        self.history.clear()