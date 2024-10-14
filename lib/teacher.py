#!/usr/bin/env python

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"]  # Add some default lessons

    def teach(self):
        return self.knowledge[0]  # Returns the first lesson in the knowledge list
