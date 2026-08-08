class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("A", 89)
s2 = Student("B", 97)

print(s1 == s2)
print(s1 > s2)
print(s1 < s2)