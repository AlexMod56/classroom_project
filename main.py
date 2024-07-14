import unittest
from Subject import Subject
from Human import Human
from Class import Class
from Student import Student
from Teacher import Teacher

person1 = Human("Alexander", "Modestov")

student1 = Student("Alice", "Smith", "5A")
student2 = Student("Adam", "Doe", "5A")
student3 = Student("Maxim", "Smirnov", "6B")
student4 = Student("Emily", "Johnson", "7C")
student5 = Student("Charlotte", "Davis", "7C")
student6 = Student("James", "Brown", "8C")
student7 = Student("Alexander", "Taylor", "5A")
student8 = Student("Sophia", "Miller", "5A")

teacher1 = Teacher("John", "Johnson", "5A", [Subject.MATH, Subject.PHYSICS])
teacher2 = Teacher("Liam", "Smith", "7C", [Subject.BIOLOGY, Subject.GENETICS])

classroom1 = Class(teacher1, [student1, student2, student7, student8])
classroom2 = Class(teacher2, [student4, student5])

###

print(person1.last_name)

print(student1.last_name)
print(student1.get_class())
student1.set_class("5B")
print(student1.get_class())
student1.set_class(classroom1)
print(student1.get_class())

print(teacher1.last_name)
print(teacher1._subjects)
print(teacher1.get_class())
teacher1.set_class("7C")
print(teacher1.get_class())
teacher1.set_class(classroom1)
print(teacher1.get_class())

print(classroom1._homeroom_teacher)
print(*classroom1, sep=", ")
print(classroom1[0])
print(len(classroom1))
classroom1.set_grade(8)
classroom1.set_letter("D")

print(student1.get_class())
print(teacher1.get_class())

print(classroom1["Smi"])
results = classroom1.search_students("Smi")
for student in results:
    print(student)

for student in classroom1:
    print(student)

print(hash(student1))
classroom1.append_func(student3)
print(classroom1._students)
classroom1.remove_func(student3)
print(classroom1._students)

print(student1 < student2)
print(Human.ids)

classroom1.write_csv("student_table.csv")
res_df = classroom1.read_csv("student_table.csv")

###Тестирование
class TestClassSortCheck(unittest.TestCase):

    def test_sort_by_lastname(self):

        sorted_students = classroom1.test_sort_by_lastname()

        sorted_by_lastnames = [student.last_name for student in sorted_students]

        self.assertEqual(sorted_by_lastnames, ["Miller", "Doe", "Smith", "Taylor"])# Error happened

if __name__ == "__main__":
    unittest.main()

