class Animal:
    def speak(self):
        print("Animal's speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
print(Dog.mro())
print(Dog.__mro__)