class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Age of {self.name} is {self.age} and pursuing {self.course}"

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} Course: {self.course}"

stu = Student("Rahul",19,"BCA")
print(stu)
print(repr(stu))