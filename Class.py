from typing import List
import csv


class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, _homeroom_teacher, _students = []):
        super().__init__()
        self._grade = None
        self._letter = None
        self._homeroom_teacher = _homeroom_teacher
        self._students = sorted(_students, key=lambda student: (student.last_name, student.name))

    def __getitem__(self, name):
        if isinstance(name, str):
            lst_res = []
            for student in self._students:
                if student.name.lower().startswith(name.lower()) or student.last_name.lower().startswith(name.lower()):
                    lst_res.append(student)

            if len(lst_res) == 0:
                raise Exception("Нет учеников")
            else:
                return lst_res

        elif isinstance(name, int):
            return self._students[name]

    def __iter__(self):
        return iter(self._students)

    def __str__(self):
        return f"{self._grade}{self._letter}"

    def __repr__(self):
        return f"{self._grade}{self._letter}"

    def __len__(self):
        return len(self._students)

    def test_sort_by_lastname(self):
        return sorted(self._students, key=lambda student: student.last_name)

    def append_func(self, student):
        self._students.append(student)

    def remove_func(self, student):
        self._students.remove(student)

    def set_grade(self, grade_to_ed):
        self._grade = grade_to_ed

    def set_letter(self, letter_to_ed):
        self._letter = letter_to_ed

    def search_students(self, query):
        return [student for student in self._students if query in student.name or query in student.last_name]

    def write_csv(self, filename):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Last_Name", "Status"])
            writer.writerow([self._homeroom_teacher.name, self._homeroom_teacher.last_name, "Teacher"])
            for student in self._students:
                writer.writerow([student.name, student.last_name, "Student"])

    @staticmethod
    def read_csv(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append((row['Name'], row['Last_Name'], row['Status']))

        print("File is uploaded!")
        return students
