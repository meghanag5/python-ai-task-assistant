class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

def __str__(self):
    if self.completed == False:
        status = "Not Done"
    else: 
        status = "Done"
    return self.title + " - " +status

def to_dict(self):
    return {
        "title": self.title,
        "completed": self.completed
    }