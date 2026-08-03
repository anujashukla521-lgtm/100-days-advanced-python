class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor

    def course_details(self):
        print(f"Course name: {self.course_name}")
        print(f"Instructor: {self.instructor}")

class Exams:
    def __init__(self, total_marks, obtained_marks):
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks

    def marks(self):
        print(f"Total marks: {self.total_marks}")
        print(f"Obtained marks: {self.obtained_marks}")

class Student(Course, Exams):
    def __init__(self, course_name, instructor, total_marks, obtained_marks):
        Course.__init__(self, course_name, instructor)
        Exams.__init__(self, total_marks, obtained_marks)

    def result(self):
        percentage = (self.obtained_marks/self.total_marks)*100
        self.course_details()
        self.marks()
        print(f"Percentage: {percentage}")
        if percentage>35:
            print("Pass")
        else:
            print("Fail")

course_name = input("Enter course name: ")
instructor = input("Enter instructor: ")
total_marks = int(input("Enter total marks: "))
obtained_marks = int(input("Enter obtained marks: "))
stu = Student(course_name, instructor, total_marks, obtained_marks)
stu.result()