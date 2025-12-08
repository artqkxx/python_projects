class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        return f"{self.name}: {self.grade}"


class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("Учнів немає")
        else:
            for s in self.students:
                print(s.info())

    def show_best(self):
        if not self.students:
            print("Учнів немає")
            return

