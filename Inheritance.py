class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        Employee.__init__(self, name, age, employee_id, salary)
        self.department = department

    def show_manager(self):
        print("Department:", self.department)


m1 = Manager("Harshal", 19, "ADT25SOCB0448", 50000, "CSE")

m1.show_person()
m1.show_employee()
m1.show_manager()
