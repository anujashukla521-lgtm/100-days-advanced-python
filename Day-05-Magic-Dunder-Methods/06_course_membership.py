class Course:
    def __init__(self, students):
        self.students = students

    def __contains__(self, student):
        return student in self.students

course = Course(["Rahul", "Priya", "Harry"])

print("Anuja" in course)
print("Rahul" in course)