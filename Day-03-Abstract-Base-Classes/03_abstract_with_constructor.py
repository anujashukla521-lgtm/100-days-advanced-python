from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_details(self):
        pass

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_details(self):
        print("Student")
        print("-"*30)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("-"*30)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_details(self):
        print("Teacher")
        print("-"*30)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")

s = Student("Rahul", 22, "BCA")
t = Teacher("Harry", 45, "Python")

s.display_details()
t.display_details()