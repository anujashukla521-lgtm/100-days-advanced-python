class Calculator:

    def __call__(self, num1, num2, operation):
       if operation == "+":
           return num1 + num2
       elif operation == "-":
           return num1 - num2
       elif operation == "*":
           return num1 * num2
       elif operation == "/":
           return num1 / num2
       else:
           return "Invalid operation"
       
cal = Calculator()

print(cal(10, 20, "+"))
print(cal(30, 20, "-"))
print(cal(10, 20, "*"))
print(cal(100, 20, "/"))


