class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def stud(self):
        print("I am a student.")

stud1 = Student("harshal", 19, 95)

stud1.display()
stud1.stud()

stud1.marks = 98
stud1.name = "harshal"

stud1.display()
