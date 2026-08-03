class Academics:
    def __init__(self, student_name, course):
        self.student_name = student_name
        self.course = course

    def show_academics(self):
        print(f"Name: {self.student_name}")
        print(f"Course: {self.course}")

class Sports:
    def __init__(self, sport_name, medals):
        self.sport_name = sport_name
        self.medals = medals

    def show_sports(self):
        print(f"Sport: {self.sport_name}")
        print(f"Medals: {self.medals}")

class Student(Academics, Sports):
    def __init__(self,student_name, course, sport_name, medals):
        Academics.__init__(self, student_name, course)
        Sports.__init__(self, sport_name, medals)

    def show_complete_profile(self):
        print("-----STUDENT PROFILE-----")
        self.show_academics()
        self.show_sports()

s = Student("Anuja Shukla", "BCA", "Chess", "2")
s.show_complete_profile()


