from Human import Human
from Class import Class


class Student(Human):
    _class: Class

    def __init__(self, name, last_name, _class = None):
        super().__init__(name, last_name)
        self._class = _class

    def set_class(self, class_name):
        self._class = class_name

    def get_class(self):
        return self._class

    def __str__(self):
        return f"Учащийся {self.name} {self.last_name} из {self._class}"

    def __repr__(self):
        return f"{self.name} {self.last_name}"
