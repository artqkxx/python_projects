
class Car:

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
    def info(self):
        print(f"Це {self.color} {self.model} {self.year} року")
Car1 = Car(color = "синя", model = "Tesla", year = 2023)
print(Car1.info())

class Student:

    def __init__(self, name, group, mark):
        self.name = name
        self.group = group
        self.mark = int(mark)

    def info(self):
        print(f"{self.name} {self.group} {self.mark}")


Student1 = Student(name = "Бро", group = "10B", mark = "10")
print(Student1.info())
if Student1.mark > 90:
    print("Відмінник")
else:
    print("Звичайний студент")




class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

