class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry", "Gryffindor")
professor = Professor("Albus", "Head Master")
wizard = Wizard("Top")