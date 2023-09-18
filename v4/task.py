class Task:
    def __init__(self, desc):
        self.description = desc
        self.done = False
    
    def done(self):
        self.done = True
