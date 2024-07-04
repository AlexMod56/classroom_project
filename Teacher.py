from Human import Human
from Class import Class
from Subject import Subject
from typing import List


class Teacher(Human):
    _homeroom_class: Class
    _subjects: List[Subject]

    def __init__(self, name, last_name, _homeroom_class = None, _subjects = []):
        super().__init__(name, last_name)
        self._homeroom_class = _homeroom_class
        self._subjects = _subjects

    def set_class(self, class_name):
        self._homeroom_class = class_name

    def get_class(self):
        return self._homeroom_class

    def __str__(self):
        return f"Учитель {self.name} {self.last_name}"

    def __repr__(self):
        return f"{self.name} {self.last_name}"
