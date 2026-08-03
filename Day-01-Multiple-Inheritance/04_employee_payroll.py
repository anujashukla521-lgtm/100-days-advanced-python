class Salary:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def showSalary(self):
        print(f"Basic Salary: {self.basic_salary}")

class Bonus:
    def __init__(self, bonus):
        self.bonus = bonus

    def showBonus(self):
        print(f"Bonus: {self.bonus}")

class Employee(Salary, Bonus):
    def __init__(self, basic_salary, bonus):
        Salary.__init__(self, basic_salary)
        Bonus.__init__(self, bonus)

    def calculate_total_salary(self):
        total_salary = self.basic_salary + self.bonus

        self.showSalary()
        self.showBonus()
        print(f"Total Salary: {total_salary}")


emp = Employee(45000,500)
emp.calculate_total_salary()