#! python3

class Person:
    def __init__(self, first_name, last_name, title):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.title = title.title()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.title}"
