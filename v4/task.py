import json


class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Not Done"
        return f"[{status}] {self.description}"
